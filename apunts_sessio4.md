# Apunts — Sessió 4
## Funcions i Diccionaris
**Data:** 21/05/2026

---

## 1. REPÀS — Bug de sobreescriptura (aplicat a `.remove()`)

El bug de sobreescriptura apareix quan poses un `else` **dins** un bucle de cerca. En cada iteració que no coincideix, sobreescriu el resultat correcte.

```python
# ❌ Bug — sobreescriu el resultat en cada iteració:
for nom in range(len(llista)):
    if llista[nom] == esborrar:
        llista.remove(esborrar)
    else:
        print("El nom no existeix a la llista")  # s'executa per cada element que NO coincideix
```

**Solució:** inicialitzar una variable bandera fora del bucle i fer el `if/else` **fora** del bucle:

```python
# ✅ Correcte:
existeix = False
for nom in range(len(llista)):
    if llista[nom] == esborrar:
        existeix = True

if existeix:
    llista.remove(esborrar)
    enumerar(llista)  # mostrar la llista actualitzada
else:
    print("El nom no existeix a la llista")
```

**Regla general:** el `if/else` que dona el resultat final d'una cerca sempre va **fora** del bucle.

---

## 2. CODI DUPLICAT — Per què és un problema

Quan un mateix bloc apareix dues vegades al codi, és un senyal d'alerta:

- Si cal canviar el comportament, has de canviar-ho en **dos llocs** (i és fàcil oblidar-ne un)
- El codi és més llarg i difícil de llegir
- Viola el principi **DRY**: *Don't Repeat Yourself*

**Solució:** convertir el bloc repetit en una **funció**.

---

## 3. FUNCIONS

### Què és una funció?

Un bloc de codi amb nom que pots cridar tantes vegades com vulguis, des de qualsevol punt del programa.

**Analogia:** la rutina de matí. En lloc d'escriure "llevar-te, dutxar-te, fer cafè" cada dia, dius "fes la rutina de matí" i ja està.

### Sintaxi bàsica

```python
def nom_de_la_funcio():
    # codi que fa la funció
```

- `def` — paraula reservada per definir una funció
- El nom segueix les mateixes regles que les variables (minúscules, sense espais, `_` per separar paraules)
- Els `:` i la indentació — obligatoris, igual que sempre

### Cridar la funció

```python
nom_de_la_funcio()
```

Simplement el nom amb parèntesis. Python executa tot el bloc de dins.

### Funcions amb paràmetres

Un paràmetre és una variable temporal que la funció rep quan se la crida:

```python
def saludar(nom):
    print(f"Hola, {nom}!")

saludar("David")   # → Hola, David!
saludar("Maria")   # → Hola, Maria!
```

`nom` només existeix **dins** la funció. Cada crida li passa un valor diferent.

### Funcions que retornen un valor

```python
def doblar(numero):
    return numero * 2

resultat = doblar(5)   # resultat = 10
```

`return` envia un valor de tornada al lloc on s'ha cridat la funció. Sense `return`, la funció retorna `None`.

### Tres preguntes per dissenyar una funció

Abans d'escriure una funció, fes-te aquestes preguntes:

| Pregunta | Resposta possible |
|----------|------------------|
| Quin nom li poso? | Ha de descriure el que fa (`enumerar`, `cercar`, `esborrar`) |
| Necessita rebre dades externes? | Si sí → afegeix paràmetres |
| Ha de retornar alguna cosa? | Si només imprimeix → no cal `return` |

---

## 4. CONVENCIÓ — On van les funcions al fitxer

Python permet definir funcions en qualsevol lloc del fitxer. Però la **convenció professional** és:

```
[definicions de funcions]   ← a dalt de tot
[codi principal]            ← a baix
```

Així qualsevol que llegeixi el codi sap on buscar cada cosa.

**Per què funciona tot i estar "mal ordenat"?** Perquè Python llegeix tot el fitxer abans d'executar-lo. Però llegibilitat i convenció importen tant com que funcioni.

---

## 5. EXEMPLE — Funció `enumerar` al `llistes.py`

### Problema detectat

El bloc per mostrar la llista numerada apareixia **dues vegades**:

```python
# Aparició 1 — mostrar la llista inicial
for i in range(len(llista)):
    print(f"{i + 1}. {llista[i]}")

# ... codi ...

# Aparició 2 — mostrar la llista després d'esborrar
for i in range(len(llista)):
    print(f"{i + 1}. {llista[i]}")
```

### Solució: convertir en funció

```python
# Definició — a dalt de tot del fitxer
def enumerar(llista):
    for i in range(len(llista)):
        print(f"{i + 1}. {llista[i]}")

# Crides — on calgui
enumerar(llista)   # mostra la llista inicial
# ... codi ...
enumerar(llista)   # mostra la llista actualitzada
```

### `llistes.py` complet i refactoritzat

```python
## Definim la funció que imprimeix la llista numerada
def enumerar(llista):
    for i in range(len(llista)):
        print(f"{i + 1}. {llista[i]}")

## Crear una llista buida i demanar 3 noms
llista = []
for i in range(3):
    llista.append(input("Escriu un nom propi: "))

print(f"La llista té {len(llista)} elements.")
print(f"El primer element és '{llista[0]}'.")
print(f"L'últim element és '{llista[-1]}'.")

print("La llista completa és:")
enumerar(llista)

## Cercar un nom
cerca = input("Cerca un nom a la llista: ")
resultat = False
for i in range(len(llista)):
    if llista[i] == cerca:
        resultat = True

if resultat:
    print("Trobat.")
else:
    print("No trobat.")

## Esborrar un nom
esborrar = input("Introdueix un nom per esborrar: ")

existeix = False
for nom in range(len(llista)):
    if llista[nom] == esborrar:
        existeix = True

if existeix:
    llista.remove(esborrar)
    enumerar(llista)
else:
    print("El nom no existeix a la llista")
```

