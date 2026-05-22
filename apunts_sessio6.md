# Apunts — Sessió 6
## Fitxers, JSON i Persistència de dades
**Data:** 22/05/2026

---

## 1. REPÀS — `enumerate()` aplicat a `agenda.py`

`enumerate()` retorna **dues variables** en cada iteració: l'índex i l'element. Evita haver d'escriure `llista[i]` i fa el codi més llegible.

```python
# Forma antiga:
for i in range(len(agenda)):
    print(f"{i + 1}. {agenda[i]}")

# Amb enumerate (start=1 per no començar a 0):
for i, contacte in enumerate(agenda, start=1):
    print(f"{i}. {mostrar_persona(contacte)}")
```

**Per què `start=1`?** Per defecte `enumerate` comença a 0. `start=1` fa que la numeració sigui natural per a l'usuari.

---

## 2. EL PROBLEMA DE LA PERSISTÈNCIA

Tots els programes que hem fet fins ara tenen un problema fonamental: **quan tanques el programa, tot desapareix.** L'agenda, els noms, tot. Cada vegada que executes el script, comences de zero.

Els fitxers solucionen això. Permeten **persistir dades** entre execucions.

**Analogia:** la memòria RAM del programa és com la pissarra d'una classe — quan s'acaba la sessió, s'esborra. Un fitxer és com un quadern — el tanques, el tornes a obrir, i les notes segueixen allà.

---

## 3. FITXERS — Conceptes bàsics

Python treballa amb fitxers en tres passos sempre iguals:

```
obrir → fer alguna cosa → tancar
```

### Modes d'obertura

| Mode | Significat | Si el fitxer no existeix |
|------|-----------|--------------------------|
| `"r"` | Llegir | Error |
| `"w"` | Escriure (sobreescriu **tot**) | El crea |
| `"a"` | Afegir al final | El crea |

**Diferència clau entre `"w"` i `"a"`:**
- `"w"` sobreescriu tot el fitxer. Si tenies 100 línies i n'escrius 1, et queden 1.
- `"a"` afegeix al final sense tocar el que ja hi ha. Útil per a logs i registres.

### Sintaxi `with open`

```python
# Forma antiga (cal tancar manualment):
fitxer = open("agenda.txt", "r")
fitxer.close()

# Forma moderna — SEMPRE usa aquesta:
with open("agenda.txt", "r") as fitxer:
    # codi aquí
# es tanca sol en acabar el bloc
```

El `with` garanteix que el fitxer es tanca sempre, fins i tot si hi ha un error.

### Què és la variable `fitxer`?

```python
with open("agenda.json", "r") as fitxer:
```

`open()` retorna un **objecte fitxer** — una connexió oberta al fitxer del disc. `fitxer` és el nom que li dones a aquesta connexió per poder-la usar dins el bloc `with`.

**Analogia:** `open()` marca un número de telèfon. `fitxer` és la línia oberta. Tot el que fas dins el `with` és la conversa.

---

## 4. EL MODEL MENTAL FONAMENTAL — Fitxer vs Memòria

Aquesta és la distinció més important per treballar amb fitxers:

| | Fitxer del disc | Variable a memòria |
|---|---|---|
| **Estat** | Permanent | Temporal |
| **Quan s'usa** | Per llegir i guardar | Per operar i modificar |
| **Es modifica directament?** | **No** | Sí |

**Python no edita fitxers "in situ".** El flux sempre és:

```
1. llegir fitxer → carregar a memòria
2. modificar a memòria (el fitxer del disc no canvia)
3. escriure de tornada al fitxer → sobreescriure
```

**En codi:**

```python
# Pas 1 — Llegir
with open("agenda.json", "r") as fitxer:
    agenda = json.load(fitxer)

# Pas 2 — Modificar a memòria (cap fitxer obert)
agenda.append(contacte_nou)

# Pas 3 — Guardar
with open("agenda.json", "w") as fitxer:
    json.dump(agenda, fitxer, ensure_ascii=False, indent=4)
```

