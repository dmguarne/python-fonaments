from pathlib import Path

# Ruta actual d'aquest fitxer:
BASE = Path(__file__).parent

# Construir ruta:
ruta_dades = BASE / "dades" / "prova.json"
ruta = Path("dades")

print(Path(__file__))
print(BASE)
print(ruta_dades)
print(ruta)

if ruta.exists():
    print("La carpeta ja existeix")
else:
    ruta.parent.mkdir(parents=True, exist_ok=True)
    print("Carpeta creada")