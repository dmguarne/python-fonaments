# Apunts — Sessió 2
## Bucles `for`, Git i Terminal
**Data:** 21/05/2026

---

## 1. REPÀS — Bucle `while`

El bucle `while` repeteix un bloc de codi **mentre es compleixi una condició**.

```python
edat = int(input("Escriu la teva edat i prem Enter: "))
while edat < 0 or edat > 120:
    print("Edat no vàlida.")
    edat = int(input("Torna a introduir la teva edat i prem Enter: "))
print("Edat acceptada")
```

**Per què funciona la indentació aquí?**

El sagnat no és decoració — és **estructura lògica visible**. Tot el que va indentat dins el `while` **depèn jeràrquicament** d'aquella condició. Si la condició és certa, s'executa. Si no, es salta.

```
while condició:        ← la porta
    bloc de dins       ← s'executa si la porta és oberta
bloc de fora           ← s'executa sempre, al final
```

**Error clàssic:** oblidar indentar el bloc de dins. Python donarà `IndentationError`.

---

## 2. BUCLE `for`

### Diferència entre `while` i `for`

| Bucle | Quan s'usa |
|-------|------------|
| `while` | Quan no saps quantes vegades s'ha de repetir |
| `for` | Quan iteres sobre una col·lecció o rang conegut |

**Analogia:** imagina una bossa amb 5 taronges.
- `while` → *"agafa taronges mentre n'hi hagi"*
- `for` → *"agafa cada taronja, una per una, fins que no en quedi cap"*

### Sintaxi bàsica

```python
fruites = ["poma", "taronja", "plàtan"]

for fruita in fruites:
    print(fruita)
```

**Sortida:**
```
poma
taronja
plàtan
```

El `for` agafa cada element de la llista, el desa temporalment a `fruita`, i executa el bloc indentat.

---

## 3. `range()` — Generar seqüències de números

`range()` genera una seqüència d'enters sense haver de crear una llista a mà.

```python
for numero in range(1, 6):
    print(numero)
```

**Sortida:**
```
1
2
3
4
5
```

⚠️ **IMPORTANT:** `range(1, 6)` va de l'**1 al 5**. El límit superior **sempre s'exclou**.

| Crida | Genera |
|-------|--------|
| `range(5)` | 0, 1, 2, 3, 4 |
| `range(1, 6)` | 1, 2, 3, 4, 5 |
| `range(1, 11)` | 1, 2, 3, 4, 5, 6, 7, 8, 9, 10 |

---

## 4. F-STRINGS AMB EXPRESSIONS

Dins una f-string, entre `{}` pots posar **qualsevol expressió Python**, no només variables. No cal `str()`.

```python
# ✅ Correcte — expressió directa dins {}
print(f"7 x {numero} = {7 * numero}")

# ❌ Incorrecte — str() és redundant i les cometes trenquen la f-string
print(f"7 x {numero} = str(7 * numero)")
```

**Error comú:** posar cometes dins la f-string per delimitar l'expressió. Les cometes tanquen la f-string i el codi falla.

---

## 5. EXERCICI — Taula de multiplicar

### Versió simple (taula del 7)

```python
for numero in range(1, 11):
    print(f"7 x {numero} = {7 * numero}")
```

**Sortida:**
```
7 x 1 = 7
7 x 2 = 14
...
7 x 10 = 70
```

### Versió autònoma (qualsevol número, amb validació)

```python
valor = int(input("Introdueix un número del 1 al 10 i prem Enter: "))
while valor < 1 or valor > 10:
    print("El número ha d'estar entre 1 i 10")
    valor = int(input("Introdueix un número del 1 al 10 i prem Enter: "))
for numero in range(1, 11):
    print(f"{valor} x {numero} = {valor * numero}")
```

**Conceptes combinats:**
- `input()` per capturar el valor
- `while` per validar que estigui en rang
- `for` + `range` per iterar de l'1 al 10
- f-string per formatar la sortida

---

## 6. GIT — Control de versions

### Què és Git?