**Regla pràctica:** dos blocs `with open` — un per llegir (`"r"`), un per escriure (`"w"`). Entre mig, tota la lògica.

---

## 5. SERIALITZACIÓ — El problema dels tipus

Un fitxer `.txt` només entén **text**. Però una llista de diccionaris Python és una estructura de dades en memòria, no text.

Si intentes escriure directament:
```python
fitxer.write(agenda)  # ❌ TypeError!
```

`write()` només accepta `str`. Calen eines de **serialització**: convertir estructures Python a text i viceversa.

**Serialització:** convertir una estructura de dades (llista, diccionari) a un format de text que es pugui guardar i recuperar.

---

## 6. JSON

**JSON** (JavaScript Object Notation) és el format estàndard d'intercanvi de dades a internet. Quan una API et respon, quasi sempre és JSON.

La seva estructura és molt similar als diccionaris Python:

```json
[
    {
        "nom": "David",
        "edat": 39,
        "ciutat": "Barcelona"
    },
    {
        "nom": "Maria",
        "edat": 24,
        "ciutat": "Girona"
    }
]
```

### Importar el mòdul

```python
import json
```

`import` li diu a Python "carrega aquesta caixa d'eines addicional". `json` és un mòdul de la biblioteca estàndard — ve amb Python, no cal instal·lar res.

### Els quatre mètodes

| Mètode | Direcció | Treballa amb |
|--------|----------|-------------|
| `json.dump()` | Python → fitxer JSON | Fitxers |
| `json.load()` | Fitxer JSON → Python | Fitxers |
| `json.dumps()` | Python → string JSON | Strings |
| `json.loads()` | String JSON → Python | Strings |

**Regla mnemotècnica:** la `s` final significa *string*. Sense `s` treballa amb fitxers.

### Guardar una llista al JSON

```python
import json

agenda = [{"nom": "David", "edat": 39, "ciutat": "Barcelona"}]

with open("agenda.json", "w") as fitxer:
    json.dump(agenda, fitxer, ensure_ascii=False, indent=4)
```

**Paràmetres opcionals de `json.dump`:**
- `ensure_ascii=False` → guarda accents i caràcters especials llegibles (`ó` en lloc de `\u00f3`)
- `indent=4` → formata el JSON amb indentació de 4 espais (llegible per humans)

### Llegir un JSON a Python

```python
with open("agenda.json", "r") as fitxer:
    agenda = json.load(fitxer)
# agenda ara és una llista de diccionaris Python normal
```

---

## 7. TIPUS DE DADES AL JSON

**Atenció:** `input()` sempre retorna `str`. Si guardes l'edat directament d'un `input()`, al JSON quedarà `"edat": "39"` (string) en lloc de `"edat": 39` (enter).

```python
# ❌ Edat com a string:
edat = input("Introdueix l'edat: ")

# ✅ Edat com a enter:
edat = int(input("Introdueix l'edat: "))
```

Importa si vols fer càlculs o ordenar per edat. No importa si només mostres el valor.

### Script per corregir tipus en un JSON existent

```python
import json

with open("agenda.json", "r") as fitxer:
    agenda = json.load(fitxer)

for i, contacte in enumerate(agenda):
    contacte["edat"] = int(contacte["edat"])

with open("agenda.json", "w") as fitxer:
    json.dump(agenda, fitxer, ensure_ascii=False, indent=4)
```

**Concepte important:** `contacte` dins el bucle no és una còpia — és una **referència** al diccionari original dins la llista. Quan el modifiques, estàs modificant directament `agenda`.

---

## 8. VARIABLES GLOBALS DINS FUNCIONS

Una funció que usa una variable definida fora d'ella **depèn de context extern**. Això és perillós:

```python
# ❌ Perillós — agenda no és paràmetre:
def afegir_contacte():
    agenda.append(demanar_contacte())  # agenda ve de fora

# ✅ Correcte — agenda entra per paràmetre:
def afegir_contacte(agenda):
    agenda.append(demanar_contacte())
```

**Regla:** tot el que una funció necessita ha d'entrar per paràmetre. Les funcions han de ser autosuficients.

