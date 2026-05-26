import json
import requests
from bs4 import BeautifulSoup

def conversio(numero): # Funció per convertir una paraula en número. L'argument que agafa és la paraula.
    equivalencies = { # Diccionari d'equivalències.
        "One" : 1,        
        "Two" : 2,
        "Three" : 3,
        "Four" : 4,
        "Five" : 5,
    }
    return(equivalencies[numero]) # Retorna el valor associat a la clau.

try:
    response = requests.get("https://books.toscrape.com")
    if response.status_code == 200: ## Si la resposta del servidor és positiva, executa el codi.
        soup = BeautifulSoup(response.text, "html.parser")
        elements = soup.find_all("article", class_="product_pod") # Retorna una llista amb tots els objectes "article".
        llibres = []
        print("Llibres:\n")
        for i, article in enumerate(elements, start=1): # Recorre cada element de la llista
            llibre = article.find("a", title=True) # Troba l'etiqueta "a" que conté el títol i el desa a "llibre"
            titol = llibre["title"] # Desa a "titol" el contingut de l'atribut "title" de l'etiqueta "a"
            preu = article.find("p", class_="price_color") # Troba l'etiqueta "p" que conté el preu
            preu_final = preu.text # Agafa el text que hi ha dins l'etiqueta "p"
            puntuacio = article.find("p")
            estrelles = puntuacio["class"][1]
            print(f"{i}. {titol} | {preu_final[2:]} £ | Puntuació: {conversio(estrelles)} estrelles") # Elimino els dos primers caracters perquè el símbol de lliure d'origen no es codifi
            nou_llibre = { # Crea el diccionari per a aquest llibre amb les tres claus
                "titol": titol,
                "preu": preu_final[2:],
                "puntuacio": conversio(estrelles),
            }
            llibres.append(nou_llibre) # Afegeix el diccionari a la llista de llibres.
        try:
            with open('llibres.json', 'w') as fitxer: ## Obre agenda.json en mode escriptura per actualitzar-lo.
                json.dump(llibres, fitxer, ensure_ascii=False, indent=4)
        except PermissionError:
            print("No tens permisos per desar el fitxer.")
        except OSError:
            print("Error del sistema.")

except ConnectionError: ## Si la connexió amb el servidor ha fallat, informa.
    print("No s'ha pogut connectar amb el servidor")