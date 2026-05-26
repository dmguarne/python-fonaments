# Apunts — Sessió 8
## HTTP, `requests`, BeautifulSoup i Seguretat de claus
**Data:** 26/05/2026

---

## 1. HTTP — El protocol de la web

Quan el teu navegador carrega una pàgina, el que passa per sota és una **conversa** entre dos programes: el client (navegador) i el servidor.

**HTTP** (HyperText Transfer Protocol) és el conjunt de regles que governa aquesta conversa:

```
CLIENT                          SERVIDOR
  |                                 |
  |--- "Vull la pàgina /index" ---> |
  |                                 |
  | <--- "Aquí tens (codi 200)" --- |
```

### Els dos verbs fonamentals

| Verb | Quan s'usa | Exemples |
|------|-----------|---------|
| `GET` | Demanar/rebre alguna cosa del servidor | Veure pàgina, fer cerques, descarregar fitxers |
| `POST` | Enviar alguna cosa al servidor | Formularis, credencials, pujar fitxers |

### Codis d'estat

| Codi | Significat |
|------|-----------|
| `200` | Tot bé, aquí tens el contingut |
| `404` | No trobat |
| `403` | Prohibit (no tens accés) |
| `500` | Error al servidor |

---

## 2. OBJECTES — Atributs vs Mètodes

Un **objecte** agrupa **dades** (atributs) i **accions** (mètodes) relacionades.

**Analogia:** una tassa de cafè té propietats (color, capacitat, temperatura) i coses que pots fer amb ella (omplir-la, buidar-la).

La diferència sintàctica:

```python
objecte.atribut       # valor guardat — sense parèntesis
objecte.metode()      # acció que s'executa — amb parèntesis
```

**Exemple amb `response`:**
```python
response.status_code   # atribut — retorna 200, 404...
response.json()        # mètode — executa la conversió i retorna un diccionari
response.text          # atribut — retorna el contingut com a string
```

---

## 3. `requests` — Peticions HTTP des de Python

`requests` és una llibreria externa que permet fer peticions HTTP des de Python sense obrir cap navegador.

### Instal·lació a Ubuntu

```bash
sudo apt install python3-requests
```

**Nota important:** `requests` no és un mòdul de la biblioteca estàndard — és una **llibreria externa** que cal instal·lar. La diferència pràctica: els mòduls estàndard (`json`, `os`) venen amb Python; les llibreries externes cal obtenir-les.

### Petició bàsica

```python
import requests

response = requests.get("https://example.com")
print(response.status_code)  # 200
print(response.text)          # contingut HTML o JSON com a string
```

### Convertir la resposta a diccionari Python

```python
dades = response.json()   # equivalent a json.loads(response.text)
```

`response.json()` és un mètode que fa la conversió directament — no cal `import json` ni `json.loads()`.

---

## 4. APIs — Serveis de dades

Una **API** (Application Programming Interface) és un servei que retorna dades en format JSON quan li fas una petició GET.

### Exemple — API de la ISS

```python
import requests

try:
    response = requests.get("http://api.open-notify.org/iss-now.json")
    if response.status_code == 200:
        dades = response.json()
        print(f"La latitud és {dades['iss_position']['latitude']} i la longitud és {dades['iss_position']['longitude']}")
    else:
        print(response.status_code)
except ConnectionError:
    print("No s'ha pogut connectar amb el servidor")
```

**Estructura correcta del `try/except` amb xarxa:**
- El `if response.status_code` ha d'anar **dins** el `try` — si la connexió falla, `response` no existeix i el `if` petaria.

---

## 5. SEGURETAT — Mai hardcodejar claus al codi

### El problema

```python
# ❌ MAI fer això — la clau quedarà exposada a GitHub:
response = requests.get("https://api.nasa.gov/apod?api_key=ABC123XYZ")
```

Existeixen bots automatitzats que escanegen GitHub en temps real buscant API keys exposades. Una clau de pagament (OpenAI, AWS) pot generar **factures de milers d'euros** en hores.

**Regla d'or:** una clau que ha tocat un repositori públic s'ha de considerar compromesa per sempre. L'única solució és revocar-la i generar-ne una de nova.

### La solució — Variables d'entorn