---

## 9. RECURSIÓ I STACK OVERFLOW

**Recursió:** quan una funció es crida a si mateixa.

```python
def eliminar_contacte():
    # ...
    if not trobat:
        eliminar_contacte()  # ← crida recursiva
```

**El problema:** cada crida recursiva crea una nova "capa" a la memòria. Si l'usuari introdueix noms incorrectes moltes vegades, la memòria se satura. Això s'anomena **stack overflow**.

**La solució:** substituir la recursió per un `while` quan no hi ha un límit clar de profunditat:

```python
# ❌ Recursió sense límit:
def eliminar_contacte():
    eliminar = input("Introdueix el nom: ")
    if not trobat:
        eliminar_contacte()  # risc de stack overflow

# ✅ While amb bandera:
def eliminar_contacte(agenda):
    repetir = True
    trobat = False
    while repetir and not trobat:
        eliminar = input("Introdueix el nom: ")
        # ...cerca...
        if not trobat:
            resposta = input("Vols cercar un altre nom? S/N ")
            if resposta != "S" and resposta != "s":
                repetir = False
```

**Quan usar recursió:** quan el problema té una profunditat natural i limitada (arbres, directoris, algoritmes divideix-i-venceràs). Per a bucles simples, sempre `while`.

---

## 10. PROJECTE FINAL — `agenda_persistent.py`

Script complet amb menú interactiu, persistència JSON, afegir i esborrar contactes:

```python
import json

def mostrar_persona(contacte):
    return f"{contacte["nom"]} | {contacte["edat"]} anys | {contacte["ciutat"]}"

def mostrar_agenda(agenda):
    print("Agenda:\n")
    for i, contacte in enumerate(agenda, start=1):
        print(f"{i}. {mostrar_persona(contacte)}")

def demanar_contacte():
    nom = input("Introdueix el nom de la persona a afegir: ")
    edat = int(input("Introdueix l'edat: "))
    ciutat = input("Introdueix la ciutat: ")
    return {"nom": nom, "edat": edat, "ciutat": ciutat}

def afegir_contacte(agenda):
    afegir = input("Vols afegir un nou contacte? (S/N)? ")
    while afegir == "S" or afegir == "s":
        agenda.append(demanar_contacte())
        mostrar_agenda(agenda)
        afegir = input("Vols afegir un nou contacte? (S/N)? ")
    else:
        print("Gràcies per la teva col·laboració")

def eliminar_contacte(agenda):
    repetir = True
    trobat = False
    while repetir and not trobat:
        eliminar = input("Introdueix el nom: ")
        for i, contacte in enumerate(agenda, start=1):
            if contacte["nom"] == eliminar:
                trobat = True
                agenda.remove(contacte)
                print("Contacte eliminat.")
        if not trobat:
            repetir = input("Contacte no trobat. Vols cercar un altre nom? S/N ")
            if repetir != "S" and repetir != "s":
                repetir = False

## Llegir l'agenda:
with open("agenda.json", "r") as fitxer:
    agenda = json.load(fitxer)

mostrar_agenda(agenda)

## Menú principal:
accio = "0"
while accio != "3":
    accio = input("Escull què vols fer:\n"
    "1. Afegir contacte\n"
    "2. Esborrar contacte\n"
    "3. Res\n")
    if accio == "1":
        afegir_contacte(agenda)
    elif accio == "2":
        eliminar_contacte(agenda)
    elif accio != "1" and accio != "2" and accio != "3":
        print("Input incorrecte")

if accio == "3":
    print("Gràcies per la teva col·laboració")

mostrar_agenda(agenda)

## Guardar:
with open("agenda.json", "w") as fitxer:
    json.dump(agenda, fitxer, ensure_ascii=False, indent=4)
```

---

## 11. ERRORS COMUNS

