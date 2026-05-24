# Apunts — Sessió 7
## Gestió d'errors (`try/except`), validació robusta i GitHub
**Data:** 22/05/2026

---

## 1. EL PROBLEMA DELS ERRORS INESPERATS

Tots els programes assumeixen que el món funciona bé. Però el món real no és tan amable:

- El fitxer que vols llegir no existeix
- L'usuari escriu text on hauria d'escriure un número
- El disc està ple i no es pot guardar

Un programa professional no pot **petar** quan passa alguna cosa inesperada. Ha de **gestionar l'error** i continuar.

**Analogia:** obres la nevera per agafar llet.
- ❌ **Sense gestió d'errors:** assumeixes que hi ha llet. Si no n'hi ha, el programa peta.
- ✅ **Amb gestió d'errors:** mires si hi ha llet. Si no n'hi ha, surts a comprar-ne.

---

## 2. `try/except` — Sintaxi bàsica

```python
try:
    # codi que podria fallar
except TipusError:
    # què fer si falla
```

Python intenta executar el bloc `try`. Si llança un error del tipus especificat, en lloc de petar, executa el bloc `except`.

### Exemple aplicat — Llegir un fitxer JSON

**Error que dona Python si el fitxer no existeix:**
```
FileNotFoundError: [Errno 2] No such file or directory: 'agenda.json'
```

**Solució amb `try/except`:**
```python
try:
    with open("agenda.json", "r") as fitxer:
        agenda = json.load(fitxer)
except FileNotFoundError:
    agenda = []
```

**Llegeix-ho en veu alta:** *"Intenta obrir el fitxer. Si no existeix, comença amb una agenda buida."*

---

## 3. CAPTURAR MÚLTIPLES ERRORS

Un sol bloc `try` pot tenir múltiples `except`, un per cada tipus d'error:

```python
try:
    with open("agenda.json", "r") as fitxer:
        agenda = json.load(fitxer)
except FileNotFoundError:
    agenda = []
except json.JSONDecodeError:
    print("El fitxer agenda.json està corromput.")
    agenda = []
```