Guardar la clau al sistema operatiu i llegir-la des de Python:

**Pas 1 — Afegir al `.bashrc`:**
```bash
nano ~/.bashrc
# Afegir al final:
export NASA_API_KEY="la_teva_clau_aqui"
```

**Pas 2 — Recarregar:**
```bash
source ~/.bashrc
```

**Pas 3 — Verificar:**
```bash
echo $NASA_API_KEY
```

**Pas 4 — Usar des de Python:**
```python
import os
import requests

api_key = os.environ.get("NASA_API_KEY")
response = requests.get(f"https://api.nasa.gov/planetary/apod?api_key={api_key}")
```

El codi que puges a GitHub **mai** conté la clau — només conté `os.environ.get("NASA_API_KEY")`.

### Sobre l'historial de Git

Fer un nou commit sense la clau **no esborra l'historial**. Git guarda tots els commits. La clau segueix visible en commits antics.

Les eines `git filter-branch` i `git filter-repo` permeten reescriure l'historial, però són complexes. Per això la regla és clara: **revoca i genera clau nova**, no intentis netejar.

---

## 6. ENTORNS VIRTUALS — Per entendre (proper pas)

Ubuntu protegeix el seu Python del sistema. Per això `pip install` dona error `externally-managed-environment`.

La solució professional són els **entorns virtuals**: cada projecte té el seu propi Python aïllat amb les seves pròpies llibreries. Dos projectes poden tenir versions diferents de la mateixa llibreria sense conflicte.

```bash
# Crear entorn virtual:
python3 -m venv nom_entorn

# Activar-lo:
source nom_entorn/bin/activate

# Instal·lar llibreries dins l'entorn:
pip install requests
```

**Pendent:** aplicar entorns virtuals a la propera sessió.

---

## 7. BeautifulSoup — Analitzar HTML

### La relació amb `requests`

```
requests      →    obté el HTML cru (text pla)
BeautifulSoup →    el converteix en estructura navegable Python
```

`requests` i BeautifulSoup sempre van junts per fer scraping de webs.

### Instal·lació

```bash
sudo apt install python3-bs4
```

### Ús bàsic

```python
import requests
from bs4 import BeautifulSoup

response = requests.get("https://books.toscrape.com")
soup = BeautifulSoup(response.text, "html.parser")
```

**`"html.parser"`** — indica a BeautifulSoup com interpretar el contingut. Converteix el text pla HTML en una estructura d'objectes Python navegable.

### Atributs i mètodes principals

```python
soup.title        # objecte complet amb etiquetes: <title>Books to Scrape</title>
soup.title.text   # només el text: "Books to Scrape"
```

### `.find()` i `.find_all()`

```python
# Trobar el primer element:
element = soup.find("p", class_="price_color")

# Trobar tots els elements:
elements = soup.find_all("article", class_="product_pod")

# Filtrar per atribut existent:
elements = soup.find_all("a", title=True)
```

**Nota:** `class_` amb guió baix — perquè `class` és una paraula reservada de Python.

### Accedir a atributs d'un element

```python
element["title"]   # equivalent a diccionari["clau"]
element.text       # text dins l'etiqueta, sense HTML
```

### Cercar dins d'un element (no a tota la pàgina)

```python
for article in soup.find_all("article", class_="product_pod"):
    titol = article.find("a", title=True)["title"]   # busca dins article
    preu = article.find("p", class_="price_color").text
```

**Regla:** `.find()` i `.find_all()` funcionen igual sobre qualsevol objecte BeautifulSoup — sigui `soup` (tota la pàgina) o un element concret.

---

## 8. SLICING DE STRINGS

El slicing permet extreure parts d'un string per posició:

```python
text = "£12.99"

text[2:]    # des de la posició 2 fins al final → "12.99"
text[:3]    # des del principi fins a la posició 2 → "£12"
text[1:4]   # de la posició 1 a la 3 → "12."
```

**Aplicació pràctica:** eliminar caràcters d'encoding incorrecte al principi d'un string.

---

## 9. PROJECTE FINAL — `scraping_03.py`

