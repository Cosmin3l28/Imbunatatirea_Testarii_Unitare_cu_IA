import pytest
import random
from luhn_algo import luhn_digit, luhn_checksum, is_luhn_valid, generate, check

# --- Teste existente (îmbunătățite cu aserțiuni conform modelului RIP) ---

def test_luhn_digit():
    """
    Îmbunătățire RIP: Adăugate comentarii pentru a explica atingerea codului, infecția și propagarea.
    Acoperă ramurile 'n > 9' (Adevărat și Fals).
    """
    # Atingere (Reachability): Intrările (3, 6, 0, 9) ajung la funcția luhn_digit.
    # Infecție (Infection):
    # Pentru 3: n=3, 2*n=6. Condiția n>9 este Falsă.
    # Pentru 6: n=6, 2*n=12. Condiția n>9 este Adevărată.
    # Pentru 0: n=0, 2*n=0. Condiția n>9 este Falsă.
    # Pentru 9: n=9, 2*n=18. Condiția n>9 este Adevărată.
    # Propagare (Propagation): Funcția returnează valorile corecte (6, 3, 0, 9).
    assert luhn_digit(3) == 6 # Cazul: n <= 9 (ramura else)
    assert luhn_digit(6) == 3 # Cazul: n > 9 (ramura if)
    # BVA: Cifre la limite (0 și 9)
    assert luhn_digit(0) == 0
    assert luhn_digit(9) == 9

def test_is_luhn_valid_amex():
    """
    Îmbunătățire RIP: Adăugate comentarii.
    """
    # Atingere: String-ul 'valid_card' ajunge la is_luhn_valid și luhn_checksum.
    # Infecție: Un număr Luhn format corect ar trebui să rezulte într-o sumă de control 0.
    # Propagare: Aserțiunea verifică că rezultatul lui luhn_checksum este într-adevăr 0 (True).
    valid_card = "376688790943011"
    assert is_luhn_valid(valid_card) == True

def test_generate_and_check():
    """
    Îmbunătățire RIP: Adăugate comentarii și aserțiuni suplimentare pentru propagare.
    """
    # Atingere: 'prefix' și 'length' ajung la 'generate', apoi 'generated_number' ajunge la 'check'.
    # Infecție: 'generate' creează un număr care ar trebui să fie intrinsec valid Luhn,
    # și să corespundă prefixului și lungimii. 'check' verifică aceste proprietăți.
    # Propagare: Aserțiunea verifică că 'check' returnează True, confirmând proprietățile.
    prefix = "37"
    length = 15
    generated_number = generate(prefix, length)

    assert check(prefix, length, generated_number) == True
    # Aserțiuni suplimentare de propagare pentru a verifica structura numărului generat.
    assert generated_number.startswith(prefix)
    assert len(generated_number) == length

def test_check_invalid_length():
    """
    Îmbunătățire RIP: Adăugate comentarii.
    Acoperă ramura `len(num) != l` (Adevărat).
    """
    # Atingere: Intrările ajung la 'check', vizând ramura `len(num) != l`.
    # Infecție: 'num' are o lungime (6) diferită de 'l' (15) așteptată.
    # Propagare: Funcția returnează corect False, verificând detectarea nepotrivirii lungimii.
    assert check("37", 15, "371234") == False

def test_check_invalid_prefix():
    """
    Îmbunătățire RIP: Adăugate comentarii.
    Acoperă ramura `num[:preflen] != pref` (Adevărat).
    """
    # Atingere: Intrările ajung la 'check', vizând ramura `num[:preflen] != pref`.
    # Infecție: 'num' are un prefix ("40") diferit de 'pref' ("37") așteptat.
    # Propagare: Funcția returnează corect False, verificând detectarea nepotrivirii prefixului.
    assert check("37", 15, "401234567890123") == False

# --- Teste noi (Acoperire Ramuri, BVA, Acoperire Condiții) ---

# Secțiunea pentru luhn_checksum (prioritate maximă)
# Acoperă L13 [decizie] if (l % 2 == 0)
# Acoperă L15 [decizie] if ((i + 1) % 2 == 0) (în blocul de lungime pară)
# Acoperă L21 [decizie] if ((i + 1) % 2 == 0) (în blocul de lungime impară)

