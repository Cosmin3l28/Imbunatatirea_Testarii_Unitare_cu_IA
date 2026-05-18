# Comenzi pentru prezentare (copy-paste)

## 1) Intrare în proiect (WSL)

```bash
cd /mnt/c/Users/Malina/Desktop/Proiect_T10_AII/Proiect_T10_AI
source .venv/bin/activate
```

## 2) Rulare teste normale

```bash
python -m pytest -q test_bank_account_V2.py
python -m pytest -q test_manual.py
```

## 3) Rulare acoperire (coverage)

```bash
python -m pytest test_bank_account_V2.py --cov=bank_account --cov-branch --cov-report=term-missing
```

## 4) Rulare raport criticitate

```bash
python criticality.py bank_account.py
```

## 5) Mutation testing - suita AI

```bash
cp setup.ai.cfg setup.cfg
rm -rf .mutmut-cache mutants
mutmut run
mutmut results
```

## 6) Mutation testing - suita manuala

```bash
cp setup.manual.cfg setup.cfg
rm -rf .mutmut-cache mutants
mutmut run
mutmut results
```

## 7) Detalii pentru un mutant (optional)

```bash
mutmut show 3
```

## 8) Ce spui la final (rezultate obtinute)

- AI (`test_bank_account_V2.py`): 20/20 mutanti omorati, 0 supravietuitori (100%)
- Manual (`test_manual.py`): 6/20 mutanti omorati, 14 supravietuitori (30%)
