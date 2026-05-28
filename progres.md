# PROGRÉS — Tutor Programació i Ciberseguretat

## PERFIL
- **Nom:** David
- **Nivell assignat:** PRINCIPIANT**→INTERMEDI** (transició en curs)
- **Objectiu:** Curiositat i feina
- **Hores setmanals:** 10
- **Risc detectat:** Tutorial hell — tendència a consumir sense construir *(risc eliminat: 12 sessions consecutives construint codi real)*

---

## TAULA DE SEGUIMENT

| Skill | Nivell | Evidència | Proper pas |
|-------|--------|-----------|------------|
| Python — Variables | 5/10 | Aplicades amb autonomia en múltiples scripts | — |
| Python — Tipus | 6/10 | Casting fluid, tipus correctes al JSON | — |
| Python — Condicions | 6/10 | Aplicades autònomament i combinades | Combinació complexa |
| Python — Bucles | 8/10 | Paginació amb patró fetch-process-fetch, lògica de condició | — |
| Python — Llistes | 9/10 | Llistes per comprensió en funció genèrica reutilitzable | — |
| Python — Funcions | 8/10 | Funció genèrica `cerca_llista()`, simplificació pythònica | Funcions amb valors per defecte |
| Python — Diccionaris | 6/10 | Diccionari com a taula de conversió, accés encadenat | Diccionaris niats |
| Python — Fitxers | 6/10 | Patró llegir→modificar→escriure consolidat | Modes avançats |
| Python — JSON | 7/10 | Gestió de duplicats, patró llegir+escriure robust | JSON amb múltiples APIs |
| Python — Errors | 8/10 | `raise TypeError` amb missatges descriptius, `except as e`, `exit()` | `ValueError`, errors personalitzats amb classe pròpia |
| Python — Strings | 5/10 | Slicing, f-strings per URLs dinàmiques | Mètodes de string |
| Python — Mòduls | 7/10 | Paquet propi, `__init__.py`, imports relatius, `if __name__` | Estructura de projecte gran |
| argparse | 6/10 | Dos arguments (`--pagina-inici`, `--pagina-fi`) amb `type` i `default` | Flags booleans |
| requests | 5/10 | Paginació, gestió de codis d'estat, 50 peticions seqüencials | POST, headers |
| BeautifulSoup | 5/10 | Classes múltiples, accés a atributs, cerca dins element | Scraping avançat |
| Entorns virtuals | 5/10 | Entorn nou creat per projecte, `requirements.txt` actualitzat | Gestió avançada |
| Seguretat | 4/10 | Token revocat i renovat ràpidament, consciència de secrets exposats | `.env` files |
| Terminal | 7/10 | `git add -A` vs `git add *`, criteri correcte d'ús | Permisos i pipes |
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
Sessió molt productiva. La deducció autònoma sobre la necessitat de les funcions és un salt qualitatiu important. El patró DRY s'ha après des de la necessitat real, no des de l'abstracció.

---

## SESSIÓ 5 — Resum

**Data:** 22/05/2026

**Contingut treballat:**
- Persistència de dades: per què els diccionaris en memòria no sobreviuen al tancament del programa
- Fitxers de text: modes `r`, `w`, `a`; `open()`, `.read()`, `.write()`, `with`
- Format JSON: estructura, `json.dump()`, `json.load()`, `ensure_ascii=False`, `indent=4`
- Patró llegir→modificar→escriure per a JSON persistent
- Gestió d'errors: `try/except FileNotFoundError` per primer ús
- Menú interactiu amb `while True` i `break`
- Agenda persistent: afegir, llistar, buscar contactes amb persistència real

**Projecte construït:**
- `agenda_persistent.py` — agenda amb menú interactiu, persistència JSON, cerca per nom

**Errors principals:**
- `json.dump` dins del bucle (escrivia el fitxer en cada iteració)
- Oblidar el `break` al menú (bucle infinit)

**Transferència autònoma destacada:**
Ha identificat per si sol que cal llegir el JSON abans d'afegir per no sobreescriure'l. ⭐

**Observació del tutor:**
Primera sessió amb persistència real. El patró llegir→modificar→escriure és fonamental i s'ha après en context real.

---

## SESSIÓ 6 — Resum

**Data:** 23/05/2026

**Contingut treballat:**
- Gestió d'errors multiexcepció: `FileNotFoundError`, `json.JSONDecodeError`, `ValueError`, `PermissionError`, `OSError`
- Validació robusta d'input: patró `valid = False` / `while not valid` / `try sets valid = True`
- Idioma pythònic `while not nom` per comprovar strings buits
- Git remote: creació de repositori GitHub, Personal Access Token, primer `git push`

**Projecte construït:**
- `agenda_persistent.py` versió robusta amb gestió completa d'errors i validació d'input

**Errors principals:**
- `try/except` sense `while` (no reintentava l'input després de l'error)
- Detectat i corregit autònomament ⭐

**Observació del tutor:**
Ha autoidentificat el bug del `try` sense `while` i l'ha corregit sol. Primera connexió real amb GitHub.

---

## SESSIÓ 7 — Resum

**Data:** 24/05/2026

**Contingut treballat:**
- Repàs i consolidació de la gestió d'errors de la sessió anterior
- Revisió del flux Git complet (add, commit, push)
- README.md: estructura bàsica en Markdown

**Deures assignats:**
- Crear README.md per al projecte
- Investigar la llibreria `requests`

