from dotenv import load_dotenv
import os
import requests
import json

load_dotenv()
token = os.environ.get("GITHUB_TOKEN")

def comprovar_issues(url, token):
    try:
        print("Issues:\n")
        comprovar_issues = requests.get(f"{url}", headers={"Authorization": f"Bearer {token}"})
        comprovar_issues.raise_for_status()
        issues = comprovar_issues.json()
        for i, element in enumerate(issues):
            print(f"{i + 1}. {element['title']} | {element['body']} | {element['state']}")
        return issues
    except (requests.exceptions.ConnectionError, requests.exceptions.HTTPError) as e:
        return(f"Error: {e}")

resposta = requests.get(f"https://api.github.com/users/dmguarne/repos", headers={"Authorization": f"Bearer {token}"})
print(resposta)

dades = resposta.json()

# 4 maneres de recórrer la llista i imprimir la clau 'name:

# 1. Bucle amb comptador: per a cada iteració durant la longitud de 'dades', imprimeix la clau el valor de 'name' per a cada iteració.
for i in range(len(dades)):
    print(dades[i]['name'])

# 2. Bucle amb enumerate(): per a cada iteració dels diccionaris enumerats de dades, imprimeix el valor de 'name' per a cada iteració. 
for i, diccionari in enumerate(dades):
    print(dades[i]['name'])

# 3. Llista per comprensió: Imprimeix en una llista el valor de 'name' per a cada diccionari dins de 'dades'  
print([element['name'] for element in dades])

# 4. Bucle simple: per a cada element de la llista 'dades', imprimeix el valor de la seva clau 'name'
for element in dades:
    print(element['name'])

try:
    llista_commits = requests.get(f"https://api.github.com/repos/dmguarne/python-fonaments/commits", headers={"Authorization": f"Bearer {token}"})
    llista_commits.raise_for_status()
    commits = llista_commits.json()
    for i, element in enumerate(commits):
        print(f"{i + 1}. Missatge: {element['commit']['message']} ({element['commit']['author']['name']} | {element['commit']['author']['date']})")
except (requests.exceptions.ConnectionError, requests.exceptions.HTTPError) as e: ## Si la connexió amb el servidor no retorna 200 o ha fallat, informa.
    print(f"Error: {e}")


comprovar_issues("https://api.github.com/repos/dmguarne/python-fonaments/issues", token)

obrir_issue = input("Vols crear una nova issue? S/N: ")
if obrir_issue == "S" or obrir_issue == "s":
    print("Es crearà una issue amb el nom: 'prova' i el body: 'contingut'")
    try:
        peticio_issues = requests.post(f"https://api.github.com/repos/dmguarne/python-fonaments/issues", headers={"Authorization": f"Bearer {token}"}, json={"title": "prova", "body": "contingut"})
        peticio_issues.raise_for_status()
        print("Petició acceptada.")
    except (requests.exceptions.ConnectionError, requests.exceptions.HTTPError) as e:
        print(f"Error: {e}")
elif obrir_issue == "N" or obrir_issue == "n":
    print("No s'ha creat cap issue.")
else:
    print("La resposta ha de ser 's' o 'n'")

comprovar_issues("https://api.github.com/repos/dmguarne/python-fonaments/issues", token)


confirma_tancar = input("Vols tancar totes les issues obertes? S/N ")
if confirma_tancar == "S" or confirma_tancar == "s":
    try: 
        issues = comprovar_issues("https://api.github.com/repos/dmguarne/python-fonaments/issues", token)
        for i in issues:
            resposta_patch = requests.patch(f"https://api.github.com/repos/dmguarne/python-fonaments/issues/{i['number']}", headers={"Authorization": f"Bearer {token}"}, json={"state": "closed"})    
            print(resposta_patch.status_code)
            print(f"Issue {i['number']} tancada")
    except (requests.exceptions.ConnectionError, requests.exceptions.HTTPError) as e:
        print(f"Error: {e}")
elif confirma_tancar == "N" or confirma_tancar == "n":
    print("No s'ha esborrat cap issue.")
else:
    print("La resposta ha de ser 's' o 'n'.")

comprovar_issues("https://api.github.com/repos/dmguarne/python-fonaments/issues", token)
