import pytest
import random
from luhn_algo import luhn_digit, is_luhn_valid, luhn_checksum, generate, check

# --- Original Tests - Improved and Extended (RIP Model, Branch Coverage) ---

# Comment: Aceste teste au fost îmbunătățite pentru a urma modelul RIP (Reachability, Infection, Propagation)
# prin a face aserțiunile mai specifice (e.g., verificarea valorilor exacte ale sumei de control)
# și prin adăugarea de condiții limită sau scenarii noi pentru a acoperi mai multe ramuri de cod.

def test_luhn_digit():
    """
    Comment: Testul original pentru luhn_digit a fost îmbunătățit prin adăugarea
    de teste cu valori de graniță pentru intrarea 'n' în jurul pragului 9/2=4.5.
    Acest lucru asigură că ambele ramuri ale `if n > 9` sunt testate în profunzime
    și că situațiile limită (cum ar fi n=5 unde 2*n=10) sunt gestionate corect.
    """
    # Aserțiuni originale
    assert luhn_digit(3) == 6, "RIP: luhn_digit(3) ar trebui să fie 6 (2*3=6, calea n<=9)"
    assert luhn_digit(6) == 3, "RIP: luhn_digit(6) ar trebui să fie 3 (2*6=12, calea n>9, 12-9=3)"

    # Aserțiuni noi pentru analiza valorilor de graniță (în jurul pragului n=4.5 pentru 2*n > 9)
    assert luhn_digit(0) == 0, "RIP: luhn_digit(0) ar trebui să fie 0 (cea mai mică intrare, calea n<=9)"
    assert luhn_digit(4) == 8, "RIP: luhn_digit(4) ar trebui să fie 8 (2*4=8, calea n<=9, imediat sub prag)"
    assert luhn_digit(5) == 1, "RIP: luhn_digit(5) ar trebui să fie 1 (2*5=10, calea n>9, imediat peste prag, 10-9=1)"
    assert luhn_digit(9) == 9, "RIP: luhn_digit(9) ar trebui să fie 9 (cea mai mare cifră unică, 2*9=18, calea n>9, 18-9=9)"

def test_luhn_checksum_odd_length():
    """
    Comment: Acest test acoperă logica `luhn_checksum` pentru numere de lungime impară (`l % 2 != 0`).
    Utilizează un număr de card Amex valid cunoscut pentru a verifica dacă suma de control este 0.
    Acest lucru acoperă explicit ramura L13 `if (l % 2 == 0)` (blocul `else` este executat) din `luhn_checksum`.
    De asemenea, acoperă sub-ramurile L21 `if ((i + 1) % 2 == 0)` (atât cazul adevărat, cât și cel fals în buclă).
    """
    valid_card_amex = "376688790943011" # Lungime 15 (impară)
    assert luhn_checksum(valid_card_amex) == 0, "RIP: Suma de control pentru un card Amex valid ar trebui să fie 0"

def test_luhn_checksum_even_length():
    """
    Comment: Test nou pentru logica `luhn_checksum` pentru numere de lungime pară (`l % 2 == 0`).
    Acest test acoperă explicit ramura L13 `if (l % 2 == 0)` (blocul `if` este executat) din `luhn_checksum`.
    De asemenea, acoperă sub-ramurile L15 `if ((i + 1) % 2 == 0)` (atât cazul adevărat, cât și cel fals în buclă).
    Utilizează un număr de card valid personalizat (construit pentru a se conforma variantei Luhn din cod)
    pentru a asigura o acoperire completă a ramurilor.
    """
    # Un număr de 16 cifre a cărui sumă Luhn este 0 conform logicii implementate (cifrele de pe poziții impare de la stânga sunt dublate)
    # Exemplu: "1234567890123452"
    # Cifre dublate (luhn_digit): 1->2, 3->6, 5->1, 7->5, 9->9, 1->2, 3->6, 5->1
    # Cifre nedublate (int): 2, 4, 6, 8, 0, 2, 4, 2
    # Suma: (2+6+1+5+9+2+6+1) + (2+4+6+8+0+2+4+2) = 32 + 28 = 60
    # 60 % 10 = 0.
    valid_card_custom_even = "1234567890123452"
    assert luhn_checksum(valid_card_custom_even) == 0, \
        "RIP: Suma de control pentru un card personalizat valid de lungime pară ar trebui să fie 0"

    # Testează un număr invalid de lungime pară
    invalid_card_even = "1234567890123453" # Ultima cifră schimbată de la 2 la 3
    assert luhn_checksum(invalid_card_even) != 0, \
        "RIP: Suma de control pentru un card personalizat invalid de lungime pară nu ar trebui să fie 0"

def test_is_luhn_valid_odd_length():
    """
    Comment: Testează `is_luhn_valid` cu un număr de lungime impară.
    Refolosește cazul Amex existent, afirmând rezultatul specific pentru claritate.
    """
    valid_card_amex = "376688790943011"
    assert is_luhn_valid(valid_card_amex) is True, "RIP: Un card Amex valid ar trebui să returneze True"

