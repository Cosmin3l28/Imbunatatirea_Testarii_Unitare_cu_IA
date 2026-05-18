import pytest


def pytest_addoption(parser: pytest.Parser) -> None:
    parser.addoption(
        "--no-criticality-order",
        action="store_true",
        default=False,
        help="Nu reordona testele după analiza de criticitate.",
    )


def pytest_collection_modifyitems(
    config: pytest.Config, items: list[pytest.Item]
) -> None:
    if config.getoption("--no-criticality-order"):
        return
    try:
        from criticality import prioritize_pytest_items

        prioritize_pytest_items(items)
    except Exception:
        pass
