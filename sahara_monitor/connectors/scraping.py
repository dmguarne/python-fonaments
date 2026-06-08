import json
import requests
import argparse
import logging
import re
from bs4 import BeautifulSoup
from pathlib import Path

# Ruta actual d'aquest fitxer:
BASE = Path(__file__).parent

## Obtenir_noticies ha de retornar una llista de diccionaris:
def obtenir_noticies():
    llista_noticies = [] ## Defineix la variable on s'emmagatzema cada diccionari
    pagina = 0 ## Definim la primera pàgina de cerca
    try:
        resposta = requests.get(f"https://www.spsrasd.info/es/depeches/categories/militar-seguridad?page={pagina}") ## Obté l'html complet de la URL.        
    except (requests.exceptions.ConnectionError, requests.exceptions.HTTPError) as e: ## Si es produeix un error de connexió amb el servidor, informa i surt.
        logging.warning(f"Error: {e}")
        return(f"Error: {e}")
        exit()
    logging.info("Connexió establerta.")
    if resposta.status_code != 200:
        logging.warning(f"La pàgina {pagina} retorna el codi de servidor {resposta.status_code}")
        return llista_noticies ## Retorna la llista de diccionaris.
    while resposta.status_code == 200: ## Mentre la connexió és correcta i la pàgina existeix, executa el codi.
        logging.info(f"Buidant pàgina {pagina + 1}")
        soup = BeautifulSoup(resposta.text, "html.parser") ## Carrega la funció que analitza l'html.
        noticies = soup.find_all("h3", class_="card-title") ## Troba totes les etiquetes que contenen un titular.
        if not noticies: ## Si arriba a una pàgina en blanc:
            logging.info(f"Pàgina {pagina + 1} sense contingut")
            break
        for noticia in noticies: ## Itera sobre cada etiqueta amb titular
            troba_titular = noticia.find("a") ## Accedeix a l'etiqueta 'a' dins de l'element
            titular = troba_titular.text ## Desa el text de l'etiqueta a 'titular'
            url = noticia.find("a", href=True) ## Accedeix a l'atribut href dins de l'element.
            enllaç = "https://www.spsrasd.info" + f"{url['href']}" ## Construeix l'enllaç complet.
            post_data = noticia.parent.parent.find("span", class_="post-date") ## Cerca l'etiqueta de data en la jerarquia correcta.
            data = re.search(r"\d\d/\d\d/\d\d\d\d", post_data.text) ## Cerca només la cadena que conté la data.
            diccionari = {"titular": titular, "url": enllaç, "data": data.group(), "font": "Sahara Press Service"} ## Construeix el diccionari desant cada variable a la clau corresponent.
            llista_noticies.append(diccionari) ## Afegeix el diccionari a la llista de diccionaris.
            logging.info("Element afegit.")
        pagina += 1
        resposta = requests.get(f"https://www.spsrasd.info/es/depeches/categories/militar-seguridad?page={pagina}")
    logging.info(f"La pàgina {pagina + 1} retorna el codi de servidor {resposta.status_code}")
    logging.info("Buidatge completat.")
    return llista_noticies ## Retorna la llista de diccionaris.