```python
import requests
from bs4 import BeautifulSoup

response = requests.get("https://books.toscrape.com")
soup = BeautifulSoup(response.text, "html.parser")
elements = soup.find_all("article", class_="product_pod")  # Retorna una llista amb tots els objectes "article"

print("Llibres:\n")
for i, article in enumerate(elements, start=1):  # Recorre cada element de la llista
    llibre = article.find("a", title=True)  # Troba l'etiqueta "a" que conté el títol
    titol = llibre["title"]  # Desa el contingut de l'atribut "title"
    preu = article.find("p", class_="price_color")  # Troba l'etiqueta "p" que conté el preu
    preu_final = preu.text  # Agafa el text dins l'etiqueta "p"
    print(f"{i}. {titol} | {preu_final[2:]} £")  # Elimina els dos primers caràcters per problema d'encoding
```

---

## 10. ERRORS COMUNS

| Error | Causa | Solució |
|-------|-------|---------|
| `response` no definida al `except` | `requests.get()` falla i el `if` peta igualment | Posar el `if status_code` dins el `try` |
| API key exposada a GitHub | Hardcodejar la clau al codi | `os.environ.get()` + `export` al `.bashrc` |
| `class` en lloc de `class_` | `class` és paraula reservada Python | Sempre `class_` a BeautifulSoup |
| `find_all` retorna llista | Intentar accedir a `.text` directament sobre la llista | Iterar amb `for` primer |
| Encoding incorrecte al preu | El símbol £ no es codifica bé | `preu_final[2:]` per eliminar caràcters inicials |
| `pip install` dona error | Ubuntu protegeix el Python del sistema | `sudo apt install python3-requests` o entorn virtual |

---

## 11. TAULA DE SEGUIMENT

| Skill | Nivell | Evidència | Proper pas |
|-------|--------|-----------|------------|
| Python — Variables | 5/10 | Aplicades amb autonomia en múltiples scripts | — |
| Python — Tipus | 6/10 | Casting fluid, detecció proactiva de tipus | — |
| Python — Condicions | 6/10 | Aplicades amb condicionals per `media_type` | Combinació complexa |
| Python — Bucles | 7/10 | `enumerate` amb `start=1` aplicat autònomament | Llistes per comprensió |
| Python — Llistes | 7/10 | Llistes de diccionaris, accés encadenat | Llistes per comprensió |
| Python — Funcions | 7/10 | `return`, Single Responsibility, paràmetres vs globals | Funcions amb valors per defecte |
| Python — Diccionaris | 5/10 | Accés encadenat, llistes de diccionaris | Diccionaris niats |
| Python — Fitxers | 5/10 | `try/except` per lectura i escriptura | Modes avançats |
| Python — JSON | 5/10 | `json.load`, `json.dump`, APIs reals | JSON amb múltiples APIs |
| Python — Errors | 6/10 | `try/except` amb xarxa, estructura correcta | Errors personalitzats |
| Python — Strings | 5/10 | Slicing deduït autònomament: `text[2:]` | Mètodes de string |
| requests | 4/10 | GET, `status_code`, `.json()`, variables d'entorn | POST, headers |
| BeautifulSoup | 4/10 | `find`, `find_all`, atributs, cerca dins element | Paginació, scraping avançat |
| Seguretat | 3/10 | Variables d'entorn, consciència de claus exposades | `.env` files, secrets management |
| Terminal | 5/10 | Navegació autònoma, `.bashrc`, `export` | Permisos i pipes |
| Git | 6/10 | Push a GitHub, flux complet, commits descriptius | Branques |
| Web | 2/10 | HTML bàsic, inspecció d'elements | DevTools |
| OSINT | 3/10 | Google ops | Automatitzar |

---

## DEURES PENDENTS

1. Ampliar `scraping_03.py`:
   - Afegir la **puntuació** de cada llibre (`"One"`, `"Two"`... a l'HTML)
   - Guardar resultats a `llibres.json` amb `json.dump` — cada llibre com a diccionari amb `titol`, `preu` i `puntuacio`
   - `git commit` i `git push`

2. **Investigar entorns virtuals** (`venv`): per a què serveixen i com es creen (sense implementar encara)

---

*Fitxer generat automàticament per Claude — Tutor de Programació i Ciberseguretat*
