# Apunts — Sessió 5
## Llistes de diccionaris, `return` i disseny de funcions
**Data:** 21/05/2026

---

## 1. REPÀS — Revisió dels deures (`agenda.py`)

### El que funcionava bé
- Llista de diccionaris creada correctament
- Funció `mostrar_agenda` amb bucle i numeració
- Patró bandera (`trobat = False`) aplicat autònomament
- Commits amb missatges descriptius

### Errors detectats i corregits

**Error 1 — Condició redundant:**
```python
# ❌ Redundant:
if trobat == False:

# ✅ Pythònic:
if not trobat:
```

**Error 2 — Variable global dins una funció:**
```python
# ❌ Perillós — depèn d'una variable global:
def mostrar_persona(persona):
    print(f"... {agenda[persona]["nom"]} ...")  # agenda no és paràmetre

# ✅ Correcte — tot el que necessita la funció entra per paràmetre:
def mostrar_persona(agenda, persona):
    print(f"... {agenda[persona]["nom"]} ...")
```

**Per què és un problema dependre de variables globals?**
Si `agenda` existís només dins d'una altra funció, `mostrar_persona` deixaria de funcionar. Les funcions han de ser **autosuficients**: tot el que necessiten ha d'entrar per paràmetre.

---

## 2. ACCÉS ENCADENAT A LLISTES DE DICCIONARIS

### La sintaxi

```python
agenda[i]["nom"]
```

**Com llegir-ho, de dins cap a fora:**

1. `agenda[i]` → accedeix a la posició `i` de la llista → retorna un **diccionari**
2. `["nom"]` → accedeix a la clau `"nom"` d'aquell diccionari → retorna el **valor**

**Regla general:** cada parell de claudàtors accedeix a un nivell. El resultat de l'expressió anterior és el que s'usa per al nivell següent.

```python
# Accés en un pas:
agenda[0]           # → {"nom": "David", "edat": 39, "ciutat": "Barcelona"}

# Accés en dos passos:
agenda[0]["nom"]    # → "David"
agenda[0]["edat"]   # → 39
```

---

## 3. DISSENY DE FUNCIONS — Single Responsibility

### El principi

Cada funció ha de tenir **una sola responsabilitat**. Si una funció fa dues coses, probablement hauria de ser dues funcions.

### Exemple aplicat

Tenim dues tasques diferenciades:
- Formatat d'un contacte individual → `mostrar_persona`
- Recorregut i numeració de tota l'agenda → `mostrar_agenda`

Si les barreges en una sola funció, quan vulguis mostrar un sol contacte (a la cerca) hauràs de duplicar el format.

---

## 4. `return` — Retornar valors des d'una funció

### Diferència entre `print` i `return`

| | `print` | `return` |
|---|---------|----------|
| Què fa | Mostra el valor per pantalla | Envia el valor al lloc on s'ha cridat la funció |
| Es pot reutilitzar? | No | Sí |
| Qui decideix com mostrar-ho? | La funció | Qui crida la funció |

### Sintaxi

```python
def mostrar_persona(contacte):
    return f"{contacte["nom"]} | {contacte["edat"]} anys | {contacte["ciutat"]}"
```

⚠️ `return` **no** necessita parèntesis:
```python
return f"..."    # ✅ correcte
return(f"...")   # funciona però sembla una crida a funció — evita-ho
```

### Per què usar `return` en lloc de `print`?

Quan una funció retorna un valor en lloc d'imprimir-lo directament, **qui la crida decideix com usar-lo**:

```python
# Mostrar sense número (cerca):
print(mostrar_persona(agenda[i]))

# Mostrar amb número (agenda completa):
print(f"{i + 1}. {mostrar_persona(agenda[i])}")

# Guardar en una variable per processar després:
text = mostrar_persona(agenda[i])
```

La mateixa funció serveix per a tres usos diferents. Si hagués fet `print` directament, cap d'aquests seria possible sense duplicar codi.

---

## 5. TENSIÓ DRY vs SINGLE RESPONSIBILITY

### El dilema

De vegades eliminar duplicació (DRY) entra en conflicte amb tenir funcions amb responsabilitat única.

**Exemple:** volem mostrar contactes amb numeració a l'agenda i sense numeració a la cerca. Dues opcions:

**Opció A — Una sola funció que ho fa tot:**
```python
def mostrar_persona(contacte, numero=None):
    # fa dues coses → viola Single Responsibility
```

**Opció B — Funció que retorna el format, cada crida afegeix el que necessita:**
```python
def mostrar_persona(contacte):
    return f"{contacte["nom"]} | {contacte["edat"]} anys | {contacte["ciutat"]}"

# Amb número:
print(f"{i + 1}. {mostrar_persona(agenda[i])}")

# Sense número:
print(mostrar_persona(agenda[i]))
```

**Conclusió:** l'Opció B respecta els dos principis. La funció fa una cosa (formatat), i qui la crida decideix com presentar-ho.

---

## 6. CODI AUTODOCUMENTAT

El nom d'una funció ha de descriure la seva intenció. Això es diu **codi autodocumentat**.

