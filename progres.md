# PROGRÉS — Tutor Programació i Ciberseguretat

## PERFIL
- **Nom:** David
- **Nivell assignat:** PRINCIPIANT
- **Objectiu:** Curiositat i feina
- **Hores setmanals:** 10
- **Risc detectat:** Tutorial hell — tendència a consumir sense construir

---

## TAULA DE SEGUIMENT

| Skill | Nivell | Evidència | Proper pas |
|-------|--------|-----------|------------|
| Python — Variables | 5/10 | Aplicades amb autonomia en múltiples scripts | Funcions |
| Python — Tipus | 5/10 | Casting fluid i sense errors | Diccionaris |
| Python — Condicions | 5/10 | Aplicades autònomament i combinades | Combinació complexa |
| Python — Bucles | 6/10 | Acumuladors, bug de sobreescriptura detectat i resolt autònomament | Bucles amb diccionaris |
| Python — Llistes | 4/10 | Creació, accés, append, recorregut, cerca, índexs negatius | `.remove()`, diccionaris |
| Terminal | 5/10 | Navegació autònoma, errors resolts sols | Permisos i pipes |
| Git | 4/10 | Commits regulars amb missatges descriptius, coneixement de staging area | Push a GitHub |
| Web | 2/10 | HTML bàsic | DevTools |
| Seguretat | 1/10 | Nocions | Laboratori futur |
| OSINT | 3/10 | Google ops | Automatitzar |

---

## SESSIÓ 1 — Resum

**Data:** 20/05/2026

**Contingut treballat:**
- Variables i tipus bàsics a Python
- Casting: str(), int(), float()
- Concatenació i f-strings
- input() per capturar dades de l'usuari
- Condicions: if / elif / else
- Indentació obligatòria a Python
- Instal·lació VS Code
- Navegació terminal: cd, mkdir
- Reparació del .bashrc corromput

**Projecte construït:**
- `presentacio.py` — script interactiu que demana dades a l'usuari i imprimeix una presentació amb condició d'edat

**Errors principals:**
- Confondre TypeError amb error de sintaxi
- Ordre incorrecte en assignació (int(edat) = input() en lloc de edat = int(input()))
- Dos punts al lloc incorrecte en condicions

**Observació del tutor:**
Ha après condicions sense explicació prèvia. Bona capacitat d'inferència. Cal consolidar l'hàbit de provar abans de preguntar.

---

## SESSIÓ 2 — Resum

**Data:** 21/05/2026

**Contingut treballat:**
- Repàs bucle `while` i lògica d'indentació
- Bucle `for`: sintaxi, iteració sobre llistes
- `range()`: generació de seqüències, límit superior exclòs
- F-strings amb expressions directes dins `{}`
- Git: conceptes fonamentals (repositori, commit, staging area, branch)
- Git: comandes `init`, `status`, `add *`, `commit -m`
- Primer commit real del repositori `Projectes`

**Projecte construït:**
- `bucles.py` — taula de multiplicar amb input de l'usuari, validació `while` i `for` + `range`

**Errors principals:**
- Cometes dins f-string (tanca la cadena prematurament)
- `git commit` executat fora de la carpeta del repositori (`fatal: no és un repositori`)

**Transferència autònoma destacada:**
Ha afegit validació `while` al `bucles.py` sense que el tutor ho demanés. Aplicació espontània de coneixement de la sessió anterior. ⭐

**Observació del tutor:**
Progressió sòlida. Bona capacitat d'inferència i transferència. Cal continuar consolidant l'hàbit d'intentar abans de preguntar — en aquesta sessió ha mirat la solució abans d'intentar-ho del tot.

---

## SESSIÓ 3 — Resum

**Data:** 21/05/2026

**Contingut treballat:**
- Operador mòdul `%`: residu de la divisió, detecció de parells i senars
- Variables acumuladores: `parells = parells + 1` vs `parells = + 1`
- Refactorització: eliminar `int()` redundant en operacions entre enters
- Números màgics: per què cal evitar-los i com substituir-los per `len()`
- Llistes: creació buida `[]`, accés per índex, índexs negatius `[-1]`
- Mètodes de llista: `.append()`, `.remove()`
- `len()` per obtenir la mida d'una llista
- Recórrer llistes: per valor (`for element in llista`) vs per índex (`for i in range(len(llista))`)
- Operador `in` per comprovar si un element és dins una col·lecció
- Simplificació pythònica: `if resultat:` en lloc de `if resultat == True:`
- Bug clàssic de sobreescriptura en bucles de cerca — detectat i resolt autònomament

**Projecte construït:**
- `llistes.py` — gestió d'una llista de noms: afegir, mostrar, numerar, cercar

**Errors principals:**
- Bug de sobreescriptura al bucle de cerca (`else` dins el bucle sobreescrivia el resultat correcte)
- `llista[]` en lloc de `llista = []` per crear una llista buida

**Transferència autònoma destacada:**
Ha detectat i resolt el bug de sobreescriptura sense ajuda del tutor. Ha simplificat `if resultat == True:` a `if resultat:` de forma espontània. ⭐⭐

**Observació del tutor:**
Sessió molt sòlida. Millora notable en autonomia de depuració. El raonament sobre per què triar opció B (càlcul de senars per deducció) demostra pensament algorítmic real. Pendent consolidar el concepte de número màgic.

---

## DEURES PENDENTS

- Afegir al `llistes.py` funcionalitat per **eliminar** un nom de la llista amb `.remove()`:
  - Si el nom existeix → elimina'l i mostra la llista actualitzada
  - Si no existeix → ho indica
- `git add` i `git commit -m "missatge descriptiu"` de tot (llistes.py + apunts_sessio3.md)

---

## CURRÍCULUM

### FASE 1 — Fonaments Python + Terminal *(en curs)*
| Setmana | Contingut | Estat |
|---------|-----------|-------|
| 1-2 | Variables, tipus, funcions, condicions | ✅ Completat |
| 2-3 | Bucles `for` i `while`, `range`, f-strings avançades | ✅ Completat |
| 3-4 | Llistes, diccionaris, fitxers | 🔄 En curs |
| 4-5 | Terminal Linux, Git (push a GitHub) | 🔄 En curs |
| 6-7 | Funcions, mòduls, errors, debugging | ⏳ Pendent |
| 7-8 | Scraping, automatització bàsica | ⏳ Pendent |

### FASE 2 — Web i APIs *(pendent)*
### FASE 3 — Sistemes i Linux *(pendent)*
### FASE 4 — Ciberseguretat *(pendent)*
### FASE 5 — OSINT *(pendent)*
### FASE 6 — IA Aplicada *(pendent)*

---

## INSTRUCCIONS PER AL TUTOR

Al iniciar sessió:
1. Llegir aquest fitxer
2. Reprendre des dels deures pendents
3. Actualitzar la taula de seguiment
4. Generar nou progres.md al final
