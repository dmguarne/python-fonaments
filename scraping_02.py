import os
import requests

api_key = os.environ.get("NASA_API_KEY")

try:
    response = requests.get(f"https://api.nasa.gov/planetary/apod?api_key={api_key}") ## Fa la petició al servidor i l'emmagatzema en text a la variable response.
    if response.status_code == 200: ## Si la resposta del servidor és positiva, executa el codi.
        dades = response.json() ## Converteix el text de la resposta del servidor a Python.
        data = dades['date']
        media = dades['media_type']# comprova si el media del dia és imatge o video
        missatge_media = "" # Crea la variable missatge_media sense contingut, i segons el que retorni l'API, emmagatzema una str diferent
        if media == "image":
            missatge_media = "La imatge del dia és: "
        elif media == "video":
            missatge_media = "El vídeo del dia és: "
        else: # Per si de cas hi ha tipus d'arxiu diferents de imatge o vídeo
            missatge:media = "El document del dia és"
        print(f"Data: {data}\n{missatge_media} {dades['title']} i l'enllaç és {dades["url"]}") ## Imprimeix les claus tipus, títol i url.
    else:
        print(response.status_code) ## Si la resposta del servidor no és 200, informa del codi de resposta.
except ConnectionError: ## Si la connexió amb el servidor ha fallat, informa.
    print("No s'ha pogut connectar amb el servidor")