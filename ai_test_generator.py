from google import genai
import os

# 1. Configurare API Key
API_KEY = "" 
client = genai.Client(api_key=API_KEY)

def generate_tests_for_file(filepath):
    print(f"-> Citesc fișierul {filepath}...")
    
    with open(filepath, "r", encoding="utf-8") as file:
        source_code = file.read()

    # 2. Construim comanda academică pentru AI bazată pe Cursurile 1-7
    prompt = f"""
    Acționează ca un expert în Software Engineering și QA Automation.
    Scrie teste unitare în Python folosind framework-ul `pytest` pentru următorul cod.
    
    Trebuie să aplici și să documentezi prin comentarii următoarele concepte:
    1. Functional Testing : Aplică 'Equivalence Partitioning' și 'Boundary Value Analysis' pentru variabile. Explică în comentariul testului ce partiție sau frontieră testezi.
    2. Structural Testing : Asigură-te că atingi 100% 'Statement Coverage' și 'Branch/Decision Coverage' parcurgând Graful de Flux de Control (CFG). Precizează ce ramură este acoperită.
    3. Oracle & RIP Model : Rezolvă 'Oracle Problem' folosind aserțiuni stricte (self-checking code) pentru a asigura fazele de Reachability, Infection și Propagation (RIP) în vederea uciderii potențialilor mutanți.
    4. Evită capcanele Random Testing : Generează exact datele semantice necesare pentru stările adânci, nu date aleatoare.
    
    Returnează doar codul Python final, valid, importând clasa din `{filepath.replace('.py', '')}`. Nu adăuga alte texte în afara codului.
    
    Codul sursă:
    {source_code}
    """

    print("-> Trimit codul către modelul IA ...")
    
    # 3. Apelăm API-ul (folosim gemini-2.5-flash)
    try:
        response = client.models.generate_content(
            model='gemini-2.5-flash', 
            contents=prompt,
        )
    except Exception as e:
        print(f"-> Eroare la serverul Google: {e}\nTe rog mai rulează scriptul o dată peste 10 secunde.")
        return
    
    # 4. Salvăm rezultatul
    test_filename = f"test_{filepath}"
    with open(test_filename, "w", encoding="utf-8") as test_file:
        clean_code = response.text.replace("```python", "").replace("```", "").strip()
        test_file.write(clean_code)
        
    print(f"-> Succes! Testele au fost salvate în: {test_filename}")

if __name__ == "__main__":
    generate_tests_for_file("bank_account.py")