def test_luhn_checksum_even_length():
    """
    Test nou pentru luhn_checksum: Acoperă ramura 'l % 2 == 0' (Adevărat).
    Asigură că pentru numere cu lungime pară, logica corectă de dublare a cifrelor
    este aplicată pe baza poziției (L15). Acoperă ambele căi pentru L15.
    Exemplu: "1234" (lungime=4, pară)
    i=0 (cifra 1, poziție impară): luhn_digit(1) -> 2
    i=1 (cifra 2, poziție pară): int(2) -> 2
    i=2 (cifra 3, poziție impară): luhn_digit(3) -> 6
    i=3 (cifra 4, poziție pară): int(4) -> 4
    Suma totală = 2 + 2 + 6 + 4 = 14. Suma de control = 14 % 10 = 4.
    """
    assert luhn_checksum("1234") == 4
    # BVA: Cea mai mică lungime pară
    assert luhn_checksum("79") == 4 # 7*2-9 + 9 = 5 + 9 = 14. Suma de control = 4.

def test_luhn_checksum_odd_length():
    """
    Test nou pentru luhn_checksum: Acoperă ramura 'l % 2 == 0' (Fals).
    Asigură că pentru numere cu lungime impară, logica corectă de dublare a cifrelor
    este aplicată pe baza poziției (L21). Acoperă ambele căi pentru L21.
    Exemplu: "123" (lungime=3, impară)
    i=0 (cifra 1, poziție impară): int(1) -> 1
    i=1 (cifra 2, poziție pară): luhn_digit(2) -> 4
    i=2 (cifra 3, poziție impară): int(3) -> 3
    Suma totală = 1 + 4 + 3 = 8. Suma de control = 8 % 10 = 8.
    """
    assert luhn_checksum("123") == 8
    # BVA: Cea mai mică lungime impară (care are sens pentru un număr Luhn, > 1)
    assert luhn_checksum("1") == 1 # Len=1, impară. i=0: int(1) -> 1. Suma = 1. Suma de control = 1.

def test_luhn_checksum_with_nines_and_zeros():
    """
    Test nou pentru luhn_checksum: Asigură tratarea corectă a cifrelor 0 și 9,
    mai ales când sunt dublate și potențial reduse cu 9.
    Exemplu: "891" (lungime=3, impară)
    i=0 (cifra 8, poziție impară): int(8) -> 8
    i=1 (cifra 9, poziție pară): luhn_digit(9) -> 18-9=9
    i=2 (cifra 1, poziție impară): int(1) -> 1
    Suma totală = 8 + 9 + 1 = 18. Suma de control = 18 % 10 = 8.
    """
    assert luhn_checksum("891") == 8
    # Exemplu cu zero: "010" (lungime=3, impară)
    # i=0 (cifra 0, poziție impară): int(0) -> 0
    # i=1 (cifra 1, poziție pară): luhn_digit(1) -> 2
    # i=2 (cifra 0, poziție impară): int(0) -> 0
    # Suma totală = 0 + 2 + 0 = 2. Suma de control = 2.
    assert luhn_checksum("010") == 2

def test_luhn_checksum_long_number_bva():
    """
    Test nou pentru luhn_checksum: Analiză a valorilor de frontieră pentru o lungime tipică mai mare a cardului.
    Asigură performanța și corectitudinea pentru dimensiuni de intrare mai realiste.
    """
    long_valid_card = "49927398716" # Un număr Luhn valid de test comun
    assert luhn_checksum(long_valid_card) == 0

# Secțiunea pentru is_luhn_valid
def test_is_luhn_valid_invalid_card():
    """
    Test nou pentru is_luhn_valid: Asigură că funcția identifică corect numerele Luhn invalide.
    Acoperă cazul în care luhn_checksum(n) != 0.
    """
    invalid_card = "376688790943012" # Ultima cifră schimbată de la 1 la 2, făcându-l invalid
    # Aserțiune suplimentară pentru a verifica că numărul este într-adevăr invalid
    assert is_luhn_valid(invalid_card) == False

# Secțiunea pentru generate (prioritate înaltă)
# Acoperă 'assert nrand > 0' (ramura implicită de decizie/condiție)
# Adresează L38 [decizie] if (check != 0)

