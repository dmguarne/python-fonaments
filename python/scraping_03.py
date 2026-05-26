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
    return equivalencies[numero] # Retorna el valor associat a la clau.

try:
    pagina = 1
    llibres = []
    response = requests.get(f"https://books.toscrape.com/catalogue/page-1.html")    
    while response.status_code == 200 and pagina < 51: ## Si la resposta del servidor és positiva, executa el codi.        
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

            nou_llibre = { # Crea el diccionari per a aquest llibre amb les tres claus
                "titol": titol,
                "preu": preu_final[2:],
                "puntuacio": conversio(estrelles),
            }
            llibres.append(nou_llibre) # Afegeix el diccionari a la llista de llibres.
        pagina += 1
        response = requests.get(f"https://books.toscrape.com/catalogue/page-{pagina}.html")
    if pagina == 51:
        print("Navegació finalitzada.")
    else:
        print(f"La pàgina {pagina} retorna el codi de servidor {response.status_code}")

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

