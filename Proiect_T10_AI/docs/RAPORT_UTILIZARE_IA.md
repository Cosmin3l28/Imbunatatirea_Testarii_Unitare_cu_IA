# Raport: utilizarea unui tool de IA în testarea software

**Tool folosit:** Google Gemini prin SDK-ul `google-genai`, model `gemini-2.5-flash`.

**Transparență:** IA a fost folosită pentru îmbunătățirea suitei de teste pornind de la `test_manual.py`. Rezultatul a fost revizuit manual, apoi validat prin `pytest`, `pytest-cov` și `mutmut`.

---

## 1. Context și obiectiv

Am testat clasa `BankAccount` din `bank_account.py`, care conține funcționalități de depunere/retragere și validări de input. Suita inițială (`test_manual.py`) acoperea fluxurile de bază, dar nu acoperea complet ramurile de excepție și cazurile de frontieră.

Obiectivul utilizării IA a fost să extindă testele astfel încât să crească acoperirea pe instrucțiuni/ramuri și să reducă mutanții supraviețuitori. Pentru prioritizare, promptul a inclus analiza automată din `criticality.py` (conform implementării din proiect).

---

## 2. Prompt transmis modelului

Promptul este construit în `ai_test_generator.py`, funcția `improve_existing_tests`, variabila `prompt`. Mai jos este versiunea folosită în proiect (cu blocurile dinamice incluse):

> „Acționează ca un Senior QA Engineer. Sarcina ta este să îmbunătățești suita de teste existentă. Primești analiza automată a zonelor critice, codul sursă și testele existente. Păstrează testele existente, îmbunătățește aserțiunile conform modelului RIP, adaugă teste pentru ramurile lipsă (branch coverage), aplică Boundary Value Analysis pentru depunere/retragere și urmărește acoperire pe instrucțiune, decizie, condiție. Returnează doar codul Python final valid.”

Blocurile injectate în prompt:
- raport criticitate: `format_report_for_prompt(source_file)`;
- cod sursă: conținutul din `bank_account.py`;
- teste inițiale: conținutul din `test_manual.py`.

---

## 3. Răspunsul modelului (extras relevant)

Modelul a returnat cod Python pentru suita extinsă, salvată în `test_bank_account_V2.py`. Exemple de îmbunătățiri:
- teste noi pentru valori de frontieră (`0`, valori negative, `0.01`, retragere exact egală cu soldul, puțin peste sold);
- verificări pe ramuri de excepție (`ValueError`) și pe rezultate (`True/False`);
- comentarii explicative pentru corelarea cu RIP/BVA.

După revizuire manuală, aserțiunile pe mesaje de excepție au fost întărite la egalitate exactă (`str(exc.value) == ...`) pentru a elimina mutanți care supraviețuiau când mesajul era doar aproximativ potrivit.

---

## 4. Comparare: teste proprii vs. teste asistate de IA

| Criteriu | Suita inițială (`test_manual.py`) | După IA / revizuire (`test_bank_account_V2.py`) |
|----------|-----------------------------------|--------------------------------------------------|
| Număr de teste | 3 | 14 |
| Acoperire linii (`Cover`) | 81% | 100% |
| Ramuri neacoperite / parțiale (`BrPart`) | 2 | 0 |
| Linii neatinse (`Miss`) | 2 | 0 |
| Mutanți omorâți (`mutmut`) | 6 / 20 | 20 / 20 |
| Mutanți supraviețuitori (`mutmut`) | 14 / 20 | 0 / 20 |
| Scor mutațional | 30% | 100% |
| Tipuri de cazuri | fluxuri de bază | fluxuri bază + BVA + excepții + validări stricte |

**Interpretare:** IA a adăugat rapid cazuri relevante pentru limite și excepții, crescând acoperirea structurală. Revizuirea umană a fost necesară pentru întărirea unor aserțiuni (în special pe mesaje de eroare), astfel încât mutanții neechivalenți să fie eliminați. Rezultatul final indică o suită mult mai robustă după etapa IA + revizie manuală.

---

## 5. Rularea codului generat

Pași utilizați:
1. Setare cheie API în variabile de mediu (`GOOGLE_API_KEY` sau `GEMINI_API_KEY`);
2. Rulare generator: `python ai_test_generator.py`;
3. Validare suite:
   - `python -m pytest -q test_bank_account_V2.py`;
   - `python -m pytest test_bank_account_V2.py --cov=bank_account --cov-branch --cov-report=term-missing`;
4. Validare mutațională în WSL cu `mutmut` (comparativ AI vs manual, prin `setup.ai.cfg` și `setup.manual.cfg`).

**Capturi de inclus în repo (`docs/capturi/`):**
- rulare generator IA;
- rulare pytest pentru `test_manual.py` și `test_bank_account_V2.py`;
- raport coverage;
- rezultate `mutmut run` + `mutmut results` pentru ambele suite.

---

## 6. Limite și riscuri ale IA în testare

IA poate produce teste plauzibile, dar cu aserțiuni prea permisive sau redundante. Acoperirea mare nu garantează automat detectarea defectelor, iar scorul mutațional rămâne un indicator mai strict. De aceea, testele generate trebuie revizuite manual, calibrate pe cerințele de business și validate cu tool-uri complementare (`pytest-cov`, `mutmut`) [1], [2], [3].

---

## 7. Referințe bibliografice (citate în text)

[1] Google LLC, *Google Gen AI SDK for Python*, documentație oficială. Disponibil: https://googleapis.github.io/python-genai/ (accesat 2026).

[2] Myers, G. J.; Sandler, C.; Badgett, T., *The Art of Software Testing*, ediție relevantă, Wiley.

[3] mutmut project, *mutmut mutation testing tool* (documentație și issue tracker). Disponibil: https://github.com/boxed/mutmut (accesat 2026).

[4] Coverage.py documentation, *Branch coverage measurement*. Disponibil: https://coverage.readthedocs.io/ (accesat 2026).