def test_is_luhn_valid_even_length():
    """
    Comment: Test nou pentru `is_luhn_valid` cu un număr de lungime pară.
    Utilizează cardul personalizat valid de lungime pară creat pentru `luhn_checksum`.
    """
    valid_card_custom_even = "1234567890123452"
    assert is_luhn_valid(valid_card_custom_even) is True, \
        "RIP: Un card personalizat valid de lungime pară ar trebui să returneze True"

def test_is_luhn_valid_invalid_number():
    """
    Comment: Test nou pentru `is_luhn_valid` pentru a se asigura că identifică corect numerele invalide.
    Acest lucru testează implicit și cazul în care `luhn_checksum` returnează o valoare diferită de zero.
    Acoperă calea inversă a unui apel `is_luhn_valid` reușit.
    """
    invalid_card = "4012345678901234" # Un număr cunoscut ca fiind invalid
    assert is_luhn_valid(invalid_card) is False, "RIP: Un card invalid ar trebui să returneze False"

def test_is_luhn_valid_single_digit():
    """
    Comment: Test de graniță pentru `is_luhn_valid` cu un număr dintr-o singură cifră.
    Asigură că numerele foarte scurte sunt gestionate corect de `luhn_checksum`.
    """
    assert is_luhn_valid("0") is True, "RIP: Cifra unică '0' ar trebui să fie validă Luhn"
    assert is_luhn_valid("1") is False, "RIP: Cifra unică '1' nu ar trebui să fie validă Luhn (suma de control 1)"
    assert is_luhn_valid("9") is False, "RIP: Cifra unică '9' nu ar trebui să fie validă Luhn (suma de control 9)"

def test_generate_and_check():
    """
    Comment: Test original pentru integrarea `generate` și `check`.
    Îmbunătățit prin adăugarea de verificări specifice pentru lungimea și prefixul numărului generat,
    și prin testarea cu un prefix gol pentru analiza de graniță.
    Acest lucru acoperă căile de succes ale ambelor funcții `generate` și `check`.
    """
    prefix = "37"
    length = 15
    generated_number = generate(prefix, length)

    # RIP: Aserțiuni care verifică starea intermediară / proprietățile numărului generat
    assert len(generated_number) == length, \
        f"RIP: Lungimea numărului generat trebuie să fie {length}, dar a fost {len(generated_number)}"
    assert generated_number.startswith(prefix), \
        f"RIP: Numărul generat trebuie să înceapă cu prefixul '{prefix}', dar a fost '{generated_number}'"

    # Aserțiunea originală, îmbunătățită pentru claritate
    assert check(prefix, length, generated_number) is True, \
        "RIP: Numărul generat ar trebui să fie valid conform funcției de verificare"

    # Test nou: prefix gol (caz de graniță)
    empty_prefix = ""
    short_length = 10
    generated_with_empty_prefix = generate(empty_prefix, short_length)
    assert len(generated_with_empty_prefix) == short_length
    assert generated_with_empty_prefix.startswith(empty_prefix) # Întotdeauna adevărat pentru prefix gol
    assert check(empty_prefix, short_length, generated_with_empty_prefix) is True

def test_generate_assertion_error():
    """
    Comment: Test nou pentru `generate` pentru a acoperi condiția `assert nrand > 0`.
    Acest lucru asigură că intrările invalide pentru lungime și lungimea prefixului (unde nrand <= 0)
    generează corect un AssertionError. Acest lucru acoperă explicit ramura `raise` din `generate`.
    """
    with pytest.raises(AssertionError, match="nrand > 0"):
        generate("123", 3) # nrand = 3 - 3 - 1 = -1
    with pytest.raises(AssertionError, match="nrand > 0"):
        generate("123", 4) # nrand = 4 - 3 - 1 = 0

def test_generate_checksum_already_zero_branch():
    """
    Comment: Test nou pentru `generate` pentru a viza în mod specific ramura `if check != 0` (ramura `else`)
    unde suma de control inițială a `pref + random_digits + '0'` este deja 0.
    Această cale este rară cu cifre aleatorii, dar poate fi forțată.
    Am modificat temporar `random.randrange` pentru a returna 0, asigurând că ultima cifră rămâne '0'.
    Acest lucru acoperă blocul `else` al deciziei L38 `if (check != 0)`.
    """
    # Utilizăm un prefix și o lungime specifice care vor face suma de control 0 dacă toate cifrele aleatorii sunt 0.
    # Pentru prefix "0", lungime 3: n = "0" + cifră_aleatorie + "0".
    # Dacă cifră_aleatorie este '0', n devine "000". luhn_checksum("000") este 0 (conform implementării).
    # Acest lucru asigură că `check` rămâne 0 și `10 - check` este sărit.
    def mock_randrange(limit):
        return 0

    original_randrange = random.randrange
    random.randrange = mock_randrange
    try:
        prefix = "0"
        length = 3
        generated_number = generate(prefix, length)
        assert generated_number == "000", \
            "RIP: Numărul generat ar trebui să fie '000' dacă cifra aleatorie este 0 și suma de control este deja 0"
        assert check(prefix, length, generated_number) is True
    finally:
        random.randrange = original_randrange # Restaurează funcția originală

