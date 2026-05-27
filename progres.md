# PROGRÉS — Tutor Programació i Ciberseguretat

## PERFIL
- **Nom:** David
- **Nivell assignat:** PRINCIPIANT**→INTERMEDI** (transició en curs)
- **Objectiu:** Curiositat i feina
- **Hores setmanals:** 10
- **Risc detectat:** Tutorial hell — tendència a consumir sense construir *(risc eliminat: 10 sessions consecutives construint codi real)*

---

## TAULA DE SEGUIMENT

| Skill | Nivell | Evidència | Proper pas |
|-------|--------|-----------|------------|
| Python — Variables | 5/10 | Aplicades amb autonomia en múltiples scripts | — |
| Python — Tipus | 6/10 | Casting fluid, tipus correctes al JSON | — |
| Python — Condicions | 6/10 | Aplicades autònomament i combinades | Combinació complexa |
| Python — Bucles | 8/10 | Paginació amb patró fetch-process-fetch, lògica de condició | — |
| Python — Llistes | 8/10 | Llistes per comprensió aplicades autònomament | Comprensió amb filtre |
| Python — Funcions | 7/10 | Diccionari de conversió, Single Responsibility | Funcions amb valors per defecte |
| Python — Diccionaris | 6/10 | Diccionari com a taula de conversió, accés encadenat | Diccionaris niats |
| Python — Fitxers | 6/10 | Patró llegir→modificar→escriure consolidat | Modes avançats |
| Python — JSON | 7/10 | Gestió de duplicats, patró llegir+escriure robust | JSON amb múltiples APIs |
| Python — Errors | 7/10 | Distinció entre errors propis i errors de llibreria | Errors personalitzats |
| Python — Strings | 5/10 | Slicing, f-strings per URLs dinàmiques | Mètodes de string |
| argparse | 5/10 | Argument `--pagina-inici` amb `type` i `default` | Múltiples arguments, flags |
| requests | 5/10 | Paginació, gestió de codis d'estat, 50 peticions seqüencials | POST, headers |
| BeautifulSoup | 5/10 | Classes múltiples, accés a atributs, cerca dins element | Scraping avançat |
| Entorns virtuals | 5/10 | Entorn nou creat per projecte, `requirements.txt` actualitzat | Gestió avançada |
| Seguretat | 4/10 | Token revocat i renovat ràpidament, consciència de secrets exposats | `.env` files |
| Terminal | 7/10 | `git add -A`, patrons `.gitignore`, reorganització de directoris | Permisos i pipes |
| Git | 7/10 | Moviments de fitxers, `.gitignore` avançat, flux complet | Branques |
| Web | 2/10 | HTML bàsic, classes múltiples, inspecció DevTools | DevTools avançat |
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
- Llistes de diccionaris: estructura, creació, accés encadenat `llista[i]["clau"]`
- Funció que retorna un diccionari: encapsulació de la creació d'un contacte
- Menú interactiu amb `while True` i `break`
- Patró bandera per a l'esborrat: buscar primer, esborrar després
- Fitxers de text: `open()`, modes `'r'`, `'w'`, `'a'`, context manager `with`
- Persistència bàsica: guardar i llegir una llista de noms

**Projecte construït:**
- `agenda.py` — agenda de contactes amb menú interactiu, afegir/mostrar/cercar/esborrar, persistència en fitxer de text

**Errors principals:**
- `agenda[i]` en lloc de `agenda[i]["nom"]` per accedir al nom dins el diccionari
- Indentació incorrecta del `break` (fora del `if` en lloc de dins)

**Transferència autònoma destacada:**
Ha proposat espontàniament guardar els contactes en un fitxer per no perdre'ls en tancar el programa. Ha implementat el menú complet amb totes les opcions sense guia pas a pas. ⭐⭐

**Observació del tutor:**
Primera agenda funcional amb persistència. La proposta espontània de persistència demostra que el pensament va més enllà de l'exercici immediat. Preparat per a JSON i persistència estructurada.

---

## SESSIÓ 6 — Resum

**Data:** 22/05/2026

**Contingut treballat:**
- JSON: format, sintaxi, diferència amb diccionari Python
- `json.dumps()` vs `json.dump()`: string vs fitxer
- `json.loads()` vs `json.load()`: des de string vs des de fitxer
- `ensure_ascii=False` i `indent=4` per a fitxers llegibles
- Migració de `agenda.py` a `agenda_persistent.py` amb JSON
- Deures autònoms: `agenda_persistent_v2.py` amb múltiples contactes i validació

**Projectes construïts:**
- `agenda_persistent.py` — agenda amb persistència JSON
- `agenda_persistent_v2.py` (deures) — versió ampliada amb múltiples contactes, telèfon, recursió per tornar al menú

**Errors principals:**
- `json.load()` sobre fitxer buit retorna error (resolt amb `try/except`)
- Confusió inicial entre `dumps`/`loads` (string) i `dump`/`load` (fitxer)

**Transferència autònoma destacada:**
Ha construït `agenda_persistent_v2.py` amb recursió espontània sense que el tutor ho demanés. Ha afegit camp telèfon i validació d'entrada de forma autònoma. ⭐⭐⭐

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

## SESSIÓ 9 — Resum

**Data:** 26/05/2026