def test_generate_assert_nrand_negative():
    """
    Test nou pentru generate: Acoperă punctul de decizie implicit 'assert nrand > 0'.
    Testează scenariul în care 'nrand' ar fi negativ, ceea ce ar trebui să declanșeze o AssertionError.
    Aici, l=3, len(pref)=3 => nrand = 3 - 3 - 1 = -1.
    """
    with pytest.raises(AssertionError) as excinfo:
        generate("123", 3)
    assert "nrand > 0" in str(excinfo.value) # Verifică propagarea mesajului specific de aserțiune

def test_generate_assert_nrand_zero():
    """
    Test nou pentru generate: Acoperă punctul de decizie implicit 'assert nrand > 0'.
    Testează scenariul în care 'nrand' ar fi zero, ceea ce ar trebui să declanșeze o AssertionError.
    Aici, l=4, len(pref)=3 => nrand = 4 - 3 - 1 = 0.
    """
    with pytest.raises(AssertionError) as excinfo:
        generate("123", 4)
    assert "nrand > 0" in str(excinfo.value)

# Notă privind acoperirea ramurii 'if check != 0' (Fals) în funcția generate:
# Acoperirea căii în care `luhn_checksum(n)` returnează 0 *înainte* de corecția finală
# (adică, `check == 0` este adevărat inițial) este extrem de dificilă de realizat deterministic
# fără a simula funcția `random.randrange`. Deoarece specificația cere să nu modificăm codul sursă
# și să nu adăugăm alte texte decât codul final, nu putem folosi `unittest.mock` aici.
# Testul existent `test_generate_and_check` acoperă implicit cazul `check != 0` (Adevărat),
# deoarece este statistic improbabil ca un număr generat aleatoriu să fie deja valid Luhn înainte de corecție.
# Ne bazăm pe faptul că funcția `generate` produce întotdeauna un număr valid Luhn la final.

# Analiza Valorilor de Frontieră (BVA) pentru generate:
def test_generate_minimum_length_bva():
    """
    Test nou pentru generate: Analiză a valorilor de frontieră pentru lungimea minimă validă.
    Asigură că generate funcționează pentru cel mai mic 'l' posibil unde nrand > 0,
    ceea ce înseamnă l = len(pref) + 2.
    Aici, pref="1", l=3. nrand = 3 - 1 - 1 = 1.
    """
    prefix = "1"
    length = 3
    generated_number = generate(prefix, length)
    assert len(generated_number) == length
    assert generated_number.startswith(prefix)
    assert is_luhn_valid(generated_number) == True

def test_generate_empty_prefix_bva():
    """
    Test nou pentru generate: Analiză a valorilor de frontieră pentru un prefix gol.
    Asigură că funcția gestionează corect un prefix gol.
    """
    prefix = ""
    length = 5
    generated_number = generate(prefix, length)
    assert len(generated_number) == length
    assert generated_number.startswith(prefix) # Adevărat și pentru prefix gol
    assert is_luhn_valid(generated_number) == True

def test_generate_long_number_bva():
    """
    Test nou pentru generate: Analiză a valorilor de frontieră pentru un număr mai lung,
    similar cu lungimile tipice ale cardurilor de credit.
    """
    prefix = "4" # Un prefix comun pentru carduri
    length = 19 # Lungimea maximă tipică a unui card
    generated_number = generate(prefix, length)
    assert len(generated_number) == length
    assert generated_number.startswith(prefix)
    assert is_luhn_valid(generated_number) == True

# Secțiunea pentru check (prioritate înaltă)
# L44 [decizie] if (len(num) != l) - Acoperită de test_check_invalid_length (Adevărat)
# L47 [decizie] if (num[:preflen] != pref) - Acoperită de test_check_invalid_prefix (Adevărat)
# Ambele condiții Fals sunt acoperite de test_generate_and_check.

def test_check_valid_prefix_length_invalid_luhn():
    """
    Test nou pentru check: Acoperă scenariul în care prefixul și lungimea sunt corecte,
    dar numărul în sine nu este valid Luhn. Aceasta asigură că linia finală
    'return is_luhn_valid(num)' (și rezultatul său Fals) este pe deplin exercitată.
    """
    invalid_luhn_num = "371234567890123" # Un număr de 15 cifre cu prefix "37" care nu este valid Luhn
    # Verificăm independent că numărul nu este valid Luhn
    assert is_luhn_valid(invalid_luhn_num) == False
    # Verificăm că funcția `check` returnează False pentru acest număr
    assert check("37", 15, invalid_luhn_num) == False