---

## 6. DICCIONARIS

### Diferència amb les llistes

| Estructura | Accés | Quan usar-la |
|------------|-------|-------------|
| Llista | Per posició: `llista[0]` | Quan l'ordre importa i els elements són de la mateixa naturalesa |
| Diccionari | Per nom: `persona["nom"]` | Quan cada camp té nom propi i la posició no importa |

**Regla pràctica:** si dir "el primer element" no té sentit i és millor dir "el nom" o "l'edat", usa diccionari.

### Sintaxi

```python
persona = {
    "nom": "David",
    "edat": 39,
    "ciutat": "Barcelona"
}
```

- Les claus solen ser `str`
- Els valors poden ser qualsevol tipus: `str`, `int`, `float`, `bool`, llista, o fins i tot un altre diccionari
- Cada parella clau-valor separada per `,`

### Accedir a un valor

```python
persona["nom"]    # → "David"
persona["edat"]   # → 39
```

### Afegir o modificar

```python
persona["email"] = "david@mail.com"   # afegeix si la clau no existeix
persona["edat"] = 40                   # modifica si la clau ja existeix
```

La mateixa sintaxi serveix per a les dues operacions. Python comprova si la clau existeix i actua en conseqüència.

### Comprovar si una clau existeix

```python
"nom" in persona       # → True
"telèfon" in persona   # → False
```

L'operador `in` funciona igual que amb les llistes, però comprova **claus**, no valors.

### Recórrer un diccionari

```python
for clau, valor in persona.items():
    print(f"{clau}: {valor}")
```

`.items()` retorna cada parella clau-valor alhora. Les dues variables (`clau`, `valor`) reben cada parella en cada iteració.

---

## 7. EXEMPLE — `contactes.py`

```python
## Crear un diccionari que representi una persona
persona = {
    "nom": "David",
    "edat": 39,
    "ciutat": "Barcelona",
}

## Imprimir cada camp amb una f-string llegible
print(f"La persona es diu {persona['nom']}, té {persona['edat']} anys i viu a {persona['ciutat']}")

## Afegir una clau nova: email
persona["mail"] = "dmguarne@gmail.com"

## Modificar la ciutat per una altra
persona["ciutat"] = "Madrid"

## Imprimir el diccionari sencer recorrent-lo amb .items()
for clau, valor in persona.items():
    print(f"{clau}: {valor}")
```

**Sortida:**
```
La persona es diu David, té 39 anys i viu a Barcelona
nom: David
edat: 39
ciutat: Madrid
mail: dmguarne@gmail.com
```

**Observació important:** la primera línia diu "Barcelona" i la última diu "Madrid". No és un bug — és el comportament esperat. El primer `print` s'executa **abans** de modificar la ciutat. El diccionari reflecteix l'estat en cada moment d'execució.

---

## 8. ERRORS COMUNS

| Error | Causa | Solució |
|-------|-------|---------|
| Bug de sobreescriptura | `else` dins el bucle de cerca/esborrat | Variable bandera fora del bucle, `if/else` fora del bucle |
| Codi duplicat | Copiar el mateix bloc dues vegades | Convertir en funció |
| Funció definida al mig del fitxer | Convenció no respectada | Totes les `def` a dalt de tot |
| `persona[nom]` en lloc de `persona["nom"]` | Falta de cometes a la clau | Les claus string necessiten cometes |
| Confondre modificar i afegir | Sembla que és diferent | Mateixa sintaxi: `diccionari["clau"] = valor` |

---

## 9. CONCEPTES CLAU DE LA SESSIÓ

**DRY (Don't Repeat Yourself):** si un bloc de codi es repeteix, és candidat a convertir-se en funció.

**Reconeixement de patrons:** identificar que el problema d'esborrar és el mateix patró que el problema de cercar (variable bandera, `if/else` fora del bucle). Aquesta habilitat és fonamental en programació.

**Refactorització:** millorar l'estructura del codi sense canviar el que fa. En aquesta sessió: eliminar duplicació convertint el bloc repetit en `enumerar()`.

---

## 10. TAULA DE SEGUIMENT

| Skill | Nivell | Evidència |
|-------|--------|-----------|
| Python — Variables | 5/10 | Aplicades amb autonomia |
| Python — Tipus | 5/10 | Casting fluid |
| Python — Condicions | 5/10 | Aplicades autònomament |
| Python — Bucles | 6/10 | Acumuladors, bugs resolts autònomament |
| Python — Llistes | 6/10 | `.remove()`, cerca, esborrat amb patró bandera |
| Python — Funcions | 4/10 | Definició, paràmetres, crida — primer ús real |
| Python — Diccionaris | 3/10 | Creació, accés, modificació, `.items()` |
| Terminal | 5/10 | Navegació autònoma |
| Git | 5/10 | Commits regulars amb missatges descriptius |

---

## DEURES PENDENTS

Crea un script nou: `agenda.py`

Ha de fer el següent:

1. Crear una **llista de diccionaris** — cada element de la llista és un diccionari amb `nom`, `edat` i `ciutat`
2. Afegir **3 contactes** a la llista (pots posar-hi les dades que vulguis)
3. Mostrar tots els contactes numerats amb una funció `mostrar_agenda(agenda)`
4. Permetre a l'usuari **cercar** un contacte pel nom i mostrar totes les seves dades si el troba
5. `git add` i `git commit -m "missatge descriptiu"`

**Pista conceptual:** si una llista és una col·lecció d'elements, i un diccionari és una persona... una llista de diccionaris és una col·lecció de persones. Exactament el que és una agenda.

---

*Fitxer generat automàticament per Claude — Tutor de Programació i Ciberseguretat*