---

## SESSIÓ 8 — Resum

**Data:** 25/05/2026

**Contingut treballat:**
- Llibreria `requests`: `requests.get()`, `response.status_code`, `response.text`, `response.json()`
- APIs públiques: estructura de resposta JSON, accés a camps niats
- Seguretat: API keys, riscos d'exposar secrets, bones pràctiques
- BeautifulSoup: `find()`, `find_all()`, accés a atributs, text d'elements
- Inspecció HTML amb DevTools per identificar elements
- Slicing `[2:]` per netejar prefixos (£, Â)

**Projecte construït:**
- `scraping_01.py` — primera petició real a una API
- `scraping_02.py` — scraping de books.toscrape.com: títol, preu, puntuació

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

## SESSIÓ 11 — Resum

**Data:** 27/05/2026

**Contingut treballat:**
- Mòduls propis: creació de `utils.py` i importació amb `import eines.utils as utils`
- Paquets: carpeta `eines/` amb `__init__.py`, `from . import utils`
- Imports relatius: per què Python 3 requereix el punt explícit dins de paquets
- `if __name__ == "__main__"`: separar codi executable de codi importable
- `__pycache__`: què és, per què es genera i com ignorar-lo al `.gitignore`
- `git add *` vs `git add -A`: criteri correcte d'ús (no mecànic)
- Funció `cerca_llista(terme, clau, llista)` a `utils.py`: lògica genèrica reutilitzable
- Simplificació pythònica: `return expressió_booleana` en lloc d'`if/else` amb `True/False`

**Projectes construïts:**
- `eines/utils.py` — mòdul propi amb `conversio()` i `cerca_llista()`
- `eines/__init__.py` — paquet configurat amb import relatiu
- `scraping_03.py` refactoritzat amb `if __name__ == "__main__"` i `import eines.utils`

**Errors principals:**
- `import utils` dins del paquet en lloc de `from . import utils` (corregit)
- `cerca_llista()` usant `terme` com a clau i valor alhora (corregit separant en dos paràmetres)
- `if/else` retornant `True/False` explícitament (simplificat a `return terme in [...]`)

**Transferència autònoma destacada:**
Ha deduït correctament que `__init__.py` "reconeix el directori com a mòdul". Ha qüestionat el comportament de VSCode en refactoritzar l'import (instint correcte). Ha raonat per si sol per què el `else` del `if __name__` s'executaria en importar, no en executar. ⭐⭐

**Observació del tutor:**
Sessió de maduresa estructural: el codi ja no és un script pla sinó un projecte organitzat amb paquets, mòduls i separació clara entre executable i importable. El raonament crític sobre el comportament de VSCode i sobre `if __name__` demostra que l'alumne ja no segueix instruccions cegament — les avalua. Preparat per a `raise` i errors personalitzats.

---

## SESSIÓ 12 — Resum

**Data:** 28/05/2026

**Contingut treballat:**
- Consolidació llistes per comprensió: ordre d'execució (llista primer, `in` després), redundància de `f"{clau}"`
- `raise`: concepte, sintaxi, diferència amb `try/except`
- `TypeError` vs `ValueError`: quan usar cada un
- Validació amb `if/elif` + `raise` per argument independent (missatges descriptius i granulars)
- `except TypeError as e` + `print(e)`: capturar i mostrar el missatge del `raise`
- `exit()` vs `break`: decisió conscient d'aturar el programa per errors de programació
- Per què un sol `try/except` cobreix dues funcions en el mateix bloc
- Principi DRY aplicat a `try/except` niats innecessaris (detectat i eliminat)
- `type()` vs `isinstance()`: diferència per herència
- Herència a Python: `bool` com a subclasse d'`int`, implicacions pràctiques

**Projectes construïts:**
- `eines/utils.py` — `conversio()` i `cerca_llista()` amb validació `raise TypeError` completa
- `scraping_03.py` — `try/except TypeError as e` + `exit()` per capturar errors de mòdul

**Errors principals:**
- Instint inicial de `try/except` en lloc d'`if` + `raise` per a validació (corregit raonat)
- `except TypeError` sense dos punts `:` (sintaxi)
- `try/except` duplicat niat innecessari (eliminat aplicant DRY)

**Transferència autònoma destacada:**
Ha qüestionat activament si el `try/except` cobria `conversio()` — instint de programador real. Ha raonat correctament la diferència `type()` vs `isinstance()` a partir del concepte d'herència. ⭐⭐

**Observació del tutor:**
Sessió de robustesa: el mòdul `utils.py` ara és defensiu — no accepta entrades invàlides silenciosament. La distinció `raise` vs `try/except` és una de les que separa el codi que funciona del codi que es pot mantenir. La comprensió de `type()` vs `isinstance()` a partir de l'herència demostra que el raonament conceptual s'aprofundeix. Preparat per a classes d'errors personalitzades.

---

## DEURES PENDENTS

- Investigar diferència entre `raise TypeError` i crear una **classe d'error personalitzada** (`class ErrorPersonalitzat(Exception)`) — preparació per a la propera sessió.

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
| 10-11 | Mòduls propis, `__init__.py`, estructura de projecte | ✅ Completat |
| 11-12 | `raise`, errors personalitzats, robustesa de mòduls | ✅ Completat |
| 12-13 | Classes d'errors personalitzades, `ValueError`, errors de domini | ⏳ Pendent |

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
