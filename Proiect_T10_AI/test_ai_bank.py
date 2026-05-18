import pytest
from bank_account import BankAccount


# Regula 1: Pastreaza testele mele existente, dar imbunatateste-le asertiunile conform modelului RIP.

def test_depunere_simpla():
    """
    Imbunatatire RIP:
    - Adaugat asertiune pentru valoarea returnata de metoda deposit, care ar trebui sa fie noul sold.
    """
    cont = BankAccount(100)
    new_balance = cont.deposit(50)
    assert cont.balance == 150, "Soldul contului ar trebui sa fie 150 dupa depunere."
    assert new_balance == 150, "Metoda deposit ar trebui sa returneze noul sold."


def test_retragere_simpla():
    """
    Imbunatatire RIP:
    - Asertiunile existente sunt precise si acopera atat valoarea returnata cat si starea interna.
    """
    cont = BankAccount(100)
    succes = cont.withdraw(50)
    assert succes is True, "Retragerea ar trebui sa fie considerata un succes."
    assert cont.balance == 50, "Soldul contului ar trebui sa fie 50 dupa retragere."


def test_fonduri_insuficiente():
    """
    Imbunatatire RIP:
    - Adaugat asertiune pentru a verifica ca soldul contului ramane neschimbat in cazul unei retrageri esuate.
    """
    initial_balance = 50
    cont = BankAccount(initial_balance)
    succes = cont.withdraw(100)
    assert succes is False, "Retragerea ar trebui sa esueze din cauza fondurilor insuficiente."
    assert cont.balance == initial_balance, "Soldul contului nu ar trebui sa se modifice in cazul unei retrageri esuate."


# Regula 2, 3, 4: Adauga teste noi pentru toate ramurile de decizie lipsa (Branch Coverage),
# aplica Boundary Value Analysis si asigura acoperire la nivel de instructiune, decizie si conditie.

# Teste noi pentru metoda __init__ (critic: scor 2.5)
def test_initializare_fara_parametru():
    """
    Nou test:
    - Verifica initializarea contului cu soldul implicit (0.0), acoperind ramura implicita a constructorului.
    """
    cont = BankAccount()
    assert cont.balance == 0.0, "Soldul initial ar trebui sa fie 0.0 daca nu este specificat."


# Teste noi pentru metoda deposit (critic: scor 8.0, ciclomatic≈2, ramuri=1, raise=1)
def test_depunere_cu_suma_zero():
    """
    Nou test (Branch Coverage & Boundary Value Analysis):
    - Acopera ramura de decizie `if amount <= 0:` (True) si verifica ridicarea exceptiei `ValueError`.
    - Aplica BVA pentru limita `amount = 0`.
    """
    cont = BankAccount(100)
    with pytest.raises(ValueError, match="Suma depusă trebuie să fie pozitivă."):
        cont.deposit(0)
    assert cont.balance == 100, "Soldul nu ar trebui sa se schimbe dupa o depunere de 0 care esueaza."


def test_depunere_cu_suma_negativa():
    """
    Nou test (Branch Coverage & Boundary Value Analysis):
    - Acopera ramura de decizie `if amount <= 0:` (True) si verifica ridicarea exceptiei `ValueError`.
    - Aplica BVA pentru limita `amount = -1`.
    """
    cont = BankAccount(100)
    with pytest.raises(ValueError, match="Suma depusă trebuie să fie pozitivă."):
        cont.deposit(-10)
    assert cont.balance == 100, "Soldul nu ar trebui sa se schimbe dupa o depunere negativa care esueaza."


def test_depunere_limita_inferioara_valida():
    """
    Nou test (Boundary Value Analysis):
    - Verifica o depunere cu cea mai mica suma pozitiva posibila (just peste 0).
    - Asigura acoperire de instructiuni si decizii pentru calea valida.
    """
    cont = BankAccount(0)
    new_balance = cont.deposit(0.01)
    assert cont.balance == 0.01, "Soldul ar trebui sa fie 0.01 dupa depunerea minima valida."
    assert new_balance == 0.01, "Metoda deposit ar trebui sa returneze noul sold 0.01."


