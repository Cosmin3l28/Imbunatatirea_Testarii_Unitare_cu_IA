import pytest
from bank_account import BankAccount


# --- Teste existente (îmbunătățite conform modelului RIP) ---

def test_depunere_simpla():
    """
    Îmbunătățire (RIP):
    - Reachability: Contul este creat cu o balanță inițială (verificată).
    - Infection: Se verifică dacă balanța contului s-a modificat conform așteptărilor după depunere.
    - Propagation: Se verifică dacă valoarea returnată de metoda 'deposit' reflectă noua balanță,
      confirmând propagarea corectă a stării.
    Acoperă: O depunere pozitivă validă.
    """
    initial_balance = 100
    deposit_amount = 50
    cont = BankAccount(initial_balance)
    assert cont.balance == initial_balance  # RIP: Starea inițială este corectă

    returned_balance = cont.deposit(deposit_amount)
    assert cont.balance == initial_balance + deposit_amount  # RIP: Balanța este infectată și corectă
    assert returned_balance == initial_balance + deposit_amount  # RIP: Valoarea returnată propagă corect starea


def test_retragere_simpla():
    """
    Îmbunătățire (RIP):
    - Reachability: Contul este creat cu o balanță inițială (verificată).
    - Infection: Se verifică dacă balanța contului s-a modificat conform așteptărilor după retragere.
    - Propagation: Se verifică dacă valoarea returnată de metodă (True pentru succes) reflectă corect
      rezultatul operației.
    Acoperă: O retragere pozitivă validă, cu fonduri suficiente.
    """
    initial_balance = 100
    withdraw_amount = 50
    cont = BankAccount(initial_balance)
    assert cont.balance == initial_balance  # RIP: Starea inițială este corectă

    succes = cont.withdraw(withdraw_amount)
    assert succes is True  # RIP: Valoarea returnată propagă succesul
    assert cont.balance == initial_balance - withdraw_amount  # RIP: Balanța este infectată și corectă


def test_fonduri_insuficiente():
    """
    Îmbunătățire (RIP):
    - Reachability: Contul este creat cu o balanță inițială (verificată).
    - Infection: Se verifică că balanța contului *nu* s-a modificat, ceea ce este comportamentul corect
      într-un scenariu de eșec (fără infecție a balanței).
    - Propagation: Se verifică dacă valoarea returnată de metodă (False pentru eșec) reflectă corect
      rezultatul operației.
    Acoperă: O retragere cu fonduri insuficiente.
    """
    initial_balance = 50
    withdraw_amount = 100
    cont = BankAccount(initial_balance)
    assert cont.balance == initial_balance  # RIP: Starea inițială este corectă

    succes = cont.withdraw(withdraw_amount)
    assert succes is False  # RIP: Valoarea returnată propagă eșecul
    assert cont.balance == initial_balance  # RIP: Balanța nu a fost infectată (a rămas neschimbată)


# --- Teste noi pentru Branch Coverage și Boundary Value Analysis ---

def test_deposit_zero_amount_raises_error():
    """
    Test nou pentru acoperirea ramurii de decizie 'if amount <= 0' din metoda 'deposit'.
    Acest caz limite (Boundary Value Analysis) verifică când 'amount' este exact 0.
    Asigură că se ridică excepția 'ValueError' specificată și că balanța contului
    nu este modificată (demonstrând că nu există infecție în cazul unei erori).
    """
    cont = BankAccount(100)
    initial_balance = cont.balance
    with pytest.raises(ValueError) as excinfo:
        cont.deposit(0)
    assert "Suma depusă trebuie să fie pozitivă." in str(excinfo.value)
    assert cont.balance == initial_balance  # RIP: Balanța nu a fost infectată


def test_deposit_negative_amount_raises_error():
    """
    Test nou pentru acoperirea ramurii de decizie 'if amount <= 0' din metoda 'deposit'.
    Acest caz limite (Boundary Value Analysis) verifică când 'amount' este negativ (-1).
    Asigură că se ridică excepția 'ValueError' specificată și că balanța contului
    nu este modificată.
    """
    cont = BankAccount(100)
    initial_balance = cont.balance
    with pytest.raises(ValueError) as excinfo:
        cont.deposit(-1)
    assert "Suma depusă trebuie să fie pozitivă." in str(excinfo.value)
    assert cont.balance == initial_balance  # RIP: Balanța nu a fost infectată


def test_withdraw_zero_amount_raises_error():
    """
    Test nou pentru acoperirea ramurii de decizie 'if amount <= 0' din metoda 'withdraw'.
    Acest caz limite (Boundary Value Analysis) verifică când 'amount' este exact 0.
    Asigură că se ridică excepția 'ValueError' specificată și că balanța contului
    nu este modificată.
    """
    cont = BankAccount(100)
    initial_balance = cont.balance
    with pytest.raises(ValueError) as excinfo:
        cont.withdraw(0)
    assert "Suma retrasă trebuie să fie pozitivă." in str(excinfo.value)
    assert cont.balance == initial_balance  # RIP: Balanța nu a fost infectată


def test_withdraw_negative_amount_raises_error():
    """
    Test nou pentru acoperirea ramurii de decizie 'if amount <= 0' din metoda 'withdraw'.
    Acest caz limite (Boundary Value Analysis) verifică când 'amount' este negativ (-1).
    Asigură că se ridică excepția 'ValueError' specificată și că balanța contului
    nu este modificată.
    """
    cont = BankAccount(100)
    initial_balance = cont.balance
    with pytest.raises(ValueError) as excinfo:
        cont.withdraw(-1)
    assert "Suma retrasă trebuie să fie pozitivă." in str(excinfo.value)
    assert cont.balance == initial_balance  # RIP: Balanța nu a fost infectată


def test_withdraw_exact_balance_boundary():
    """
    Test nou pentru acoperirea cazului limite (Boundary Value Analysis) în metoda 'withdraw',
    când suma retrasă este exact egală cu balanța contului.
    Acest test asigură că ramura 'if amount > self.balance' este FALSĂ și că retragerea
    este procesată cu succes, lăsând balanța la 0.0.
    """
    initial_balance = 100.0
    cont = BankAccount(initial_balance)
    assert cont.balance == initial_balance  # RIP: Starea inițială este corectă

    succes = cont.withdraw(initial_balance)
    assert succes is True  # RIP: Valoarea returnată propagă succesul
    assert cont.balance == 0.0  # RIP: Balanța este infectată corect (devine zero)


def test_initial_balance_default():
    """
    Test nou pentru a verifica comportamentul constructorului __init__ fără argumente.
    Asigură că balanța implicită este 0.0, conform specificațiilor.
    Acoperă: Constructorul cu valoarea implicită.
    """
    cont = BankAccount()
    assert cont.balance == 0.0


def test_initial_balance_zero():
    """
    Test nou pentru a verifica constructorul __init__ cu o balanță inițială de 0.0.
    Acesta este un caz limită (Boundary Value Analysis) pentru parametrul `balance`.
    Acoperă: Constructorul cu o balanță zero explicită.
    """
    cont = BankAccount(0.0)
    assert cont.balance == 0.0


def test_initial_balance_negative():
    """
    Test nou pentru a verifica constructorul __init__ cu o balanță inițială negativă.
    Deși logica de afaceri ar putea interzice acest lucru, codul permite inițializarea
    cu valori negative. Acesta este un caz limită (Boundary Value Analysis) pentru
    parametrul `balance` pentru a documenta comportamentul actual.
    Acoperă: Constructorul cu o balanță negativă.
    """
    cont = BankAccount(-100.0)
    assert cont.balance == -100.0