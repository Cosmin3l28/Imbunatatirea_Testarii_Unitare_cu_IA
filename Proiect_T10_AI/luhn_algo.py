import random

def luhn_digit(n):
    n = 2 * n
    if n > 9:
        return n - 9
    else:
        return n

def luhn_checksum(n):
    l = len(n)
    total_sum = 0
    if l % 2 == 0:
        for i in range(l):
            if (i+1) % 2 == 0:
                total_sum += int(n[i])
            else:
                total_sum += luhn_digit(int(n[i]))
    else:
        for i in range(l):
            if (i+1) % 2 == 0:
                total_sum += luhn_digit(int(n[i]))
            else:
                total_sum += int(n[i])
    return total_sum % 10

def is_luhn_valid(n):
    return luhn_checksum(n) == 0

def generate(pref, l):
    nrand = l - len(pref) - 1
    assert nrand > 0, "nrand > 0"
    n = pref
    for i in range(nrand):
        n += str(random.randrange(10))
    n += "0"
    check = luhn_checksum(n)
    if check != 0:
        check = 10 - check
    n = n[:-1] + str(check)
    return n

def check(pref, l, num):
    if len(num) != l:
        return False
    preflen = len(pref)
    if num[:preflen] != pref:
        return False
    return is_luhn_valid(num)