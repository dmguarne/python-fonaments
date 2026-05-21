# PROGRÉS — Tutor Programació i Ciberseguretat

## PERFIL
- **Nom:** David
- **Nivell assignat:** PRINCIPIANT**→INTERMEDI** (transició en curs)
- **Objectiu:** Curiositat i feina
- **Hores setmanals:** 10
- **Risc detectat:** Tutorial hell — tendència a consumir sense construir *(risc reduït: 5 sessions consecutives construint codi real)*

---

## TAULA DE SEGUIMENT

| Skill | Nivell | Evidència | Proper pas |
|-------|--------|-----------|------------|
| Python — Variables | 5/10 | Aplicades amb autonomia en múltiples scripts | — |
| Python — Tipus | 5/10 | Casting fluid i sense errors | — |
| Python — Condicions | 5/10 | Aplicades autònomament i combinades | Combinació complexa |
| Python — Bucles | 6/10 | Acumuladors, bugs resolts autònomament | `enumerate` |
| Python — Llistes | 7/10 | Llistes de diccionaris, accés encadenat, refactorització | Llistes per comprensió |
| Python — Funcions | 6/10 | `return`, Single Responsibility, codi autodocumentat, variables globals detectades | Funcions amb valors per defecte |
| Python — Diccionaris | 5/10 | Accés encadenat, llistes de diccionaris, cerca per clau | Diccionaris niats |
| Terminal | 5/10 | Navegació autònoma | Permisos i pipes |
| Git | 5/10 | Commits regulars amb missatges descriptius, hàbit consolidat | Push a GitHub |
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

## SESSIÓ 4 — Resum

**Data:** 21/05/2026

**Contingut treballat:**
- Repàs bug de sobreescriptura aplicat a `.remove()` — resolt autònomament
- Principi DRY (Don't Repeat Yourself): identificació de codi duplicat
- Funcions: `def`, paràmetres, crida, convenció d'ordre al fitxer
- Refactorització de `llistes.py`: bloc repetit convertit en funció `enumerar(llista)`
- Diccionaris: creació, accés per clau, afegir, modificar, `.items()`, recorregut
- Diferència conceptual llista vs diccionari: posició vs nom del camp
- Comportament temporal del diccionari: reflecteix l'estat en cada moment d'execució

**Projectes construïts:**
- `llistes.py` refactoritzat — funció `enumerar()`, esborrat amb patró bandera
- `contactes.py` — diccionari d'una persona, accés, modificació, recorregut amb `.items()`

**Errors principals:**
- Bug de sobreescriptura al `.remove()` (resolt autònomament sense ajuda del tutor)
- Funció definida al mig del fitxer en lloc de dalt de tot (detectat i corregit)

**Transferència autònoma destacada:**
Ha deduït per si sol per què existeixen les funcions a partir del problema del codi duplicat. Ha resolt el bug de sobreescriptura aplicant el patró après a la sessió anterior sense que el tutor li ho recordés. ⭐⭐⭐

**Observació del tutor:**
Sessió excel·lent. Autonomia creixent i molt notable. El salt qualitatiu més important fins ara: no només aplica el que se li explica, sinó que **generalitza patrons** i els reutilitza en contextos nous. Preparat per al primer exercici que combina llistes + diccionaris + funcions.

---

## SESSIÓ 5 — Resum

**Data:** 21/05/2026

**Contingut treballat:**
- Revisió i depuració de `agenda.py` (deures de la sessió 4)
- Detecció i correcció de variable global dins funció — passar-ho com a paràmetre
- Accés encadenat a llistes de diccionaris: `agenda[i]["clau"]`
- `return` vs `print`: diferència conceptual i pràctica
- Principi Single Responsibility: cada funció fa una cosa
- Tensió DRY vs Single Responsibility — resolució per disseny
- Codi autodocumentat: el nom de la funció com a documentació
- `enumerate()` — introduït per investigació autònoma

**Projecte construït:**
- `agenda.py` final — llista de diccionaris, dues funcions (`mostrar_persona` amb `return`, `mostrar_agenda`), cerca per nom amb patró bandera

**Errors principals:**
- `if trobat == False` en lloc de `if not trobat` (corregit)
- Variable global `agenda` dins `mostrar_persona` sense paràmetre (detectat i corregit)
- `return(f"...")` amb parèntesis innecessaris (corregit)

**Transferència autònoma destacada:**
Ha raonat autònomament la tensió entre DRY i Single Responsibility. Ha defensat decisions de disseny amb argumentació tècnica real ("depèn de per a què serveixi"). ⭐⭐⭐

**Observació del tutor:**
Sessió de maduresa. El salt no és de sintaxi sinó conceptual: ha après a pensar en responsabilitats i a prendre decisions de disseny conscients. Progressió que justifica revisar el nivell assignat cap a intermedi en les properes sessions.

---

## DEURES PENDENTS

Refactoritza `agenda.py` substituint `for i in range(len(agenda))` per `enumerate()` a les dues funcions i al bucle de cerca.

Investiga la sintaxi de `enumerate()` i aplica-la. Després: `git commit -m "missatge descriptiu"`.

---

## CURRÍCULUM

### FASE 1 — Fonaments Python + Terminal *(en curs)*
| Setmana | Contingut | Estat |
|---------|-----------|-------|
| 1-2 | Variables, tipus, condicions | ✅ Completat |
| 2-3 | Bucles `for` i `while`, `range`, f-strings avançades | ✅ Completat |
| 3-4 | Llistes, diccionaris, funcions | ✅ Completat |
| 4-5 | Terminal Linux, Git (push a GitHub) | 🔄 En curs |
| 6-7 | Fitxers, mòduls, errors, debugging | ⏳ Pendent |
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
