"""
Analiză statică pentru puncte critice în cod (ramuri, complexitate, excepții)
și priorizarea testelor după impactul potențial asupra acestor zone.
"""
from __future__ import annotations

import ast
import os
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any


@dataclass
class CriticalPoint:
    line: int
    kind: str
    detail: str


@dataclass
class MethodMetrics:
    name: str
    lineno: int
    branch_nodes: int
    raise_count: int
    cyclomatic: int
    criticality_score: float
    points: list[CriticalPoint] = field(default_factory=list)


def _cyclomatic_increment(node: ast.AST) -> int:
    if isinstance(node, (ast.If, ast.While, ast.For)):
        return 1
    if isinstance(node, ast.ExceptHandler):
        return 1
    if isinstance(node, ast.BoolOp):
        return len(node.values) - 1
    if isinstance(node, ast.comprehension) and node.ifs:
        return len(node.ifs)
    return 0


class _FunctionAnalyzer(ast.NodeVisitor):
    def __init__(self, name: str, lineno: int) -> None:
        self.name = name
        self.lineno = lineno
        self.branch_nodes = 0
        self.raise_count = 0
        self.cyclomatic = 1
        self.points: list[CriticalPoint] = []

    def generic_visit(self, node: ast.AST) -> None:
        inc = _cyclomatic_increment(node)
        if inc:
            self.cyclomatic += inc
            if isinstance(node, ast.If):
                self.branch_nodes += 1
                try:
                    src = ast.unparse(node.test)
                except Exception:
                    src = "condiție"
                self.points.append(
                    CriticalPoint(node.lineno, "decizie", f"if ({src})")
                )
            elif isinstance(node, ast.ExceptHandler):
                self.branch_nodes += 1
                self.points.append(
                    CriticalPoint(node.lineno, "excepție", "except")
                )
        if isinstance(node, (ast.Raise, ast.Assert)):
            self.raise_count += 1
            if isinstance(node, ast.Raise):
                self.points.append(CriticalPoint(node.lineno, "raise", "raise"))
        super().generic_visit(node)


def analyze_module(source_path: str | Path) -> dict[str, MethodMetrics]:
    path = Path(source_path)
    tree = ast.parse(path.read_text(encoding="utf-8"), filename=str(path))
    out: dict[str, MethodMetrics] = {}

    for node in tree.body:
        if isinstance(node, ast.ClassDef):
            for item in node.body:
                if isinstance(item, (ast.FunctionDef, ast.AsyncFunctionDef)):
                    an = _FunctionAnalyzer(item.name, item.lineno)
                    an.visit(item)
                    score = float(
                        2.5 * an.cyclomatic
                        + 1.8 * an.branch_nodes
                        + 1.2 * an.raise_count
                    )
                    out[item.name] = MethodMetrics(
                        name=item.name,
                        lineno=item.lineno,
                        branch_nodes=an.branch_nodes,
                        raise_count=an.raise_count,
                        cyclomatic=an.cyclomatic,
                        criticality_score=round(score, 2),
                        points=sorted(an.points, key=lambda p: p.line),
                    )
    return out


def _test_calls_methods(func: ast.FunctionDef) -> set[str]:
    names: set[str] = set()
    for n in ast.walk(func):
        if isinstance(n, ast.Call) and isinstance(n.func, ast.Attribute):
            names.add(n.func.attr)
    return names


def _test_uses_raises(func: ast.FunctionDef) -> bool:
    for n in ast.walk(func):
        if isinstance(n, ast.With):
            for item in n.items:
                c = item.context_expr
                if isinstance(c, ast.Call) and isinstance(c.func, ast.Attribute):
                    if c.func.attr == "raises":
                        return True
                if isinstance(c, ast.Name) and c.id == "raises":
                    return True
    return False


def test_function_scores(
    test_path: str | Path, metrics: dict[str, MethodMetrics]
) -> dict[str, float]:
    path = Path(test_path)
    tree = ast.parse(path.read_text(encoding="utf-8"), filename=str(path))
    scores: dict[str, float] = {}

    for node in tree.body:
        if not isinstance(node, ast.FunctionDef):
            continue
        if not node.name.startswith("test"):
            continue
        called = _test_calls_methods(node)
        base = 0.0
        for m in called:
            if m in metrics:
                base = max(base, metrics[m].criticality_score)
        if _test_uses_raises(node):
            base += 2.0
        scores[node.name] = base

    return scores


def ordered_test_names_by_criticality(
    test_path: str | Path, source_path: str | Path
) -> list[str]:
    metrics = analyze_module(source_path)
    scores = test_function_scores(test_path, metrics)
    names = [n for n, _ in sorted(scores.items(), key=lambda x: -x[1])]
    return names


def format_report_for_prompt(source_path: str | Path) -> str:
    metrics = analyze_module(source_path)
    lines: list[str] = [
        "PUNCTE CRITICE (prioritate pentru testare — complexitate și ramuri):",
    ]
    ranked = sorted(
        metrics.values(), key=lambda m: -m.criticality_score
    )
    for m in ranked:
        lines.append(
            f"- {m.name} (linia {m.lineno}): scor={m.criticality_score}, "
            f"ciclomatic≈{m.cyclomatic}, ramuri={m.branch_nodes}, raise={m.raise_count}"
        )
        for p in m.points[:12]:
            lines.append(f"    L{p.line} [{p.kind}] {p.detail}")
    return "\n".join(lines)


def _default_source_path(collection_root: Path) -> Path | None:
    env = os.environ.get("CRITICALITY_SOURCE")
    if env:
        p = Path(env)
        if p.is_file():
            return p
    candidate = collection_root / "bank_account.py"
    if candidate.is_file():
        return candidate
    return None


def _pytest_item_path(item: Any) -> Path:
    p = getattr(item, "path", None)
    if p is not None:
        return Path(p)
    return Path(str(item.fspath))


def prioritize_pytest_items(items: list[Any], source_path: str | Path | None = None) -> None:
    if not items:
        return
    metrics_by_src: dict[str, dict[str, MethodMetrics]] = {}
    scores_by_test: dict[str, dict[str, float]] = {}

    def metrics_for(root: Path) -> dict[str, MethodMetrics] | None:
        src = Path(source_path) if source_path else _default_source_path(root)
        if not src or not src.is_file():
            return None
        key = str(src.resolve())
        if key not in metrics_by_src:
            metrics_by_src[key] = analyze_module(src)
        return metrics_by_src[key]

    def score_for(it: Any) -> float:
        tp = _pytest_item_path(it)
        root = tp.parent
        m = metrics_for(root)
        if not m:
            return 0.0
        tk = str(tp.resolve())
        if tk not in scores_by_test:
            scores_by_test[tk] = test_function_scores(tp, m)
        name = getattr(it, "originalname", it.name)
        return scores_by_test[tk].get(name, 0.0)

    items.sort(key=lambda it: -score_for(it))


if __name__ == "__main__":
    import sys

    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except Exception:
        pass
    target = sys.argv[1] if len(sys.argv) > 1 else "bank_account.py"
    print(format_report_for_prompt(target))