def test_depunere_limita_superioara_valida():
    """
    Nou test (Boundary Value Analysis):
    - Verifica o depunere cu o suma foarte mare, testand capabilitatea sistemului cu valori mari.
    - Asigura acoperire de instructiuni si decizii pentru calea valida.
    """
    cont = BankAccount(0)
    new_balance = cont.deposit(1_000_000_000.00)
    assert cont.balance == 1_000_000_000.00, "Soldul ar trebui sa reflecte depunerea unei sume mari."
    assert new_balance == 1_000_000_000.00, "Metoda deposit ar trebui sa returneze noul sold mare."


# Teste noi pentru metoda withdraw (critic: scor 12.3, ciclomatic≈3, ramuri=2, raise=1)
def test_retragere_cu_suma_zero():
    """
    Nou test (Branch Coverage & Boundary Value Analysis):
    - Acopera ramura de decizie `if amount <= 0:` (True) si verifica ridicarea exceptiei `ValueError`.
    - Aplica BVA pentru limita `amount = 0`.
    """
    cont = BankAccount(100)
    with pytest.raises(ValueError, match="Suma retrasă trebuie să fie pozitivă."):
        cont.withdraw(0)
    assert cont.balance == 100, "Soldul nu ar trebui sa se schimbe dupa o retragere de 0 care esueaza."


def test_retragere_cu_suma_negativa():
    """
    Nou test (Branch Coverage & Boundary Value Analysis):
    - Acopera ramura de decizie `if amount <= 0:` (True) si verifica ridicarea exceptiei `ValueError`.
    - Aplica BVA pentru limita `amount = -1`.
    """
    cont = BankAccount(100)
    with pytest.raises(ValueError, match="Suma retrasă trebuie să fie pozitivă."):
        cont.withdraw(-10)
    assert cont.balance == 100, "Soldul nu ar trebui sa se schimbe dupa o retragere negativa care esueaza."


def test_retragere_suma_exact_egala_cu_soldul():
    """
    Nou test (Branch Coverage & Boundary Value Analysis):
    - Acopera calea de succes unde soldul devine 0.
    - Aplica BVA pentru limita `amount = self.balance`.
    - Asigura acoperire de instructiuni si decizii pentru calea valida.
    """
    cont = BankAccount(100)
    succes = cont.withdraw(100)
    assert succes is True, "Retragerea sumei exact egale cu soldul ar trebui sa fie un succes."
    assert cont.balance == 0, "Soldul ar trebui sa fie 0 dupa retragerea intregii sume."


def test_retragere_fonduri_insuficiente_exact_peste_sold():
    """
    Nou test (Branch Coverage & Boundary Value Analysis):
    - Acopera ramura de decizie `if amount > self.balance:` (True).
    - Aplica BVA pentru limita `amount = self.balance + 0.01`.
    - Asigura acoperire de instructiuni si decizii pentru calea de esec.
    """
    initial_balance = 100
    cont = BankAccount(initial_balance)
    succes = cont.withdraw(100.01)
    assert succes is False, "Retragerea unei sume putin peste sold ar trebui sa esueze."
    assert cont.balance == initial_balance, "Soldul nu ar trebui sa se schimbe in cazul unei retrageri esuate."


def test_retragere_limita_inferioara_valida():
    """
    Nou test (Boundary Value Analysis):
    - Verifica o retragere cu cea mai mica suma pozitiva posibila (just peste 0).
    - Asigura acoperire de instructiuni si decizii pentru calea valida.
    """
    cont = BankAccount(10)
    succes = cont.withdraw(0.01)
    assert succes is True, "Retragerea minima valida ar trebui sa fie un succes."
    assert cont.balance == 9.99, "Soldul ar trebui sa fie 9.99 dupa retragerea minima valida."