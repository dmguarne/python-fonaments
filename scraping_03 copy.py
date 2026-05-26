import json
import requests
from bs4 import BeautifulSoup

try:
    with open("llibres.json", "r") as fitxer: ## Obre llibres.json i el llegeix a fitxer.
        llibres = json.load(fitxer) ## Estableix la variable llibres, que emmagatzema el contingut del fitxer
except FileNotFoundError:
    llibres = []
except json.JSONDecodeError:
    print("El fitxer llibres.json està corromput.")
    llibres = []



response = requests.get("https://books.toscrape.com")
soup = BeautifulSoup(response.text, "html.parser")
elements = soup.find_all("article", class_="product_pod") # Retorna una llista amb tots els objectes "article".

print("Llibres:\n")
for i, article in enumerate(elements, start=1): # Recorre cada element de la llista
    llibre = article.find("a", title=True) # Troba l'etiqueta "a" que conté el títol i el desa a "llibre"
    titol = llibre["title"] # Desa a "titol" el contingut de l'atribut "title" de l'etiqueta "a"
    preu = article.find("p", class_="price_color") # Troba l'etiqueta "p" que conté el preu
    preu_final = preu.text # Agafa el text que hi ha dins l'etiqueta "p"
    puntuacio = ""
    if article.find("p", class_="star-rating One"):
        puntuacio = "1/5"
    elif article.find("p", class_="star-rating Two"):
        puntuacio = "2/5"
    elif article.find("p", class_="star-rating Three"):
        puntuacio = "3/5"
    elif article.find("p", class_="star-rating Four"):
        puntuacio = "4/5"
    elif article.find("p", class_="star-rating Five"):
        puntuacio = "5/5"    
    print(f"{i}. {titol} | {preu_final[2:]} £ | Puntuació: {puntuacio}") # Elimino els dos primers caracters perquè el símbol de lliure d'origen no es codifica bé
    nou_llibre = {
        "titol": titol,
        "preu": preu,
        "puntuacio": puntuacio,
    }
    llibres.append(nou_llibre)

    # Afegir la puntuació de cada llibre
    # Desar els resultats en un fitxer llibres.json (utilitzant json.dump). Cada llibre com un diccionari amb titol, preu i puntuacio
    # <p class="star-rating One">
 
try:
    with open('llibres.json', 'w') as fitxer: ## Obre agenda.json en mode escriptura per actualitzar-lo.
        json.dump(llibres, fitxer, ensure_ascii=False, indent=4) ## Bolca el contingut actualitzat d'agenda al json sobreescrivint el contingut previ.
except PermissionError:
    print("No tens permisos per desar el fitxer.")
except OSError:
    print("Error del sistema.")

