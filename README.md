# T10: Imbunatatirea testarii unitare cu Inteligenta Artificiala

**Membrii echipa:** Niculae Cosmin, Branzea Malina
**Stadiu:** Implementare 1/3

## 1. Descrierea Proiectului si Fundament Teoretic
Acest proiect demonstreaza integrarea modelelor de limbaj in automatizarea testarii unitare, trecand de la o abordare stocastica la una predictiva si semantica.

Abordarile clasice precum *Fuzzing-ul* au o probabilitate exponential descrescatoare de a atinge stari adanci in cod (poor coverage), deoarece genereaza date aleatoare. Sistemul nostru, bazat pe modelul Gemini (LLM), rezolva aceasta problema realizand o **analiza statica** a codului sursa (`bank_account.py`). Modelul actioneaza ca un solver semantic: intelege constrangerile logice si genereaza direct datele de intrare necesare pentru a declansa rutele de executie ascunse.

## 2. Aplicarea Principiilor de Testare

Testele generate automat de scriptul nostru (`ai_test_generator.py`) aplica urmatoarele concepte teoretice:

* **Functional Testing:** IA-ul aplica automat **Equivalence Partitioning** si **Boundary Value Analysis**. De exemplu, pentru conditia `amount <= 0`, IA-ul nu testeaza numere la intamplare, ci tinteste direct frontiera (valoarea `0` si valori negative) pentru a valida aruncarea exceptiei `ValueError`.
* **Structural Testing & Coverage:** Scopul este parcurgerea Grafului de Flux de Control (CFG). Prompt-ul trimis catre IA forteaza modelul sa genereze teste care ating 100% **Statement Coverage** si **Branch/Decision Coverage** (testand atat ramurile de `True`, cat si cele de `False` ale deciziilor `if/else`).
* **The Oracle Problem & Mutation Testing:** Modelul rezolva problema oracolului scriind cod de tip *self-checking* (asertiuni stricte pentru stare si valori returnate). Aceste asertiuni sunt vitale pentru modelul **R.I.P.** (Reachability, Infection, Propagation) – asigurand faza de *Propagation* pentru a "ucide" orice potential mutant introdus in cod.

## 3. Configuratia Software
* **Limbaj:** Python 3.13
* **Framework Testare:** `pytest`
* **Integrare IA:** pachetul `google-genai` (Model: Gemini 2.5 Flash)
* **IDE:** Visual Studio Code (fara masina virtuala)

## 4. Comparatia Suitelor de Teste
Am creat fisierul `test_manual.py` pentru a compara o abordare manuala clasica cu cea bazata pe IA (`test_bank_account.py`).

* **Suita Manuala (`test_manual.py`):** Contine 3 teste care acopera doar calea de succes (*happy path*). Atingerea criteriilor de Branch Coverage necesita calcularea manuala a rutelor din CFG, un proces lent si predispus la erori de omisiune.
* **Suita Autogenerata:** Printr-un singur apel API, modelul a analizat structura clasei si a generat instantaneu o suita completa de teste documentate academic. Aceste teste acopera atat logica pozitiva, cat si cazurile limita si exceptiile, oferind comentarii care explica ce tip de acoperire este testat.

## 5. Captura de ecran cu rularea testelor
<img width="1878" height="1353" alt="image" src="https://github.com/user-attachments/assets/63db8ed7-e653-4a3f-a3d7-c116d12f3acf" />

## 6. Instructiuni de rulare
1. Instalare dependente: 
   `pip install -r requirements.txt`
2. Rulare script generare teste: 
   `python ai_test_generator.py`
3. Rulare toate testele: 
   `python -m pytest`

## 7. Prompt-ul utilizat
```text
Actioneaza ca un expert in Software Engineering si QA Automation.
Scrie teste unitare in Python folosind framework-ul `pytest` pentru urmatorul cod.

Trebuie sa aplici si sa documentezi prin comentarii urmatoarele concepte:
1. Functional Testing : Aplica 'Equivalence Partitioning' si 'Boundary Value Analysis' pentru variabile. Explica in comentariul testului ce partitie sau frontiera testezi.
2. Structural Testing : Asigura-te ca atingi 100% 'Statement Coverage' si 'Branch/Decision Coverage' parcurgand Graful de Flux de Control (CFG). Precizeaza ce ramura este acoperita.
3. Oracle & RIP Model : Rezolva 'Oracle Problem' folosind asertiuni stricte (self-checking code) pentru a asigura fazele de Reachability, Infection si Propagation (RIP) in vederea uciderii potentialilor mutanti.
4. Evita capcanele Random Testing : Genereaza exact datele semantice necesare pentru starile adanci, nu date aleatoare.

Returneaza doar codul Python final, valid, importand clasa. Nu adauga alte texte.
