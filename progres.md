# PROGRÉS — Tutor Programació i Ciberseguretat

## PERFIL
- **Nom:** David
- **Nivell assignat:** PRINCIPIANT**→INTERMEDI** (transició en curs)
- **Objectiu:** Curiositat i feina
- **Hores setmanals:** 10
- **Risc detectat:** Tutorial hell — tendència a consumir sense construir *(risc eliminat: 8 sessions consecutives construint codi real)*

---

## TAULA DE SEGUIMENT

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
| Python — Errors | 6/10 | `try/except` amb xarxa, estructura correcta dins `try` | Errors personalitzats |
| Python — Strings | 5/10 | Slicing deduït autònomament: `text[2:]` | Mètodes de string |
| requests | 4/10 | GET, `status_code`, `.json()`, variables d'entorn | POST, headers |
| BeautifulSoup | 4/10 | `find`, `find_all`, atributs, cerca dins element | Paginació, scraping avançat |
| Seguretat | 3/10 | Variables d'entorn, consciència de claus exposades, historial Git | `.env` files, secrets management |
| Terminal | 5/10 | Navegació autònoma, `.bashrc`, `export` | Permisos i pipes |
| Git | 6/10 | Push a GitHub, flux complet, commits descriptius | Branques |
| Web | 2/10 | HTML bàsic, inspecció d'elements amb DevTools | DevTools avançat |
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
Sessió excel·lent. Autonomia creixent i molt notable. El salt qualitatiu més important fins ara: no només aplica el que se li explica, sinó que generalitza patrons i els reutilitza en contextos nous. Preparat per al primer exercici que combina llistes + diccionaris + funcions.

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

## SESSIÓ 6 — Resum

**Data:** 22/05/2026

**Contingut treballat:**
- Repàs i aplicació definitiva de `enumerate()` amb `start=1`
- Debat DRY vs Single Responsibility — resolució argumentada autònomament
- Recuperació de `mostrar_persona` per centralitzar el format (DRY aplicat)
- El problema de la persistència: per què les dades desapareixen en tancar el programa
- Fitxers: modes `"r"`, `"w"`, `"a"` i diferències pràctiques
- Sintaxi `with open ... as fitxer` — per què és la forma correcta
- Model mental fonamental: fitxer vs memòria (llegir → memòria → modificar → guardar)
- Serialització: per què no es pot escriure una llista directament a un fitxer
- JSON: estructura, similitud amb diccionaris Python, format estàndard d'APIs
- `import json` — primer ús d'un mòdul de la biblioteca estàndard
- `json.dump()` amb `ensure_ascii=False` i `indent=4`
- `json.load()` per recuperar estructures Python des d'un fitxer
- Tipus de dades al JSON: `input()` retorna `str`, cal `int()` per guardar enters
- Script de correcció de tipus en un JSON existent
- Referència vs còpia: modificar un diccionari dins un bucle modifica l'original
- Variables globals dins funcions: per què son perilloses, solució amb paràmetres
- Recursió i stack overflow: quan usar-la i quan substituir-la per `while`
- Bug lògic `or` vs `and` en condicions de negació múltiple
- Inicialització correcta de variables de control (`accio = "0"` vs `accio = int`)

**Projectes construïts:**
- `agenda_persistent.py` — programa complet amb menú interactiu, afegir i esborrar contactes, persistència JSON, funcions autosuficients
- `refactoritzar_agenda.py` — script de correcció de tipus al JSON existent

**Errors principals:**
- Malentès inicial sobre modificar fitxers directament (resolt amb model mental)
- Tres blocs `with open` en lloc de dos (refactoritzat)
- Variables globals dins funcions (corregit afegint paràmetres)
- Recursió sense límit a `eliminar_contacte` (substituïda per `while` amb bandera)
- `if repetir != "S" or repetir != "s"` — condició sempre `True` (corregit a `and`)
- `accio = int` — assignació de funció en lloc de valor (corregit a `accio = "0"`)

**Transferència autònoma destacada:**
Ha afegit menú interactiu complet sense que el tutor ho demanés. Ha usat recursió per primera vegada de forma espontània. Ha detectat i corregit el bug `or` vs `and` autònomament. Ha construït el script de correcció de tipus completament sol. ⭐⭐⭐

**Observació del tutor:**
Sessió excepcional. Ha entregat els deures i ha construït un programa molt més ambiciós del que se li demanava. La recursió espontània demostra que el pensament algorítmic està madur. Preparat per a `try/except` i push a GitHub.

---

## SESSIÓ 7 — Resum

**Data:** 22/05/2026

**Contingut treballat:**
- Deures verificats: `FileNotFoundError` identificat correctament sense ajuda
- `try/except`: sintaxi bàsica, funcionament, captura d'errors específics
- Múltiples `except` en un sol bloc `try`
- Regla d'or: mai capturar `Exception` genèrica
- Errors comuns i els seus noms: `FileNotFoundError`, `json.JSONDecodeError`, `ValueError`, `PermissionError`, `OSError`
- `try/except` per lectura de fitxers JSON
- `try/except` per escriptura de fitxers JSON
- Patró `while` + `try/except` per validació robusta d'entrades
- Validació de strings buits amb `while not nom` (forma pythònica)
- Funció `demanar_contacte()` completament robusta
- Git remot: `git remote add origin`, `git branch -M main`, `git push -u origin main`
- Personal Access Token de GitHub
- Flux de treball diari amb GitHub: `add` → `commit` → `push`
- Markdown: sintaxi bàsica per a documentació

