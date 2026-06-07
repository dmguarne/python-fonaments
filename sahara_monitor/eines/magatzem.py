import json
import logging
from pathlib import Path

# Ruta actual d'aquest fitxer:
BASE = Path(__file__).parent

# Ruta de 'magatzem.json':
ruta_magatzem = BASE.parent / "dades" / "magatzem" / "magatzem.json"

ruta_magatzem.parent.mkdir(parents=True, exist_ok=True)  # Crea la carpeta si no existeix

def desar_noticies(llista_noticies):

    try:
        with open(ruta_magatzem, "r") as fitxer: ## Obre magatzem.json i el llegeix a fitxer.
            magatzem = json.load(fitxer) ## Estableix la variable magatzem, que emmagatzema el contingut del fitxer.
    except FileNotFoundError:
        magatzem = []
    except json.JSONDecodeError:
        logging.warning("El fitxer magatzem.json està corromput.")
        magatzem = []

    llista_urls = [diccionari["url"] for diccionari in magatzem] ## Crea una llista de urls presents a magatzem.
    for element in llista_noticies: ## Recorre cada diccionari de la llista de diccionaris de llista_noticies.         
        if not element["url"] in llista_urls: ## Busca la url dins la llista de diccionaris i executa el codi si no existeix.
            magatzem.append(element) ## Afegeix el diccionari a magatzem.

    try:
        with open(ruta_magatzem, 'w') as fitxer: ## Obre magatzem.json en mode escriptura per actualitzar-lo.
            json.dump(magatzem, fitxer, ensure_ascii=False, indent=4)
    except PermissionError:
        logging.critical("No tens permisos per desar el fitxer.")
    except OSError:
        logging.critical("Error del sistema.")
    
    return f"{ruta_magatzem} actualitzat correctament."
