import pytest
from bank_account import BankAccount

def test_bank_account_init_default_balance():
    """
    Test case pentru metoda BankAccount.__init__ cu sold inițial implicit.
    
    Functional Testing:
    - Equivalence Partitioning: Testează partiția valorii implicite pentru `balance`.
    - Boundary Value Analysis: N/A, deoarece este un argument implicit, nu un parametru de intrare direct pentru acest test.
    
    Structural Testing:
    - Statement Coverage: Acoperă instrucțiunea `self.balance = balance` când `balance` este valoarea sa implicită (0.0).
    - Branch/Decision Coverage: N/A, constructorul `__init__` nu are ramuri (decizii) în acest caz.
    
    Oracle & RIP Model:
    - Reachability: Apelul `BankAccount()` creează un obiect nou.
    - Infection: Starea `self.balance` a obiectului este setată la `0.0`.
    - Propagation: Se verifică (`assert`) că `account.balance` este `0.0`.
    
    Avoid Random Testing:
    - S-a creat explicit un cont fără a specifica un sold, invocând astfel valoarea implicită.
    """
    account = BankAccount()
    assert account.balance == 0.0

def test_bank_account_init_custom_balance():
    """
    Test case pentru metoda BankAccount.__init__ cu un sold inițial personalizat.
    
    Functional Testing:
    - Equivalence Partitioning: Testează partiția pentru valori pozitive valide pentru `balance`.
    - Boundary Value Analysis: N/A, se folosește o valoare pozitivă tipică, nu o limită specifică.
    
    Structural Testing:
    - Statement Coverage: Acoperă instrucțiunea `self.balance = balance` când `balance` este o valoare personalizată.
    - Branch/Decision Coverage: N/A.
    
    Oracle & RIP Model:
    - Reachability: Apelul `BankAccount(100.0)` creează un obiect nou cu un sold specific.
    - Infection: Starea `self.balance` a obiectului este setată la `100.0`.
    - Propagation: Se verifică (`assert`) că `account.balance` este `100.0`.
    
    Avoid Random Testing:
    - S-a creat explicit un cont cu un sold inițial pozitiv specific.
    """
    account = BankAccount(100.0)
    assert account.balance == 100.0

def test_deposit_positive_amount():
    """
    Test case pentru metoda deposit cu o sumă pozitivă validă.
    
    Functional Testing:
    - Equivalence Partitioning: Testează partiția validă pentru 'amount' (numere pozitive).
    - Boundary Value Analysis: Testează o sumă pozitivă tipică, departe de limite.
    
    Structural Testing:
    - Statement Coverage: Acoperă instrucțiunile `self.balance += amount` și `return self.balance`.
    - Branch/Decision Coverage: Acoperă ramura FALSE a deciziei `if amount <= 0:`.
    
    Oracle & RIP Model:
    - Reachability: Apelul `account.deposit(50.0)` este executat pe un cont cu `balance = 100.0`.
    - Infection: Starea `self.balance` se modifică de la `100.0` la `150.0`.
    - Propagation: Se verifică (`assert`) valoarea returnată (`new_balance`) și soldul intern al contului (`account.balance`).
    
    Avoid Random Testing:
    - S-au folosit sold inițial și sumă de depunere specifice și semantice.
    """
    account = BankAccount(100.0)
    deposited_amount = 50.0
    expected_balance = 150.0

    new_balance = account.deposit(deposited_amount)
    
    assert new_balance == expected_balance
    assert account.balance == expected_balance

def test_deposit_minimum_positive_amount():
    """
    Test case pentru metoda deposit cu cea mai mică sumă pozitivă posibilă.
    
    Functional Testing:
    - Equivalence Partitioning: Testează partiția validă pentru 'amount' (numere pozitive).
    - Boundary Value Analysis: Testează limita inferioară a partiției valide pozitive (0 + epsilon).
    
    Structural Testing:
    - Statement Coverage: Acoperă instrucțiunile `self.balance += amount` și `return self.balance`.
    - Branch/Decision Coverage: Acoperă ramura FALSE a deciziei `if amount <= 0:`.
    
    Oracle & RIP Model:
    - Reachability: Apelul `account.deposit(0.01)` este executat pe un cont cu `balance = 0.0`.
    - Infection: Starea `self.balance` se modifică de la `0.0` la `0.01`.
    - Propagation: Se verifică (`assert`) valoarea returnată (`new_balance`) și soldul intern al contului (`account.balance`).
    
    Avoid Random Testing:
    - S-au folosit sold inițial și valoarea limită precisă `0.01` în mod explicit.
    """
    account = BankAccount(0.0)
    deposited_amount = 0.01 
    expected_balance = 0.01

    new_balance = account.deposit(deposited_amount)
    
    assert new_balance == expected_balance
    assert account.balance == expected_balance

