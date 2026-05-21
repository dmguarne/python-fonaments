# Apunts — Sessió 3
## Llistes, operador mòdul i depuració
**Data:** 21/05/2026

---

## 1. REPÀS — Operador mòdul `%`

L'operador `%` fa la divisió i retorna el **residu** (el que sobra).

```python
10 % 2  → 0   # parell: no sobra res
7 % 2   → 1   # senar: sobra 1
```

**Per saber si un número és parell:**
```python
if numero % 2 == 0:
    print("És parell")
```

Un número parell dividit entre 2 sempre té residu 0. Per tant `% 2 == 0` és la condició correcta.

---

## 2. REPÀS — Variables acumuladores

Una variable acumuladora suma progressivament al llarg d'un bucle.

```python
# ❌ Incorrecte — sempre assigna 1, no acumula:
parells = + 1

# ✅ Correcte — suma 1 al valor actual:
parells = parells + 1
```

**Per què funciona:** `parells = parells + 1` llegeix el valor actual de `parells`, li suma 1, i guarda el resultat a la mateixa variable.

---

## 3. REPÀS — Refactorització: treure codi innecessari

Quan multipliques dos `int`, el resultat ja és `int`. No cal fer casting:

```python
# ❌ Redundant:
if int(valor * numero) % 2 == 0:

# ✅ Net:
if (valor * numero) % 2 == 0:
```

**Refactorització:** millorar el codi sense canviar el que fa.

---

## 4. REPÀS — Números màgics

Un **número màgic** és un valor literal posat directament al codi sense explicació.

```python
# ❌ Número màgic — si el range canvia, el càlcul falla:
senars = 10 - parells

# ✅ Millor — el valor es calcula a partir de dades reals:
senars = len(llista) - parells
```

**Regla:** evita números màgics. El codi ha de funcionar encara que canviïn els paràmetres.

---

## 5. LLISTES

Una llista és una **col·lecció ordenada de valors** dins una sola variable.

```python
fruites = ["poma", "taronja", "plàtan"]
```

### Crear una llista buida

```python
llista = []
```

### Accedir per índex

Els índexs comencen a **0**:

```python
fruites[0]   # → "poma"
fruites[1]   # → "taronja"
fruites[2]   # → "plàtan"
```

### Índexs negatius

Compten des del final:

```python
fruites[-1]  # → "plàtan" (últim)
fruites[-2]  # → "taronja" (penúltim)
```

### `len()` — nombre d'elements

```python
len(fruites)  # → 3
```

**Accedir a l'últim element sense saber la mida:**
```python
fruites[len(fruites) - 1]  # equivalent a fruites[-1]
```

### `.append()` — afegir elements

```python
fruites.append("raïm")
# ara fruites = ["poma", "taronja", "plàtan", "raïm"]
```

### `.remove()` — eliminar elements

```python
fruites.remove("taronja")
# ara fruites = ["poma", "plàtan", "raïm"]
```

Si l'element no existeix, dona `ValueError`.

---

## 6. RECÓRRER LLISTES AMB BUCLES

### Iterar per valor (quan no necessites l'índex)

```python
for nom in llista:
    print(nom)
```

### Iterar per índex (quan necessites la posició)

```python
for i in range(len(llista)):
    print(f"{i + 1}. {llista[i]}")
```

**Regla general:**
| Necessito | Faig servir |
|-----------|-------------|
| Només el valor | `for element in llista` |
| L'índex o posició | `for i in range(len(llista))` |

**La variable `i`** és una convenció per a comptadors numèrics. Podria dir-se `x`, `n` o qualsevol nom. Python la crea automàticament quan comença el `for`.

---

## 7. L'OPERADOR `in`

Comprova si un valor és dins una col·lecció. Retorna `True` o `False`.

```python
"poma" in fruites   # → True
"mango" in fruites  # → False
```

**Simplificació important:**

