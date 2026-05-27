import json
import requests
import argparse
import eines.utils as utils
from bs4 import BeautifulSoup

parser = argparse.ArgumentParser() # Crea l'objecte parser
parser.add_argument("--pagina-inici", type=int, default=1) # Crea l'argument --pagina-inici i li dona tipus int i valor 1 per defecte.
parser.add_argument("--pagina-fi", type=int, default=100)

arguments = parser.parse_args() # Defineix el mètode que analitza l'argument introduït en el terminal.

try:
    with open("llibres.json", "r") as fitxer: ## Obre agenda.json i el llegeix a fitxer.
        llibres = json.load(fitxer) ## Estableix la variable agenda, que emmagatzema el contingut del fitxer
except FileNotFoundError:
    llibres = []
except json.JSONDecodeError:
    print("El fitxer agenda.json està corromput.")
    llibres = []

try:
    pagina = arguments.pagina_inici # Emmagatzema a pagina el numero rebut com a argument a arguments.    
    final = arguments.pagina_fi
    response = requests.get(f"https://books.toscrape.com/catalogue/page-{pagina}.html")    
    while response.status_code == 200 and pagina <= final: ## Si la resposta del servidor és positiva, executa el codi.        
        print(f"Pàgina {pagina}/50")
        soup = BeautifulSoup(response.text, "html.parser")
        elements = soup.find_all("article", class_="product_pod") # Retorna una llista amb tots els objectes "article".
        for i, article in enumerate(elements): # Recorre cada element de la llista
            llibre = article.find("a", title=True) # Troba l'etiqueta "a" que conté el títol i el desa a "llibre"
            titol = llibre["title"] # Desa a "titol" el contingut de l'atribut "title" de l'etiqueta "a"
            preu = article.find("p", class_="price_color") # Troba l'etiqueta "p" que conté el preu
            preu_final = preu.text # Agafa el text que hi ha dins l'etiqueta "p"
            puntuacio = article.find("p")
            estrelles = puntuacio["class"][1]
            if not titol in [llibre["titol"] for llibre in llibres]:
                nou_llibre = { # Crea el diccionari per a aquest llibre amb les tres claus
                    "titol": titol,
                    "preu": preu_final[2:],
                    "puntuacio": utils.conversio(estrelles),
                }
                llibres.append(nou_llibre) # Afegeix el diccionari a la llista de llibres.
        pagina += 1
        response = requests.get(f"https://books.toscrape.com/catalogue/page-{pagina}.html")
    if response.status_code == 403 or response.status_code == 404: # Si la pàgina no existeix, atura el bucle i informa l'usuari.
        print("Navegació finalitzada.")
    else:
        print(f"La pàgina {pagina} retorna el codi de servidor {response.status_code}") # Si el codi de resposta és un altre, n'informa l'usuari.

    for i, linia in enumerate(llibres, start=1): # Agafa la llista llibres i enumera els seus elements (diccionaris).
        print(f"{i}. {linia['titol']} | {linia['preu']} £ | {linia['puntuacio']} estrelles")
   
    try:
        with open('llibres.json', 'w') as fitxer: ## Obre agenda.json en mode escriptura per actualitzar-lo.
            json.dump(llibres, fitxer, ensure_ascii=False, indent=4)
    except PermissionError:
        print("No tens permisos per desar el fitxer.")
    except OSError:
        print("Error del sistema.")

except ConnectionError: ## Si la connexió amb el servidor ha fallat, informa.
    print("No s'ha pogut connectar amb el servidor")