def test_deposit_zero_amount_raises_error():
    """
    Test case pentru metoda deposit când suma este zero.
    
    Functional Testing:
    - Equivalence Partitioning: Testează partiția invalidă pentru 'amount' (numere non-pozitive).
    - Boundary Value Analysis: Testează valoarea limită '0' pentru intrare invalidă.
    
    Structural Testing:
    - Statement Coverage: Acoperă instrucțiunile `if amount <= 0:` și `raise ValueError(...)`.
    - Branch/Decision Coverage: Acoperă ramura TRUE a deciziei `if amount <= 0:`.
    
    Oracle & RIP Model:
    - Reachability: Apelul `account.deposit(0)` este executat.
    - Infection: Excepția `ValueError` este declanșată.
    - Propagation: `pytest.raises` verifică tipul și mesajul excepției declanșate. Soldul contului este verificat să nu se fi modificat.
    
    Avoid Random Testing:
    - S-a folosit valoarea limită invalidă exactă `0`.
    """
    account = BankAccount(100.0)
    with pytest.raises(ValueError, match="Suma depusă trebuie să fie pozitivă."):
        account.deposit(0)
    # Verifică că soldul nu s-a modificat
    assert account.balance == 100.0

def test_deposit_negative_amount_raises_error():
    """
    Test case pentru metoda deposit când suma este negativă.
    
    Functional Testing:
    - Equivalence Partitioning: Testează partiția invalidă pentru 'amount' (numere non-pozitive).
    - Boundary Value Analysis: Testează o valoare negativă.
    
    Structural Testing:
    - Statement Coverage: Acoperă instrucțiunile `if amount <= 0:` și `raise ValueError(...)`.
    - Branch/Decision Coverage: Acoperă ramura TRUE a deciziei `if amount <= 0:`.
    
    Oracle & RIP Model:
    - Reachability: Apelul `account.deposit(-10.0)` este executat.
    - Infection: Excepția `ValueError` este declanșată.
    - Propagation: `pytest.raises` verifică tipul și mesajul excepției declanșate. Soldul contului este verificat să nu se fi modificat.
    
    Avoid Random Testing:
    - S-a folosit o valoare negativă specifică `-10.0`.
    """
    account = BankAccount(100.0)
    with pytest.raises(ValueError, match="Suma depusă trebuie să fie pozitivă."):
        account.deposit(-10.0)
    # Verifică că soldul nu s-a modificat
    assert account.balance == 100.0


def test_withdraw_positive_amount_sufficient_funds():
    """
    Test case pentru metoda withdraw cu o sumă pozitivă validă și fonduri suficiente.
    
    Functional Testing:
    - Equivalence Partitioning: Testează partiția validă pentru 'amount' (pozitiv, mai mic sau egal cu soldul).
    - Boundary Value Analysis: Testează o sumă tipică, mult sub sold.
    
    Structural Testing:
    - Statement Coverage: Acoperă instrucțiunile `self.balance -= amount` și `return True`.
    - Branch/Decision Coverage:
        - Acoperă ramura FALSE a deciziei `if amount <= 0:`.
        - Acoperă ramura FALSE a deciziei `if amount > self.balance:`.
    
    Oracle & RIP Model:
    - Reachability: Apelul `account.withdraw(20.0)` este executat pe un cont cu `balance = 100.0`.
    - Infection: Starea `self.balance` se modifică de la `100.0` la `80.0`, și se returnează `True`.
    - Propagation: Se verifică (`assert`) valoarea booleană returnată și soldul intern al contului (`account.balance`).
    
    Avoid Random Testing:
    - S-au folosit sold inițial și sumă de retragere specifice.
    """
    account = BankAccount(100.0)
    withdraw_amount = 20.0
    expected_balance = 80.0

    result = account.withdraw(withdraw_amount)
    
    assert result is True
    assert account.balance == expected_balance

def test_withdraw_exact_balance():
    """
    Test case pentru metoda withdraw, retrăgând exact soldul curent.
    
    Functional Testing:
    - Equivalence Partitioning: Testează partiția validă pentru 'amount' (pozitiv, mai mic sau egal cu soldul).
    - Boundary Value Analysis: Testează limita superioară a partiției valide de retragere (suma == soldul).
    
    Structural Testing:
    - Statement Coverage: Acoperă instrucțiunile `self.balance -= amount` și `return True`.
    - Branch/Decision Coverage:
        - Acoperă ramura FALSE a deciziei `if amount <= 0:`.
        - Acoperă ramura FALSE a deciziei `if amount > self.balance:` (specific cazul `amount == balance`).
    
    Oracle & RIP Model:
    - Reachability: Apelul `account.withdraw(100.0)` este executat pe un cont cu `balance = 100.0`.
    - Infection: Starea `self.balance` se modifică de la `100.0` la `0.0`, și se returnează `True`.
    - Propagation: Se verifică (`assert`) valoarea booleană returnată și soldul intern al contului (`account.balance`).
    
    Avoid Random Testing:
    - S-au folosit sold inițial și valoarea limită precisă `100.0` în mod explicit.
    """
    account = BankAccount(100.0)
    withdraw_amount = 100.0
    expected_balance = 0.0

    result = account.withdraw(withdraw_amount)
    
    assert result is True
    assert account.balance == expected_balance

