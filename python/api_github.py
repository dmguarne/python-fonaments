from dotenv import load_dotenv
import os
import requests
import json

load_dotenv()
token = os.environ.get("GITHUB_TOKEN")

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