```python
# ❌ Cal llegir tot per entendre:
print(f"{agenda[i]['nom']} | {agenda[i]['edat']} anys | {agenda[i]['ciutat']}")

# ✅ El nom explica la intenció:
print(mostrar_persona(agenda[i]))
```

Quan tornis al codi d'aquí a 6 mesos, el segon és llegible en un segon. El primer requereix anàlisi.

---

## 7. PROJECTE FINAL — `agenda.py`

```python
## Definició de la funció que formata un contacte:
def mostrar_persona(contacte):
    return f"{contacte["nom"]} | {contacte["edat"]} anys | {contacte["ciutat"]}"

## Imprimeix cada diccionari numerat:
def mostrar_agenda(agenda):
    for i in range(len(agenda)):
        print(f"{i + 1}. {mostrar_persona(agenda[i])}")

## Crear la llista de contactes:
persona01 = {
    "nom": "David",
    "edat": 39,
    "ciutat": "Barcelona",
}

persona02 = {
    "nom": "Maria",
    "edat": 24,
    "ciutat": "Girona",
}

persona03 = {
    "nom": "Antoni",
    "edat": 55,
    "ciutat": "Mataró",
}

agenda = [persona01, persona02, persona03]

## Mostrar l'agenda:
print("Agenda:")
mostrar_agenda(agenda)

## Cerca per nom:
cerca = input("Introdueix un nom a buscar: ")
trobat = False

for i in range(len(agenda)):
    if agenda[i]["nom"] == cerca:
        trobat = True
        print(f"{i + 1}. {mostrar_persona(agenda[i])}")

if not trobat:
    print("Persona no trobada.")
```

---

## 8. `enumerate()` — Per investigar

Python té una forma més elegant de recórrer una llista quan necessites l'índex i el valor alhora:

```python
# Forma habitual:
for i in range(len(agenda)):
    print(f"{i + 1}. {agenda[i]}")

# Amb enumerate:
for i, contacte in enumerate(agenda):
    print(f"{i + 1}. {contacte}")
```

`enumerate()` retorna **dues variables** en cada iteració: l'índex i l'element. Evita haver d'escriure `agenda[i]` i fa el codi més llegible.

---

## 9. ERRORS COMUNS

| Error | Causa | Solució |
|-------|-------|---------|
| `if trobat == False` | Comparació redundant | `if not trobat` |
| Variable global dins funció | La funció depèn de context extern | Passar-ho com a paràmetre |
| `return(f"...")` | Parèntesis innecessaris | `return f"..."` |
| `print(f"{funcio()}")` | F-string redundant quan no hi ha text addicional | `print(funcio())` |
| Nom de variable que no reflecteix el tipus | `contacte` per un índex numèric | `i` per índexs, noms descriptius per dades |

---

## 10. CONCEPTES CLAU DE LA SESSIÓ

**Accés encadenat:** `llista[i]["clau"]` — cada claudàtor accedeix a un nivell de la estructura de dades.

**`return` vs `print`:** `return` fa la funció reutilitzable en múltiples contextos. `print` bloqueja la decisió de com usar el valor.

**Single Responsibility:** cada funció fa una cosa. Si fa dues, probablement haurien de ser dues funcions.

**Codi autodocumentat:** el nom de la funció explica la intenció millor que cap comentari.

**Disseny conscient:** "depèn de per a què serveixi" no és indecisió — és arquitectura. Les decisions de disseny depenen dels requisits.

---

## 11. TAULA DE SEGUIMENT

| Skill | Nivell | Evidència | Proper pas |
|-------|--------|-----------|------------|
| Python — Variables | 5/10 | Aplicades amb autonomia en múltiples scripts | — |
| Python — Tipus | 5/10 | Casting fluid i sense errors | — |
| Python — Condicions | 5/10 | Aplicades autònomament i combinades | Combinació complexa |
| Python — Bucles | 6/10 | Acumuladors, bugs resolts autònomament | `enumerate` |
| Python — Llistes | 7/10 | Llistes de diccionaris, accés encadenat | Llistes per comprensió |
| Python — Funcions | 6/10 | `return`, Single Responsibility, codi autodocumentat | Funcions amb valors per defecte |
| Python — Diccionaris | 5/10 | Accés encadenat, llistes de diccionaris, cerca per clau | Diccionaris niats |
| Terminal | 5/10 | Navegació autònoma | Permisos i pipes |
| Git | 5/10 | Commits regulars amb missatges descriptius | Push a GitHub |
| Web | 2/10 | HTML bàsic | DevTools |
| Seguretat | 1/10 | Nocions | Laboratori futur |
| OSINT | 3/10 | Google ops | Automatitzar |

---

## DEURES PENDENTS

Refactoritza `agenda.py` substituint `for i in range(len(agenda))` per `enumerate()` a les dues funcions i al bucle de cerca.

Investiga la sintaxi de `enumerate()` i aplica-la. Després: `git commit -m "missatge descriptiu"`.

---

*Fitxer generat automàticament per Claude — Tutor de Programació i Ciberseguretat*