**`json.JSONDecodeError`:** error que dona Python quan el fitxer existeix però el contingut no és JSON vàlid (per exemple, si algú l'ha editat a mà i ha trencat el format).

---

## 4. LA REGLA D'OR — Mai capturis genèricament

```python
# ❌ Mal hàbit — amaga tots els errors, inclosos els bugs teus:
except Exception:
    pass

# ✅ Professional — captures exactament el que esperes:
except FileNotFoundError:
    agenda = []
```

Si captureixes tot genèricament, un bug al teu propi codi passarà desapercebut. Un `NameError` o `TypeError` que hauries de veure i corregir quedarà silenciat. **Perillós.**

---

## 5. ERRORS COMUNS I ELS SEUS NOMS

| Error | Quan es produeix |
|-------|-----------------|
| `FileNotFoundError` | Intentar obrir un fitxer que no existeix |
| `json.JSONDecodeError` | El fitxer existeix però el contingut no és JSON vàlid |
| `ValueError` | Conversió de tipus impossible (`int("hola")`) |
| `PermissionError` | No tens permisos per llegir o escriure un fitxer |
| `OSError` | Error genèric del sistema operatiu (disc ple, ruta incorrecta...) |

---

## 6. GESTIÓ D'ERRORS EN ESCRIPTURA

No només la lectura pot fallar. L'escriptura també:

```python
try:
    with open('agenda.json', 'w') as fitxer:
        json.dump(agenda, fitxer, ensure_ascii=False, indent=4)
except PermissionError:
    print("No tens permisos per desar el fitxer.")
except OSError:
    print("Error del sistema. No s'han pogut guardar els canvis.")
```

**Regla pràctica:** qualsevol operació d'entrada/sortida (fitxers, xarxa, base de dades) és candidata a tenir `try/except`.

---

## 7. VALIDACIÓ ROBUSTA D'ENTRADES — `try/except` dins `while`

### El problema

```python
# ❌ Només cobreix el primer intent:
try:
    edat = int(input("Introdueix l'edat: "))
except ValueError:
    print("L'edat ha de ser un número.")
    edat = int(input("Introdueix l'edat: "))  # si torna a fallar, peta igualment
```

### La solució — Patró `while` + `try/except`

```python
# ✅ Robust — continua fins que l'entrada sigui vàlida:
valid = False
while not valid:
    try:
        edat = int(input("Introdueix l'edat: "))
        valid = True  # només s'executa si int() ha tingut èxit
    except ValueError:
        print("L'edat ha de ser un número.")
```

**Com funciona:**
1. `valid = False` → el bucle comença
2. Python intenta `int(input(...))`
3. Si té èxit → `valid = True` → el bucle s'atura
4. Si falla → salta a `except`, imprimeix l'avís, **`valid` segueix sent `False`** → el bucle continua

**Clau:** `valid = True` està dins el `try`, després de la línia que pot fallar. Si falla, mai s'executa.

---

## 8. VALIDACIÓ DE STRINGS BUITS

```python
# Forma correcta — pythònica:
while not nom:
    nom = input("Introdueix el nom: ")

while not ciutat:
    ciutat = input("Introdueix la ciutat: ")
```

**Per què funciona `not nom`?** A Python, un string buit `""` es comporta com `False`. Per tant `not ""` és `True`, i el bucle continua. Quan l'usuari escriu alguna cosa, `not "David"` és `False`, i el bucle s'atura.

---

## 9. FUNCIÓ `demanar_contacte()` — Versió final robusta

```python
def demanar_contacte():
    nom = ""
    ciutat = ""

    while not nom:
        nom = input("Introdueix el nom de la persona a afegir: ")

    valid = False
    while not valid:
        try:
            edat = int(input("Introdueix l'edat: "))
            valid = True
        except ValueError:
            print("L'edat ha de ser un número.")

    while not ciutat:
        ciutat = input("Introdueix la ciutat: ")

    contacte_nou = {
        "nom": nom,
        "edat": edat,
        "ciutat": ciutat,
    }
    return contacte_nou
```

**Aquesta funció:**
- No accepta noms ni ciutats buits
- No accepta edats que no siguin números enters
- Aguanta qualsevol nombre d'intents incorrectes sense petar

---

## 10. PATRÓ CONSOLIDAT — Validació robusta

```
while not valid:
    try:
        # operació que pot fallar
        valid = True
    except ErrorEspecífic:
        # avisar i tornar a intentar
```

Aquest patró apareixerà arreu: formularis web, APIs, scripts d'automatització, lectures de fitxers.

---

## 11. GIT — Push a GitHub

### Conceptes nous

| Concepte | Significat |
|----------|-----------|
| **Repositori remot** | Còpia del repositori allotjada a un servidor (GitHub) |
| `git remote add origin URL` | Connecta el repositori local amb el remot |
| `git branch -M main` | Assegura que la branca principal es diu `main` |
| `git push -u origin main` | Puja el codi al servidor per primera vegada |
| `git push` | Puja els canvis (totes les vegades següents) |

### Primera vegada — connectar i pujar

```bash
git remote add origin https://github.com/usuari/repositori.git
git branch -M main
git push -u origin main
```

### Totes les vegades següents

```bash
git add *
git commit -m "missatge descriptiu"
git push
```

El `-u origin main` de la primera vegada ja no cal — Git recorda on ha de pujar.

### Personal Access Token

GitHub ja no accepta la contrasenya normal per fer `push`. Cal un **Personal Access Token**:

1. GitHub → foto de perfil → **Settings**
2. **Developer settings** → **Personal access tokens** → **Tokens (classic)**
3. **Generate new token (classic)**
4. Marca el checkbox **`repo`**
5. Copia el token — GitHub no te'l tornarà a mostrar mai més
6. Quan `git push` demani la contrasenya → enganxa el token

---

## 12. MARKDOWN — Sintaxi bàsica

Markdown és el format estàndard per a documentació tècnica, README de GitHub i notes.

| Sintaxi | Resultat |
|---------|---------|
| `# Títol` | Títol gran (H1) |
| `## Subtítol` | Subtítol (H2) |
| `**text**` | **negreta** |
| `*text*` | *cursiva* |
| `` `codi` `` | `codi inline` |
| ` ```python ` | Bloc de codi amb sintaxi |
| `- element` | Llista amb punts |
| `1. element` | Llista numerada |

---

## 13. ERRORS COMUNS

| Error | Causa | Solució |
|-------|-------|---------|
| `FileNotFoundError` | Fitxer no existeix | `try/except FileNotFoundError` → `agenda = []` |
| `try/except` sense `while` | Només cobreix el primer intent | Combinar amb `while not valid` |
| `except Exception` genèric | Amaga bugs propis | Sempre capturar l'error específic |
| `while nom == ""` | Funciona però no és pythònic | `while not nom` |
| Push sense token | GitHub rebutja contrasenya normal | Crear Personal Access Token |

---

## 14. TAULA DE SEGUIMENT

| Skill | Nivell | Evidència | Proper pas |
|-------|--------|-----------|------------|
| Python — Variables | 5/10 | Aplicades amb autonomia en múltiples scripts | — |
| Python — Tipus | 6/10 | Casting fluid, detecció proactiva de tipus a JSON | — |
| Python — Condicions | 5/10 | Aplicades autònomament i combinades | Combinació complexa |
| Python — Bucles | 7/10 | `enumerate` amb `start=1`, `while` afegit autònomament | Llistes per comprensió |
| Python — Llistes | 7/10 | Llistes de diccionaris, accés encadenat, refactorització | Llistes per comprensió |
| Python — Funcions | 7/10 | `return`, Single Responsibility, paràmetres vs globals | Funcions amb valors per defecte |
| Python — Diccionaris | 5/10 | Accés encadenat, llistes de diccionaris, cerca per clau | Diccionaris niats |
| Python — Fitxers | 5/10 | `try/except` per lectura i escriptura, gestió robusta | Modes avançats |
| Python — JSON | 4/10 | `json.load`, `json.dump`, `ensure_ascii`, `indent` | JSON amb APIs |
| Python — Errors | 5/10 | `try/except` específic, `while` + `try/except` combinats | Errors personalitzats |
| Terminal | 5/10 | Navegació autònoma | Permisos i pipes |
| Git | 6/10 | Push a GitHub, Personal Access Token, flux complet | Branques |
| Web | 2/10 | HTML bàsic | DevTools |
| Seguretat | 1/10 | Nocions | Laboratori futur |
| OSINT | 3/10 | Google ops | Automatitzar |

---

## DEURES PENDENTS

- **`README.md`:** crear fitxer de documentació al repositori amb sintaxi Markdown bàsica i fer `git push`
- **Investigar `requests`:** llegir què és la llibreria `requests` de Python i per a què serveix (sense instal·lar ni escriure codi — només entendre la idea)

---

*Fitxer generat automàticament per Claude — Tutor de Programació i Ciberseguretat*