def test_withdraw_minimum_positive_amount():
    """
    Test case pentru metoda withdraw cu cea mai mică sumă pozitivă posibilă.
    
    Functional Testing:
    - Equivalence Partitioning: Testează partiția validă pentru 'amount' (pozitiv, mai mic sau egal cu soldul).
    - Boundary Value Analysis: Testează limita inferioară a partiției valide de retragere (0 + epsilon).
    
    Structural Testing:
    - Statement Coverage: Acoperă instrucțiunile `self.balance -= amount` și `return True`.
    - Branch/Decision Coverage:
        - Acoperă ramura FALSE a deciziei `if amount <= 0:`.
        - Acoperă ramura FALSE a deciziei `if amount > self.balance:`.
    
    Oracle & RIP Model:
    - Reachability: Apelul `account.withdraw(0.01)` este executat pe un cont cu `balance = 10.0`.
    - Infection: Starea `self.balance` se modifică de la `10.0` la `9.99`, și se returnează `True`.
    - Propagation: Se verifică (`assert`) valoarea booleană returnată și soldul intern al contului (`account.balance`).
    
    Avoid Random Testing:
    - S-au folosit sold inițial și valoarea limită precisă `0.01` în mod explicit.
    """
    account = BankAccount(10.0)
    withdraw_amount = 0.01
    expected_balance = 9.99

    result = account.withdraw(withdraw_amount)
    
    assert result is True
    assert account.balance == expected_balance

def test_withdraw_insufficient_funds():
    """
    Test case pentru metoda withdraw când fondurile sunt insuficiente.
    
    Functional Testing:
    - Equivalence Partitioning: Testează partiția invalidă pentru 'amount' (mai mare decât soldul).
    - Boundary Value Analysis: Testează o sumă imediat peste soldul curent (sold + epsilon).
    
    Structural Testing:
    - Statement Coverage: Acoperă instrucțiunile `if amount > self.balance:` și `return False`.
    - Branch/Decision Coverage:
        - Acoperă ramura FALSE a deciziei `if amount <= 0:`.
        - Acoperă ramura TRUE a deciziei `if amount > self.balance:`.
    
    Oracle & RIP Model:
    - Reachability: Apelul `account.withdraw(100.01)` este executat pe un cont cu `balance = 100.0`.
    - Infection: Se returnează `False`, și `self.balance` rămâne nemodificat.
    - Propagation: Se verifică (`assert`) valoarea booleană returnată (`False`) și că soldul intern al contului (`account.balance`) nu s-a modificat.
    
    Avoid Random Testing:
    - S-au folosit sold inițial și o valoare limită precisă `100.01` în mod explicit.
    """
    account = BankAccount(100.0)
    withdraw_amount = 100.01 
    original_balance = account.balance

    result = account.withdraw(withdraw_amount)
    
    assert result is False
    assert account.balance == original_balance 

def test_withdraw_zero_amount_raises_error():
    """
    Test case pentru metoda withdraw când suma este zero.
    
    Functional Testing:
    - Equivalence Partitioning: Testează partiția invalidă pentru 'amount' (numere non-pozitive).
    - Boundary Value Analysis: Testează valoarea limită '0' pentru intrare invalidă.
    
    Structural Testing:
    - Statement Coverage: Acoperă instrucțiunile `if amount <= 0:` și `raise ValueError(...)`.
    - Branch/Decision Coverage: Acoperă ramura TRUE a deciziei `if amount <= 0:`.
    
    Oracle & RIP Model:
    - Reachability: Apelul `account.withdraw(0)` este executat.
    - Infection: Excepția `ValueError` este declanșată.
    - Propagation: `pytest.raises` verifică tipul și mesajul excepției declanșate. Soldul contului este verificat să nu se fi modificat.
    
    Avoid Random Testing:
    - S-a folosit valoarea limită invalidă exactă `0`.
    """
    account = BankAccount(100.0)
    with pytest.raises(ValueError, match="Suma retrasă trebuie să fie pozitivă."):
        account.withdraw(0)
    # Verifică că soldul nu s-a modificat
    assert account.balance == 100.0

def test_withdraw_negative_amount_raises_error():
    """
    Test case pentru metoda withdraw când suma este negativă.
    
    Functional Testing:
    - Equivalence Partitioning: Testează partiția invalidă pentru 'amount' (numere non-pozitive).
    - Boundary Value Analysis: Testează o valoare negativă.
    
    Structural Testing:
    - Statement Coverage: Acoperă instrucțiunile `if amount <= 0:` și `raise ValueError(...)`.
    - Branch/Decision Coverage: Acoperă ramura TRUE a deciziei `if amount <= 0:`.
    
    Oracle & RIP Model:
    - Reachability: Apelul `account.withdraw(-10.0)` este executat.
    - Infection: Excepția `ValueError` este declanșată.
    - Propagation: `pytest.raises` verifică tipul și mesajul excepției declanșate. Soldul contului este verificat să nu se fi modificat.
    
    Avoid Random Testing:
    - S-a folosit o valoare negativă specifică `-10.0`.
    """
    account = BankAccount(100.0)
    with pytest.raises(ValueError, match="Suma retrasă trebuie să fie pozitivă."):
        account.withdraw(-10.0)
    # Verifică că soldul nu s-a modificat
    assert account.balance == 100.0