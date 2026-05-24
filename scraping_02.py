import os
import requests

api_key = os.environ.get("NASA_API_KEY")

try:
    response = requests.get(f"https://api.nasa.gov/planetary/apod?api_key={api_key}") ## Fa la petició al servidor i l'emmagatzema en text a la variable response.
    if response.status_code == 200: ## Si la resposta del servidor és positiva, executa el codi.
        dades = response.json() ## Converteix el text de la resposta del servidor a Python.
        print(f"La imatge del dia és {dades['media_type']}, el títol és {dades['title']} i l'enllaç és {dades["url"]}") ## Imprimeix les claus tipus, títol i url.
    else:
        print(response.status_code) ## Si la resposta del servidor no és 200, informa del codi de resposta.
except ConnectionError: ## Si la connexió amb el servidor ha fallat, informa.
    print("No s'ha pogut connectar amb el servidor")