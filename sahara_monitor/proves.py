import logging
from pathlib import Path
from connectors.scraping import obtenir_noticies
from eines.magatzem import desar_noticies

# Ruta actual d'aquest fitxer:
BASE = Path(__file__).parent

# Configuració del logging:
logging.basicConfig(
    filename=BASE / "scraping.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)
# Afegeix també sortida per pantalla:
logging.getLogger().addHandler(logging.StreamHandler())

noticies = obtenir_noticies()
print(desar_noticies(noticies))