```python
# ❌ Redundant:
if resultat == True:

# ✅ Pythònic:
if resultat:
```

Quan una variable ja és `True` o `False`, no cal comparar-la amb `== True`.

---

## 8. BUG CLÀSSIC — El bucle que sobreescriu

**Problema:** un bucle que actualitza una variable en cada iteració pot sobreescriure el resultat correcte.

```python
# ❌ Bug — l'última iteració sempre sobreescriu:
for i in range(len(llista)):
    if llista[i] == cerca:
        resultat = "Trobat."
    else:
        resultat = "No trobat."  # sobreescriu si l'últim element no coincideix
```

**Solució:** inicialitzar amb el valor per defecte i només canviar quan es troba:

```python
# ✅ Correcte:
resultat = False
for i in range(len(llista)):
    if llista[i] == cerca:
        resultat = True

if resultat:
    print("Trobat.")
else:
    print("No trobat.")
```

---

## 9. PROJECTE — llistes.py

Script complet que gestiona una llista de noms:

```python
## Crear una llista buida
## Demanar 3 noms a l'usuari amb input() i afegir-los a la llista
## Mostrar quants noms hi ha a la llista
## Mostrar el primer i l'últim nom

llista = []
for i in range(3):
    llista.append(input("Escriu un nom propi: "))

print(f"La llista té {len(llista)} elements.")
print(f"El primer element és '{llista[0]}'.")
print(f"L'últim element és '{llista[-1]}'.")

print("La llista completa és:")
for i in range(len(llista)):
    print(f"{i + 1}. {llista[i]}")

cerca = input("Cerca un nom a la llista: ")
resultat = False
for i in range(len(llista)):
    if llista[i] == cerca:
        resultat = True

if resultat:
    print("Trobat.")
else:
    print("No trobat.")
```

---

## 10. GIT — Bones pràctiques consolidades

```bash
# Sempre amb -m i missatge descriptiu:
git commit -m "Afegir gestió de llistes amb cerca i numeració"

# Mai:
git commit    # obre l'editor, és incòmode
git commit -m "canvis"   # missatge inútil
```

**Bon missatge de commit:** descriu *què* has fet, no *que has fet coses*.

---

## 11. ERRORS COMUNS

| Error | Causa | Solució |
|-------|-------|---------|
| Acumulador no suma | `parells = + 1` | `parells = parells + 1` |
| Bug de sobreescriptura | `else` dins el bucle de cerca | Inicialitzar amb `False`, canviar només quan es troba |
| Índex fora de rang | Accedir a `llista[3]` en una llista de 3 | Índexs van de `0` a `len-1` |
| `if resultat == True` | Redundant | `if resultat:` és suficient |
| Número màgic | Valor literal que pot canviar | Usar `len()` o variables de configuració |

---

## 12. TAULA DE SEGUIMENT

| Skill | Nivell | Evidència |
|-------|--------|-----------|
| Python — Variables | 5/10 | Aplicades amb autonomia |
| Python — Tipus | 5/10 | Casting fluid |
| Python — Condicions | 5/10 | Aplicades autònomament |
| Python — Bucles | 6/10 | `for`, `while`, acumuladors, bug de sobreescriptura resolt |
| Python — Llistes | 4/10 | Creació, accés, append, recorregut, cerca |
| Terminal | 5/10 | Navegació autònoma |
| Git | 4/10 | Commits regulars amb missatges descriptius |

---

## DEURES PENDENTS

Afegir al `llistes.py` una quarta funcionalitat: permetre a l'usuari **eliminar** un nom de la llista.

- Si el nom existeix → elimina'l i mostra la llista actualitzada
- Si no existeix → ho indica

**Investiga:** mètode `.remove()` de les llistes Python.

Després: `git add` i `git commit -m "missatge descriptiu"`.

---

*Fitxer generat automàticament per Claude — Tutor de Programació i Ciberseguretat*