**Contingut treballat:**
- Classes múltiples en HTML: `class="star-rating Three"` són dues classes independents
- BeautifulSoup retorna classes com a llista: `element["class"]` → `["star-rating", "Three"]`
- Diccionari de conversió com a alternativa escalable a cadenes d'`if/elif`
- Tipus de dades al JSON: guardar enters operables, no strings presentacionals
- Paginació: construcció dinàmica de URLs amb f-string
- Patró fetch-process-fetch: petició al final del bucle per condició sempre actualitzada
- `while/else` vs `if/else` fora del bucle per gestionar el final de la paginació
- Eliminació de variables innecessàries (`ordre`) quan el context canvia
- Entorns virtuals (`venv`): creació, activació, instal·lació de llibreries aïllades
- `pip freeze > requirements.txt`: documentar dependències amb l'operador `>`
- `.gitignore`: excloure `entorn/` i fitxers locals de Git
- Fitxers ocults a Linux (comencen per `.`): cal `git add .gitignore` explícitament

**Projecte construït:**
- `scraping_03.py` versió final — 1000 llibres de 50 pàgines amb títol, preu i puntuació numèrica guardats a `llibres.json`
- Entorn virtual configurat amb `requirements.txt` i `.gitignore`

**Errors principals:**
- JSON creixent infinitament per llegir el fitxer existent abans d'afegir (resolt inicialitzant `llibres = []` fora del bucle)
- Petició duplicada a la pàgina 1 (resolt amb patró fetch-process-fetch)
- `response` de la condició obsoleta per petició al principi del bucle (resolt movent-la al final)
- Nom de funció igual que variable interna: `def conversio` + `conversio = {}` (corregit a `equivalencies`)
- Puntuació guardada com a string `"3 estrelles"` en lloc d'enter `3` (corregit)

**Transferència autònoma destacada:**
Ha identificat que la pàgina 1 seguia el mateix patró URL que la resta abans d'assumir un cas especial. Ha eliminat la variable `ordre` autònomament en detectar que ja no era necessària. Ha raonat correctament la lògica del `while/else` sense ajuda. ⭐⭐

**Observació del tutor:**
Sessió de consolidació i salt qualitatiu: de scrapar una pàgina a scrapar una web sencera amb 1000 registres. El patró fetch-process-fetch és un dels més recurrents en programació de xarxa i l'ha interioritzat bé. L'entorn virtual configurat correctament marca l'inici del treball professional. Preparat per a `argparse` i arguments de línia de comandes.

---

## SESSIÓ 10 — Resum

**Data:** 27/05/2026

**Contingut treballat:**
- `argparse`: flux complet — `ArgumentParser()`, `add_argument()`, `parse_args()`, accés a `arguments.nom`
- `type=` i `default=` a `add_argument()`
- Conversió automàtica de guions a guions baixos en noms d'arguments
- Regla: no cal `try/except` sobre el que les llibreries ja gestionen internament
- Llistes per comprensió: sintaxi `[expressió for element in col·lecció]`, equivalent al bucle `for` + `.append()`
- Aplicació de llistes per comprensió per extreure valors d'una llista de diccionaris
- Gestió de duplicats al scraper: llegir JSON existent + comprovar per títol + escriure tot de nou
- Per què `'w'` i no `'a'` per a fitxers JSON (mode append trenca l'estructura)
- `git add -A`: registra supressions, addicions i moviments de fitxers
- Patrons genèrics al `.gitignore`: `entorn*` per cobrir qualsevol entorn virtual
- Incident real: token de GitHub exposat al xat → revocat i renovat immediatament
- Reorganització del directori de projectes: subcarpeta `python/` per a exercicis

**Projecte construït:**
- `scraping_03.py` versió final amb `argparse` (`--pagina-inici`) i gestió de duplicats per títol

**Errors principals:**
- `try/except` innecessari al voltant de `parse_args()` (eliminat — `argparse` gestiona els seus errors)
- `KeyError: 'titol'` per copy-paste d'`agenda.json` en lloc de `llibres.json` (detectat autònomament)
- Token de GitHub exposat públicament al xat (revocat i renovat immediatament)
- Fitxers moguts sense `git add -A` (resolt amb `git add -A`)

**Transferència autònoma destacada:**
Ha detectat el `KeyError` ell sol amb depuració mental sense necessitar el `print()` de diagnòstic suggerit. Ha raonat correctament per què cal `'w'` i no `'a'` per a JSON, i ha identificat la solució (llegir→modificar→escriure) per analogia amb `agenda_persistent.py`. ⭐⭐

**Observació del tutor:**
Sessió productiva amb un incident de seguretat real gestionat correctament — el millor aprenentatge és el que costa. Les llistes per comprensió s'han introduït de forma orgànica en context real. El raonament per analogia (agenda→scraper) demostra que els patrons s'estan consolidant transversalment. Preparat per a mòduls propis i estructura de projecte.

---

## DEURES PENDENTS

- Afegir un segon argument `--pagina-fi` a `scraping_03.py` per definir també la pàgina final
- Investigar el concepte de **mòduls propis** a Python: com es crea un fitxer `.py` que s'importa des d'un altre

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
| 8-9 | Entorns virtuals, scraping avançat, paginació | ✅ Completat |
| 9-10 | `argparse`, llistes per comprensió, gestió de duplicats | ✅ Completat |
| 10-11 | Mòduls propis, `__init__.py`, estructura de projecte | ⏳ Pendent |

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
