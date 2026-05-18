import pytest
from bank_account import BankAccount


def test_depunere_simpla():
    cont = BankAccount(100)
    cont.deposit(50)
    assert cont.balance == 150

def test_retragere_simpla():
    cont = BankAccount(100)
    succes = cont.withdraw(50)
    assert succes is True
    assert cont.balance == 50

def test_fonduri_insuficiente():
    cont = BankAccount(50)
    succes = cont.withdraw(100)
    assert succes is False