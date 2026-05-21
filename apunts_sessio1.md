# Apunts — Sessió 1
## Programació Python i Terminal
**Data:** 20/05/2026

---

## 1. VARIABLES

Una variable és una **caixa amb etiqueta** que guarda un valor a la memòria.

```python
nom = "David"
edat = 39
altura = 1.70
```

**Regles:**
- El nom va a l'esquerra
- El valor va a la dreta
- Mai al revés

---

## 2. TIPUS DE DADES

| Tipus | Exemple | Per a què serveix |
|-------|---------|------------------|
| `str` | `"David"` | Text |
| `int` | `39` | Nombres enters |
| `float` | `1.70` | Nombres decimals |
| `bool` | `True / False` | Condicions |

**Python és de tipatge dinàmic:** no cal declarar el tipus, Python l'endevina sol. Però els tipus **existeixen i importen**.

---

## 3. CASTING — Convertir entre tipus

Convertir un valor d'un tipus a un altre s'anomena **casting**.

| Funció | Converteix a | Exemple |
|--------|-------------|---------|
| `str()` | Text | `str(39)` → `"39"` |
| `int()` | Nombre enter | `int("39")` → `39` |
| `float()` | Nombre decimal | `float("1.7")` → `1.7` |

**Per què és important?**
No es poden sumar tipus incompatibles:

```python
# ❌ Això falla:
"Edat: " + 39

# ✅ Això funciona:
"Edat: " + str(39)
```

**L'error que dona si no fas casting:**
```
TypeError: can only concatenate str (not "int") to str
```

`TypeError` = has intentat fer una operació amb un **tipus inadequat**.

---

## 4. CONCATENACIÓ DE STRINGS

Unir text amb el símbol `+`:

```python
nom = "David"
"Em dic " + nom  # → "Em dic David"
```

⚠️ Els dos valors han de ser del mateix tipus (`str`).

---

## 5. F-STRINGS — La forma professional

Les **f-strings** permeten incloure variables dins un text sense `+` ni `str()`.

```python
nom = "David"
edat = 39
altura = 1.70

print(f"Em dic {nom}, tinc {edat} anys i faig {altura} metres d'altura.")
```

**Com funciona:**
- Posa una `f` davant de les cometes
- Les variables van entre `{ }`
- Python les converteix automàticament

---

## 6. INPUT() — Capturar dades de l'usuari

`input()` atura el programa i espera que l'usuari escrigui alguna cosa.

```python
nom = input("Escriu el teu nom i prem Enter: ")
```

**⚠️ Important:** `input()` sempre retorna un `str`, fins i tot si l'usuari escriu un número.

Per això cal combinar-lo amb casting quan necessitem números:

```python
# String (text):
nom = input("Escriu el teu nom: ")

# Enter:
edat = int(input("Escriu la teva edat: "))

# Decimal:
altura = float(input("Escriu la teva altura: "))
```

**Llegir de dins cap a fora:**
1. `input()` demana el valor → retorna string
2. `int()` el converteix a enter
3. Es guarda a la variable `edat`

---

## 7. CONDICIONS — if / elif / else

Les condicions permeten executar codi diferent segons un valor.

**Sintaxi:**
```python
if condició:
    # codi si la condició és certa
elif altra_condició:
    # codi si la segona condició és certa
else:
    # codi si cap condició és certa
```

**Regles importants:**
- Cada `if`, `elif`, `else` acaba amb **`:`**
- El codi de dins va **indentat** (4 espais)
- La indentació no és opcional a Python — és sintaxi

**Operadors de comparació:**
| Operador | Significat |
|----------|-----------|
| `<` | Menor que |
| `>` | Major que |
| `<=` | Menor o igual |
| `>=` | Major o igual |
| `==` | Igual |
| `!=` | Diferent |

**Operadors lògics:**
| Operador | Significat |
|----------|-----------|
| `and` | Les dues condicions han de ser certes |
| `or` | N'hi ha prou que una sigui certa |
| `not` | Nega la condició |

**Exemple:**
```python
if edat < 18:
    print("Ets menor d'edat")
elif edat >= 18 and edat < 65:
    print("Ets adult")
else:
    print("Ets jubilat")
```

---

## 8. PROJECTE — presentacio.py

Script interactiu que demana dades a l'usuari i imprimeix una presentació.

```python
nom = input("Escriu el teu nom i prem Enter: ")
edat = int(input("Escriu la teva edat i prem Enter: "))
altura = float(input("Escriu la teva altura i prem Enter: "))
gos = input("Escriu el nom del teu gos i prem Enter: ")
edat_gos = int(input("Escriu l'edat del teu gos i prem Enter: "))

if edat < 18:
    print("Ets menor d'edat")
elif edat >= 18 and edat < 65:
    print("Ets adult")
else:
    print("Ets jubilat")

print(f"Em dic {nom}, tinc {edat} anys i faig {altura} metres d'altura. El meu gos es diu {gos} i té {edat_gos} anys")
```

**Per executar-lo:**
```bash
python3 presentacio.py
```

---

## 9. TERMINAL — Comandes bàsiques

| Comanda | Funció |
|---------|--------|
| `cd ~` | Anar al directori personal |
| `cd Projectes` | Entrar a la carpeta Projectes |
| `mkdir Projectes` | Crear una carpeta |
| `ls` | Llistar fitxers i carpetes |
| `pwd` | Mostrar on ets |
| `python3 fitxer.py` | Executar un script Python |
| `nano ~/.bashrc` | Editar fitxer de configuració del terminal |
| `source ~/.bashrc` | Recarregar la configuració del terminal |

**Obrir VS Code des de terminal:**
```bash
cd ~/Projectes
code .
```
El punt `.` significa "obre la carpeta actual".

**Instal·lar programes a Ubuntu:**
```bash
sudo apt install nom_paquet
```
- `sudo` = executa com a administrador
- `apt` = gestor de paquets d'Ubuntu
- `install` = l'acció
- `nom_paquet` = el que vols instal·lar

---

## 10. ERRORS COMUNS

| Error | Causa | Solució |
|-------|-------|---------|
| `TypeError` | Tipus inadequat en una operació | Fer casting amb `str()`, `int()`, `float()` |
| Ordre incorrecte | `int(edat) = input()` | Sempre variable = valor: `edat = int(input())` |
| Falta `:` | `if edat < 18` sense dos punts | Afegir `:` al final: `if edat < 18:` |
| Indentació | Codi no sangrat dins `if` | 4 espais o Tab davant del codi |
| Majúscules | `Sudo` en lloc de `sudo` | Linux distingeix majúscules i minúscules |

---

## DEURES PENDENTS

Afegir al `presentacio.py` un **bucle `while`** que validi que l'edat introduïda és entre 0 i 120. Si l'usuari introdueix un valor fora d'aquest rang, el programa ha de tornar a demanar-lo.

**Pensa:** quin tipus de bucle usaries quan no saps quantes vegades s'ha de repetir?