def test_check_invalid_length():
    """
    Comment: Test original pentru `check` cu lungime invalidă.
    Aserțiunea a fost îmbunătățită pentru claritate.
    Acoperă ramura `check` L44 `if (len(num) != l)` (blocul `true`).
    """
    # Aserțiunea originală, îmbunătățită pentru claritate
    assert check("37", 15, "371234") is False, \
        "RIP: Numărul cu lungime incorectă ar trebui să returneze False"
    assert check("37", 15, "37123456789012345") is False, \
        "RIP: Numărul cu lungime incorectă (prea lungă) ar trebui să returneze False"

def test_check_invalid_prefix():
    """
    Comment: Test original pentru `check` cu prefix invalid.
    Aserțiunea a fost îmbunătățită pentru claritate.
    Acoperă ramura `check` L47 `if (num[:preflen] != pref)` (blocul `true`).
    """
    # Aserțiunea originală, îmbunătățită pentru claritate
    assert check("37", 15, "401234567890123") is False, \
        "RIP: Numărul cu prefix incorect ar trebui să returneze False"

def test_check_empty_number():
    """
    Comment: Test nou de graniță pentru `check` cu un șir de numere gol.
    Asigură robustețea pentru cazurile limită.
    Acest lucru va atinge și ramura `len(num) != l` (L44).
    """
    assert check("123", 10, "") is False, "RIP: Șirul de numere gol ar trebui să returneze False"

def test_check_number_too_short_for_prefix():
    """
    Comment: Test nou de graniță pentru `check` unde numărul este mai scurt decât prefixul.
    Acest lucru testează cazurile limită specifice pentru operațiile de tăiere și verificările de lungime.
    Acest lucru va atinge prima dată ramura `len(num) != l` (L44).
    """
    assert check("12345", 5, "123") is False, \
        "RIP: Numărul mai scurt decât lungimea sa necesară (care se potrivește lungimii prefixului) ar trebui să returneze False"
    assert check("12345", 10, "123") is False, \
        "RIP: Numărul mai scurt decât lungimea sa necesară (care nu se potrivește lungimii prefixului) ar trebui să returneze False"

# --- Mutanți Ocupați (Dedus) ---
# Fără o unealtă de testare a mutațiilor, ID-urile specifice ale mutanților nu pot fi furnizate.
# Cu toate acestea, îmbunătățirile sunt concepute pentru a elimina tipuri comune de mutanți:

# luhn_digit:
# - `n > 9` schimbat în `n >= 9` sau `n < 9`: Acoperit de `luhn_digit(4)`, `luhn_digit(5)`, `luhn_digit(9)`.
# - `return n - 9` schimbat în `return n` sau `return n + 9`: Acoperit de `luhn_digit(6)`, `luhn_digit(5)`, `luhn_digit(9)`.
# - `return n` schimbat în `return n - 9`: Acoperit de `luhn_digit(3)`, `luhn_digit(0)`, `luhn_digit(4)`.

# luhn_checksum:
# - `l % 2 == 0` schimbat în `l % 2 != 0` (Înlocuirea Operatorului Condițional): Acoperit prin testarea atât a lungimilor pare, cât și impare (`test_luhn_checksum_even_length`, `test_luhn_checksum_odd_length`).
# - `(i+1) % 2 == 0` schimbat în `(i+1) % 2 != 0`: Acoperit prin asigurarea aplicării `luhn_digit` pe cifrele corecte și `int()` pe celelalte în bucle (verificat de rezultatul corect al sumei de control).
# - `total_sum += int(n[i])` schimbat în `total_sum -= int(n[i])` sau mutanți de operatori aritmetici similari: Acoperit prin verificarea rezultatului exact `total_sum % 10` (0 în cazuri valide).
# - `total_sum % 10` schimbat în `total_sum % 10 == 0` (returnează boolean): Acoperit prin compararea explicită cu `0`.

# is_luhn_valid:
# - `luhn_checksum(n) == 0` schimbat în `luhn_checksum(n) != 0`: Acoperit de `test_is_luhn_valid_odd_length`, `test_is_luhn_valid_even_length`, `test_is_luhn_valid_invalid_number`.

# generate:
# - `nrand > 0` schimbat în `nrand >= 0`: Acoperit de `test_generate_assertion_error` care vizează specific `nrand=0`.
# - `check != 0` schimbat în `check == 0`: Acoperit de `test_generate_checksum_already_zero_branch` care forțează `check == 0` inițial, și de alte teste generale `generate` unde `check != 0` este norma.
# - Erori "off-by-one" în calculul `nrand` sau `n = n[:-1] + str(check)` (mutanți de slice): Parțial acoperite prin verificările de lungime din `test_generate_and_check`.

# check:
# - `len(num) != l` schimbat în `len(num) == l`: Acoperit de `test_check_invalid_length` și `test_generate_and_check`.
# - `num[:preflen] != pref` schimbat în `num[:preflen] == pref`: Acoperit de `test_check_invalid_prefix` și `test_generate_and_check`.
# - `return False` schimbat în `return True` (și invers): Acoperit de aserțiunile specifice true/false din `test_check_invalid_length`, `test_check_invalid_prefix`, etc.