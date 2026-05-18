import os

from google import genai

from criticality import format_report_for_prompt


def _make_client() -> genai.Client:
    key = "AIzaSyCid1KXuOZ5jOReffg-m-PioCFlsGcdw68"
    return genai.Client(api_key=key)


def improve_existing_tests(source_file, manual_test_file, output_file="bank_account_tests.py"):
    client = _make_client()
    print(f"-> Citesc codul sursa ({source_file}) si testele tale ({manual_test_file})...")

    if os.path.exists(output_file):
        print(f"[SKIP] -> Fisierul '{output_file}' exista deja. Sarim peste generarea prin API.")
        return

    with open(source_file, "r", encoding="utf-8") as f:
        source_code = f.read()
    with open(manual_test_file, "r", encoding="utf-8") as f:
        manual_tests = f.read()

    criticality_block = format_report_for_prompt(source_file)

    prompt = f"""
    Actioneaza ca un Senior QA Engineer. Sarcina ta este sa IMBUNATATESTI suita de teste existenta.

    ANALIZA AUTOMATA — zone de prioritate maxima pentru teste (ramuri, decizii, exceptii):
    {criticality_block}

    COD SURSA:
    {source_code}

    TESTE EXISTENTE (de imbunatatit):
    {manual_tests}

    CERINTE PENTRU IMBUNATATIRE:
    1. Pastreaza testele mele existente, dar imbunatateste-le asertiunile conform modelului RIP .
    2. Adauga teste noi pentru toate ramurile de decizie (Branch Coverage) care lipsesc in testele mele,
       acoperind in primul rand metodele si liniile marcate ca critice mai sus.
    3. Aplica Boundary Value Analysis pentru a verifica limitele de depunere si retragere.
    4. Urmareste acoperire la nivel de instructiune, decizie si conditie; propune cazuri care exerseaza
       fiecare ramura if si fiecare conditie compusa.
    5. Adauga comentarii care sa explice cum ai imbunatatit fiecare test manual.
    6. Te rog sa imi spui ce mutanti ai omorit cu aceste imbunatatiri, daca ai aceasta informatie.

    Returneaza doar codul Python final, valid, importand clasa din {source_file.replace('.py', '')}. Nu adauga alte texte.
    """

    print("-> Trimit codul catre modelul IA pentru imbunatatire...")
    
    try:
        response = client.models.generate_content(
            model='gemini-2.5-flash', 
            contents=prompt,
        )
    except Exception as e:
        print(f"-> Eroare la server: {e}")
        return
    
    with open(output_file, "w", encoding="utf-8") as test_file:
        clean_code = response.text.replace("```python", "").replace("```", "").strip()
        test_file.write(clean_code)

    print(f"-> Succes! Testele imbunatatite au fost salvate in: {output_file}")

if __name__ == "__main__":
    improve_existing_tests("bank_account.py", "test_manual_bank.py", "bank_account_tests.py")
    improve_existing_tests("luhn_algo.py", "test_manual_luhn.py", "luhn_algo_tests.py")