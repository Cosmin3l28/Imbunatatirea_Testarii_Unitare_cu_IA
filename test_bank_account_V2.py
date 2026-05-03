import pytest
from bank_account import BankAccount


# --- Teste Existente (Imbunatatite conform RIP) ---

def test_depunere_simpla():
    """
    Imbunatatire: A fost adaugata verificarea valorii returnate de metoda deposit,
    pe langa verificarea soldului contului, conform modelului RIP (Propagation).
    Aceasta asigura ca nu doar starea interna este corecta, ci si output-ul public.
    """
    cont = BankAccount(100)
    # Verificarea valorii returnate (noul sold)
    returned_balance = cont.deposit(50)
    assert returned_balance == 150
    # Verificarea starii interne a obiectului (soldul contului)
    assert cont.balance == 150

def test_retragere_simpla():
    """
    Imbunatatire: Assertiile erau deja bune, verificand atat valoarea returnata (True),
    cat si soldul contului, acoperind Propagation in modelul RIP.
    Acesta testeaza calea de succes a retragerii.
    """
    cont = BankAccount(100)
    succes = cont.withdraw(50)
    assert succes is True
    assert cont.balance == 50

def test_fonduri_insuficiente():
    """
    Imbunatatire: A fost adaugata verificarea ca soldul contului ramane neschimbat
    atunci cand retragerea esueaza, pe langa verificarea valorii returnate (False),
    conform modelului RIP (Propagation). Acest lucru confirma ca tranzactia nu a afectat starea.
    """
    initial_balance = 50
    cont = BankAccount(initial_balance)
    succes = cont.withdraw(100)
    assert succes is False
    # Verificarea ca soldul nu s-a modificat
    assert cont.balance == initial_balance


# --- Teste Noi pentru Acoperirea Ramurilor si Boundary Value Analysis ---

# Teste pentru metoda __init__ (constructor)
def test_initializare_cont_cu_sold_implicit_zero():
    """
    Test nou: Verifica initializarea contului fara a specifica un sold,
    asigurand ca soldul implicit este 0.0. Acopera functionalitatea constructorului
    pentru cazul de valoare implicita.
    """
    cont = BankAccount()
    assert cont.balance == 0.0

def test_initializare_cont_cu_sold_specificat():
    """
    Test nou: Verifica initializarea contului cu un sold specificat,
    asigurand ca soldul este setat corect. Acopera functionalitatea constructorului
    pentru cazul de valoare explicita.
    """
    cont = BankAccount(100.50)
    assert cont.balance == 100.50


# Teste pentru metoda deposit (cu Boundary Value Analysis si Branch Coverage)
def test_depunere_suma_zero_ridica_exceptie():
    """
    Test nou: Acopera ramura de decizie `if amount <= 0` (True) pentru `deposit`
    si cazul de limita (Boundary Value Analysis) `amount = 0`.
    Verifica ca se ridica ValueError cu mesajul corect si ca soldul nu se modifica.
    """
    cont = BankAccount(100)
    with pytest.raises(ValueError, match="Suma depusă trebuie să fie pozitivă."):
        cont.deposit(0)
    # Asiguram ca soldul nu s-a modificat
    assert cont.balance == 100

def test_depunere_suma_negativa_ridica_exceptie():
    """
    Test nou: Acopera ramura de decizie `if amount <= 0` (True) pentru `deposit`
    si cazul de limita (Boundary Value Analysis) `amount < 0`.
    Verifica ca se ridica ValueError cu mesajul corect si ca soldul nu se modifica.
    """
    cont = BankAccount(100)
    with pytest.raises(ValueError, match="Suma depusă trebuie să fie pozitivă."):
        cont.deposit(-50)
    # Asiguram ca soldul nu s-a modificat
    assert cont.balance == 100

def test_depunere_suma_minima_pozitiva_succes():
    """
    Test nou: Acopera ramura de decizie `if amount <= 0` (False) pentru `deposit`
    si cazul de limita (Boundary Value Analysis) `amount` imediat peste 0.
    Verifica functionalitatea corecta pentru cea mai mica suma pozitiva posibila (0.01).
    """
    cont = BankAccount(100)
    returned_balance = cont.deposit(0.01)
    assert returned_balance == 100.01
    assert cont.balance == 100.01


# Teste pentru metoda withdraw (cu Boundary Value Analysis si Branch Coverage)
def test_retragere_suma_zero_ridica_exceptie():
    """
    Test nou: Acopera ramura de decizie `if amount <= 0` (True) pentru prima conditie din `withdraw`
    si cazul de limita (Boundary Value Analysis) `amount = 0`.
    Verifica ca se ridica ValueError cu mesajul corect si ca soldul nu se modifica.
    """
    cont = BankAccount(100)
    with pytest.raises(ValueError, match="Suma retrasă trebuie să fie pozitivă."):
        cont.withdraw(0)
    # Asiguram ca soldul nu s-a modificat
    assert cont.balance == 100

def test_retragere_suma_negativa_ridica_exceptie():
    """
    Test nou: Acopera ramura de decizie `if amount <= 0` (True) pentru prima conditie din `withdraw`
    si cazul de limita (Boundary Value Analysis) `amount < 0`.
    Verifica ca se ridica ValueError cu mesajul corect si ca soldul nu se modifica.
    """
    cont = BankAccount(100)
    with pytest.raises(ValueError, match="Suma retrasă trebuie să fie pozitivă."):
        cont.withdraw(-50)
    # Asiguram ca soldul nu s-a modificat
    assert cont.balance == 100

def test_retragere_suma_minima_pozitiva_succes():
    """
    Test nou: Acopera ramura de decizie `if amount <= 0` (False) si `if amount > self.balance` (False)
    pentru `withdraw`, si cazul de limita (Boundary Value Analysis) `amount` imediat peste 0.
    Verifica functionalitatea corecta pentru cea mai mica suma pozitiva care nu depaseste soldul.
    """
    cont = BankAccount(100)
    succes = cont.withdraw(0.01)
    assert succes is True
    assert cont.balance == 99.99

def test_retragere_suma_exacta_soldului_succes():
    """
    Test nou: Acopera ramura de decizie `if amount > self.balance` (False)
    si cazul de limita (Boundary Value Analysis) `amount = self.balance`.
    Verifica ca retragerea intregului sold este posibila si soldul devine zero.
    """
    cont = BankAccount(100)
    succes = cont.withdraw(100)
    assert succes is True
    assert cont.balance == 0.0

def test_retragere_suma_doar_putin_mai_mare_decat_soldul_esec():
    """
    Test nou: Acopera ramura de decizie `if amount > self.balance` (True)
    si cazul de limita (Boundary Value Analysis) `amount` imediat peste `self.balance`.
    Verifica ca retragerea esueaza si soldul ramane neschimbat.
    """
    initial_balance = 50
    cont = BankAccount(initial_balance)
    succes = cont.withdraw(50.01)  # Suma doar putin mai mare decat soldul
    assert succes is False
    assert cont.balance == initial_balance  # Soldul trebuie sa ramana neschimbat