| Error | Causa | Solució |
|-------|-------|---------|
| `TypeError: write() argument must be str` | Intentar escriure una llista directament al fitxer | Usar `json.dump()` per serialitzar |
| Dades perdudes en reiniciar | Guardar amb `"w"` dins el bucle | Guardar **fora** del bucle, un cop acabat |
| Edats com a string al JSON | `input()` sempre retorna `str` | `int(input(...))` per capturar enters |
| Accents com `\u00f3` al JSON | `ensure_ascii=True` per defecte | Afegir `ensure_ascii=False` a `json.dump` |
| Tres blocs `with open` | Confondre fitxer amb memòria | Dos blocs: un `"r"` i un `"w"`. Lògica entremig |
| Variable global dins funció | Funció depèn de context extern | Passar-la com a paràmetre |
| Recursió sense límit | Stack overflow amb moltes crides | Substituir per `while` amb bandera |
| `accio = int` o `accio = str` | Assigna la funció, no un valor | Inicialitzar amb un valor: `accio = "0"` |
| `if x != "A" or x != "B"` | Sempre `True` — cap valor pot ser A i B alhora | Usar `and`: `if x != "A" and x != "B"` |

---

## 12. CONCEPTES CLAU DE LA SESSIÓ

**Persistència:** capacitat de conservar dades entre execucions d'un programa. Sense fitxers, tot es perd en tancar.

**Serialització:** convertir estructures de dades Python (llistes, diccionaris) a un format de text que es pugui guardar (JSON) i recuperar.

**Model mental fitxer/memòria:** mai es modifica un fitxer directament. Sempre: llegir → memòria → modificar → guardar.

**JSON:** format estàndard d'intercanvi de dades. Estructura idèntica als diccionaris i llistes Python. Fonamental per a APIs i web.

**Referència vs còpia:** quan iteres una llista de diccionaris i modifiques un element, estàs modificant l'original — no una còpia.

**Recursió vs while:** la recursió és poderosa però perillosa sense límit. Per a bucles simples, `while` amb bandera és sempre més segur.

**Stack overflow:** saturació de la pila de crides per recursió excessiva. El nom d'una web molt famosa no és casualitat.

---

## 13. TAULA DE SEGUIMENT

| Skill | Nivell | Evidència | Proper pas |
|-------|--------|-----------|------------|
| Python — Variables | 5/10 | Aplicades amb autonomia en múltiples scripts | — |
| Python — Tipus | 6/10 | Casting fluid, detecció proactiva de tipus a JSON | — |
| Python — Condicions | 5/10 | Aplicades autònomament i combinades | Combinació complexa |
| Python — Bucles | 7/10 | `enumerate` amb `start=1`, `while` afegit autònomament | Llistes per comprensió |
| Python — Llistes | 7/10 | Llistes de diccionaris, accés encadenat, refactorització | Llistes per comprensió |
| Python — Funcions | 7/10 | `return`, Single Responsibility, paràmetres vs globals | Funcions amb valors per defecte |
| Python — Diccionaris | 5/10 | Accés encadenat, llistes de diccionaris, cerca per clau | Diccionaris niats |
| Python — Fitxers | 4/10 | `with open`, modes `r/w`, model mental memòria/disc | Gestió d'errors amb fitxers |
| Python — JSON | 4/10 | `json.load`, `json.dump`, `ensure_ascii`, `indent` | JSON amb APIs |
| Terminal | 5/10 | Navegació autònoma | Permisos i pipes |
| Git | 5/10 | Commits regulars amb missatges descriptius | Push a GitHub |
| Web | 2/10 | HTML bàsic | DevTools |
| Seguretat | 1/10 | Nocions | Laboratori futur |
| OSINT | 3/10 | Google ops | Automatitzar |

---

## DEURES PENDENTS (completats)

✅ Afegir funcionalitat d'esborrar contacte per nom
✅ Menú interactiu amb opcions afegir / esborrar / sortir
✅ Funcions autosuficients amb `agenda` com a paràmetre
✅ Recursió substituïda per `while` amb bandera

**Propera sessió:** `try/except` per gestionar errors inesperats (què passa si `agenda.json` no existeix?) i push a GitHub.

---

*Fitxer generat automàticament per Claude — Tutor de Programació i Ciberseguretat*
