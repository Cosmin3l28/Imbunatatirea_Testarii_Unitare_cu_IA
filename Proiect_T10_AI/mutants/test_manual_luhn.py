import pytest
from luhn_algo import luhn_digit, is_luhn_valid, generate, check

def test_luhn_digit():
    assert luhn_digit(3) == 6
    assert luhn_digit(6) == 3 # 12 -> 12-9 = 3

def test_is_luhn_valid_amex():
    valid_card = "376688790943011"
    assert is_luhn_valid(valid_card) == True

def test_generate_and_check():
    prefix = "37"
    length = 15
    generated_number = generate(prefix, length)

    assert check(prefix, length, generated_number) == True

def test_check_invalid_length():

    assert check("37", 15, "371234") == False

def test_check_invalid_prefix():

    assert check("37", 15, "401234567890123") == False