**Projecte construït:**
- `agenda_persistent.py` versió final robusta — gestió completa d'errors en lectura, escriptura i entrades d'usuari
- `apunts_sessio7.md` — documentació de la sessió en Markdown

**Errors principals:**
- Primer `try/except` sense `while` — només cobria el primer intent (detectat i corregit autònomament)
- `while nom == ""` en lloc de `while not nom` (corregit quan se li va suggerir)

**Transferència autònoma destacada:**
Ha detectat i corregit el bug del `try/except` sense `while` ell sol, abans que el tutor li ho indiqués. Ha fet el push a GitHub de forma autònoma seguint les instruccions. ⭐⭐

**Observació del tutor:**
Sessió sòlida de consolidació. El patró `while` + `try/except` és un dels més importants de Python i l'ha interioritzat bé. El codi de la `demanar_contacte()` final és genuïnament professional. Primer codi públic a internet: fita important. Preparat per a scraping amb `requests`.

---

## SESSIÓ 8 — Resum

**Data:** 26/05/2026

**Contingut treballat:**
- HTTP: protocol client/servidor, verbs GET i POST, codis d'estat (200, 404, 403, 500)
- Objectes: atributs (sense parèntesis) vs mètodes (amb parèntesis)
- `requests`: instal·lació, `requests.get()`, objecte `response`
- `response.status_code`, `response.text`, `response.json()`
- APIs públiques: peticions reals a ISS (Open Notify) i NASA APOD
- Estructura correcta de `try/except` amb xarxa: `if status_code` dins el `try`
- Seguretat: mai hardcodejar API keys al codi
- Variables d'entorn: `export` al `.bashrc`, `os.environ.get()`
- Historial de Git: per què un commit nou no esborra dades sensibles anteriors
- `git config --global credential.helper store` per recordar el token
- BeautifulSoup: instal·lació, `html.parser`, relació amb `requests`
- `soup.title` vs `soup.title.text` — objecte complet vs text pur
- `.find()` i `.find_all()` amb filtres: `class_=`, `title=True`
- Cercar dins un element concret amb `.find()` (no a tota la pàgina)
- Slicing de strings: `text[2:]`, `text[:3]`, `text[1:4]`
- Inspecció d'HTML amb DevTools del navegador per identificar elements

**Projectes construïts:**
- `scraping_01.py` — petició GET a httpbin.org, exploració de `response`
- `scraping_02.py` — API NASA APOD amb `os.environ.get()`, condicional per `media_type`, data
- `scraping_03.py` — scraping de books.toscrape.com: títols i preus de 20 llibres

**Errors principals:**
- API key de la NASA hardcodejada a GitHub (corregida amb variables d'entorn)
- `response = False` com a solució al problema de variable no definida al `except` (resolt movent el `if` dins el `try`)
- `missatge:media` en lloc de `missatge_media` — dos punts en lloc d'igual (detectat per revisió de codi)
- `find_all('a')` sense filtre retornava tots els `<a>` de la pàgina (resolt amb `title=True`)
- Element d'entrada massa específic (`<a>`) que no contenia el preu (resolt pujant al `<article>` pare)

**Transferència autònoma destacada:**
Ha explorat l'estructura de la resposta de l'API abans d'escriure el codi. Ha aplicat slicing `[2:]` per resoldre un problema d'encoding sense que el tutor li ho expliqués. Ha inspeccionat l'HTML autònomament per identificar l'element pare correcte. ⭐⭐⭐

**Observació del tutor:**
Sessió de maduresa tècnica real. Ha passat de scripts locals a parlar amb serveis d'internet i extreure dades de webs reals. La lliçó de seguretat de les API keys és de les que no s'obliden. El slicing deduït autònomament és un indicador clar que el pensament algorítmic està consolidat. Preparat per a entorns virtuals i scraping avançat amb paginació.

---

## DEURES PENDENTS

- Ampliar `scraping_03.py`:
  - Afegir la **puntuació** de cada llibre (`"One"`, `"Two"`... a l'HTML)
  - Guardar resultats a `llibres.json` amb `json.dump` — cada llibre com a diccionari amb `titol`, `preu` i `puntuacio`
  - `git commit` i `git push`
- **Investigar entorns virtuals** (`venv`): per a què serveixen i com es creen (sense implementar encara)

---

## CURRÍCULUM

### FASE 1 — Fonaments Python + Terminal *(en curs)*
| Setmana | Contingut | Estat |
|---------|-----------|-------|
| 1-2 | Variables, tipus, condicions | ✅ Completat |
| 2-3 | Bucles `for` i `while`, `range`, f-strings avançades | ✅ Completat |
| 3-4 | Llistes, diccionaris, funcions | ✅ Completat |
| 4-5 | Fitxers, JSON, persistència | ✅ Completat |
| 5-6 | Terminal Linux, Git (push a GitHub) | ✅ Completat |
| 6-7 | Gestió d'errors (`try/except`), validació robusta | ✅ Completat |
| 7-8 | Scraping, `requests`, BeautifulSoup, APIs reals | ✅ Completat |
| 8-9 | Entorns virtuals, scraping avançat, paginació | ⏳ Pendent |

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
