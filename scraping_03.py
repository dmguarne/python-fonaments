import requests
from bs4 import BeautifulSoup

response = requests.get("https://books.toscrape.com")
soup = BeautifulSoup(response.text, "html.parser")
elements = soup.find_all("article", class_="product_pod") # Retorna una llista amb tots els objectes "article".

print("Llibres:\n")
for i, article in enumerate(elements, start=1): # Recorre cada element de la llista
    llibre = article.find("a", title=True) # Troba l'etiqueta "a" que conté el títol i el desa a "llibre"
    titol = llibre["title"] # Desa a "titol" el contingut de l'atribut "title" de l'etiqueta "a"
    preu = article.find("p", class_="price_color") # Troba l'etiqueta "p" que conté el preu
    preu_final = preu.text # Agafa el text que hi ha dins l'etiqueta "p"
    print(f"{i}. {titol} | {preu_final[2:]} £") # Elimino els dos primers caracters perquè el símbol de lliure d'origen no es codifica bé