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

## Nivells:
## DEBUG: Informació detallada.
## INFO: Confirmació que el funcionamient és correcte.
## WARNING: Indica situacions potencialment problemàtiques.
## ERROR: Indica errors en el funcionament.
## CRITICAL: Errors que aturen el programa. 

# Afegeix també sortida per pantalla:
logging.getLogger().addHandler(logging.StreamHandler())