Git és l'**eina** que fa seguiment de tots els canvis del teu codi. El **repositori** és el lloc on es guarda aquest historial.

Analogia: Git és com rodar una pel·lícula. Cada `commit` és una escena gravada i guardada per sempre.

### 4 conceptes fonamentals

| Concepte | Significat |
|----------|-----------|
| **Repositori** | La carpeta que Git vigila |
| **commit** | Una "foto" del codi en un moment concret |
| **staging area** | La sala d'espera: tries quins fitxers vols fotografiar |
| **branca (branch)** | Una línia de desenvolupament independent |

### El flux bàsic (sempre el mateix)

```
fas canvis  →  git add  →  git commit
```

1. **`git add`** → poses els fitxers a la staging area (els "actors a l'escena")
2. **`git commit`** → graves l'escena amb un missatge descriptiu

---

## 7. COMANDES GIT ESSENCIALS

### Inicialitzar un repositori

```bash
git init
```

Crea un repositori buit a la carpeta actual. Git comença a vigilar-la.

### Veure l'estat

```bash
git status
```

Mostra:
- Fitxers **no seguits** (en vermell) → Git els veu però no els registra
- Fitxers a la **staging area** (en verd) → preparats per al commit
- Si l'arbre de treball està net → tot está fotografiat

### Afegir fitxers a la staging area

```bash
git add nom_fitxer.py    # un fitxer concret
git add *                # tots els fitxers de la carpeta
```

### Fer un commit

```bash
git commit -m "Missatge descriptiu del que has fet"
```

El missatge ha de ser clar i útil. D'aquí a 6 mesos has de poder entendre què va passar en aquest commit.

**Exemple de bon missatge:** `"Afegir validació d'edat al script de presentació"`
**Exemple de mal missatge:** `"canvis"`, `"coses"`, `"aaa"`

### Veure l'historial de commits

```bash
git log
```

---

## 8. PRIMERA SESSIÓ GIT — Pas a pas

```bash
# 1. Anar a la carpeta del projecte
cd ~/Projectes

# 2. Inicialitzar el repositori
git init

# 3. Veure l'estat (fitxers en vermell = no seguits)
git status

# 4. Afegir tots els fitxers
git add *

# 5. Veure l'estat (fitxers en verd = a la staging area)
git status

# 6. Fer el primer commit
git commit -m "Exercicis de la primera sessió"

# 7. Verificar que tot està net
git status
# → "l'arbre de treball està net"
```

---

## 9. ERRORS COMUNS

| Error | Causa | Solució |
|-------|-------|---------|
| `IndentationError` | Codi no sagnat dins `for` o `while` | 4 espais o Tab davant del codi |
| Cometes dins f-string | `f"text {valor 'x'}"`  | No posar cometes dins `{}` |
| `range` incorrecte | `range(1, 10)` quan vols fins a 10 | `range(1, 11)` — el límit s'exclou |
| `fatal: no és un repositori` | Executar `git commit` fora de la carpeta | `cd ~/Projectes` primer |
| Missatge de commit buit | `git commit` sense `-m` | Sempre afegir `-m "missatge"` |

---

## 10. TAULA DE SEGUIMENT

| Skill | Nivell | Evidència |
|-------|--------|-----------|
| Python — Variables | 5/10 | Aplicades amb autonomia |
| Python — Tipus | 5/10 | Casting fluid |
| Python — Condicions | 5/10 | Aplicades autònomament |
| Python — Bucles | 4/10 | `for` i `while` funcionant |
| Terminal | 5/10 | Navegació i errors resolts sols |
| Git | 3/10 | Primer commit real |

---

## 11. DEURES PENDENTS

Modifica el `bucles.py` afegint, **després** de mostrar la taula de multiplicar, un recompte de quants números de la taula són **parells** i quants són **senars**.

**Pista:** en Python hi ha un operador que retorna el **residu** d'una divisió. Investiga quin és i com funciona. Amb aquest operador pots saber si un número és parell o senar.

---

*Fitxer generat automàticament per Claude — Tutor de Programació i Ciberseguretat*
