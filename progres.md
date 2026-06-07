# PROGRÉS — Tutor Programació i Ciberseguretat

## PERFIL
- **Nom:** David
- **Nivell assignat:** PRINCIPIANT**→INTERMEDI** (transició en curs)
- **Objectiu:** Curiositat i feina
- **Hores setmanals:** 10
- **Risc detectat:** Tutorial hell — tendència a consumir sense construir *(risc eliminat: 15 sessions consecutives construint codi real)*

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
| Python — Diccionaris | 6/10 | Diccionari com a taula de conversió, accés encadenat niat | Diccionaris niats complexos |
| Python — Fitxers | 6/10 | Patró llegir→modificar→escriure consolidat | Modes avançats |
| Python — JSON | 7/10 | Gestió de duplicats, patró llegir+escriure robust | JSON amb múltiples APIs |
| Python — Errors | 9/10 | Classes d'errors personalitzades (`CadenaInvalida`, `ClauInvalida`, `LlistaInvalida`, `PuntuacioInvalida`), captura múltiple, raonament sobre captura excessiva | Classes d'error amb atributs propis |
| Python — Strings | 5/10 | Slicing, f-strings per URLs dinàmiques | Mètodes de string |
| Python — Mòduls | 7/10 | Paquet propi, `__init__.py`, imports relatius, `if __name__` | Estructura de projecte gran |
| argparse | 6/10 | Dos arguments (`--pagina-inici`, `--pagina-fi`) amb `type` i `default` | Flags booleans |
| requests | 8/10 | POST amb `json=`, PATCH, codis HTTP (200/201/403), flux GET→POST→PATCH→GET, funció reutilitzable | timeout, paginació d'APIs |
| BeautifulSoup | 7/10 | Navegació DOM amb `.parent`, accés a atributs `element["href"]`, scraping real de producció | Scraping avançat |
| Regex | 6/10 | Sintaxi fonamental, patró complex de definició de funció, `re.search/match/findall`, raw strings, aplicació dins scraping | Grups de captura, substitució |
| Entorns virtuals | 5/10 | Entorn nou creat per projecte, `requirements.txt` actualitzat | Gestió avançada |
| Seguretat | 7/10 | Àmbits de tokens (scopes), 403 per permisos insuficients, token renovat amb permisos correctes | OAuth |
| Terminal | 7/10 | `git add -A` vs `git add *`, criteri correcte d'ús | Permisos i pipes |
| Git | 8/10 | `HEAD`/`main`/`origin/main` com a etiquetes de commits, branques com a decorats, sincronització push | Branques |
| pathlib | 7/10 | `Path(__file__).parent`, operador `/`, `.exists()`, `.mkdir()`, rutes absolutes vs relatives | Mètodes avançats |
| logging | 7/10 | Nivells INFO/WARNING/ERROR/CRITICAL, `basicConfig`, `StreamHandler` dual, integrat a scraping_03 | Handlers múltiples |
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
Ha identificat per si sol que calia un `try/except` per al primer ús (fitxer inexistent). ⭐⭐

**Observació del tutor:**
Primera aplicació de persistència real. L'agenda ja és un programa funcional complet.

---

## SESSIÓ 6 — Resum

**Data:** 22/05/2026

**Contingut treballat:**
- Terminal Linux: navegació, `pwd`, `ls`, `cd`, `mkdir`, `rm`, `cp`, `mv`
- Permisos bàsics: `chmod +x`
- Git avançat: `git log`, `git diff`, `git stash`, branques conceptuals
- GitHub: creació de repositori remot, `git remote add origin`, `git push`
- Personal Access Token: creació, ús, revocació
- `.gitignore`: patrons, fitxers locals, per què ignorar `__pycache__`

**Projecte construït:**
- Repositori `python-fonaments` publicat a GitHub amb primer push

**Errors principals:**
- Token exposat al xat (detectat i revocat immediatament)

**Observació del tutor:**
Incident de seguretat real gestionat correctament. La millor manera d'aprendre seguretat és patir-ne les conseqüències de forma controlada.

---

## SESSIÓ 7 — Resum

**Data:** 23/05/2026

**Contingut treballat:**
- Gestió d'errors avançada: multi-excepció (`FileNotFoundError`, `json.JSONDecodeError`, `ValueError`, `PermissionError`, `OSError`)
- Validació robusta: patró `while not valid` + `try/except` per forçar input correcte
- Idioma pythònic: `while not nom` per comprovar cadena buida
- Git remote: push a GitHub amb token, gestió de credencials

**Projecte construït:**
- `agenda_persistent.py` versió robusta amb multi-excepció i validació d'input

**Transferència autònoma destacada:**
Ha detectat que el `try/except` sense `while` no resolia el problema i l'ha corregit autònomament. ⭐⭐

---

## SESSIÓ 8 — Resum

**Data:** 24/05/2026

**Contingut treballat:**
- Web scraping: concepte, HTML, inspecció DevTools
- `requests`: GET bàsic, `response.text`, codis d'estat
- BeautifulSoup: `find`, `find_all`, accés a atributs, `.text`
- Primer scraper funcional

**Projecte construït:**
- `scraping_01.py` — títol i preu del primer llibre de books.toscrape.com

---

## SESSIÓ 9 — Resum

**Data:** 26/05/2026

**Contingut treballat:**
- Scraping de pàgina completa: tots els elements d'una pàgina
- Classes múltiples a BeautifulSoup
- Diccionari de conversió per a dades categòriques (puntuació en paraules → nombre)
- Patró fetch-process-fetch per paginació
- Entorns virtuals: creació, activació, `pip install`, `requirements.txt`
- `.gitignore`: excloure `entorn/` i fitxers locals de Git

**Projecte construït:**
- `scraping_03.py` versió final — 1000 llibres de 50 pàgines guardats a `llibres.json`
- Entorn virtual configurat amb `requirements.txt` i `.gitignore`

**Errors principals:**
- `response` de la condició obsoleta per petició al principi del bucle
- Nom de funció igual que variable interna
- Puntuació guardada com a string en lloc d'enter

**Transferència autònoma destacada:**
Ha identificat que la pàgina 1 seguia el mateix patró URL. Ha eliminat la variable `ordre` autònomament. ⭐⭐

**Observació del tutor:**
Salt qualitatiu: de scrapar una pàgina a scrapar una web sencera amb 1000 registres.

---

## SESSIÓ 10 — Resum

**Data:** 27/05/2026

**Contingut treballat:**
- `argparse`: flux complet — `ArgumentParser()`, `add_argument()`, `parse_args()`, accés a `arguments.nom`
- `type=` i `default=` a `add_argument()`
- Conversió automàtica de guions a guions baixos en noms d'arguments
- Regla: no cal `try/except` sobre el que les llibreries ja gestionen internament
- Llistes per comprensió: sintaxi `[expressió for element in col·lecció]`
- Gestió de duplicats al scraper: llegir JSON existent + comprovar per títol + escriure tot de nou
- Per què `'w'` i no `'a'` per a fitxers JSON
- `git add -A`: registra supressions, addicions i moviments de fitxers
- Patrons genèrics al `.gitignore`: `entorn*`
- Incident real: token de GitHub exposat al xat → revocat i renovat immediatament

**Projecte construït:**
- `scraping_03.py` versió final amb `argparse` i gestió de duplicats per títol

**Errors principals:**
- `try/except` innecessari al voltant de `parse_args()`
- `KeyError: 'titol'` per copy-paste (detectat autònomament)
- Token de GitHub exposat públicament

**Transferència autònoma destacada:**
Ha detectat el `KeyError` sol amb depuració mental. Ha raonat correctament per què cal `'w'` i no `'a'`. ⭐⭐

**Observació del tutor:**
Incident de seguretat real gestionat correctament — el millor aprenentatge és el que costa.

---

## SESSIÓ 11 — Resum

**Data:** 27/05/2026

**Contingut treballat:**
- Mòduls propis: creació de `utils.py` i importació amb `import eines.utils as utils`
- Paquets: carpeta `eines/` amb `__init__.py`, `from . import utils`
- Imports relatius: per què Python 3 requereix el punt explícit dins de paquets
- `if __name__ == "__main__"`: separar codi executable de codi importable
- `__pycache__`: què és, per què es genera i com ignorar-lo al `.gitignore`
- `git add *` vs `git add -A`: criteri correcte d'ús
- Funció `cerca_llista(terme, clau, llista)` a `utils.py`
- Simplificació pythònica: `return expressió_booleana`

**Projectes construïts:**
- `eines/utils.py` — mòdul propi amb `conversio()` i `cerca_llista()`
- `eines/__init__.py` — paquet configurat amb import relatiu
- `scraping_03.py` refactoritzat

**Transferència autònoma destacada:**
Ha deduït que `__init__.py` "reconeix el directori com a mòdul". Ha raonat per si sol el comportament de `if __name__`. ⭐⭐

**Observació del tutor:**
Sessió de maduresa estructural: el codi ja és un projecte organitzat amb paquets.

---

## SESSIÓ 12 — Resum

**Data:** 28/05/2026

**Contingut treballat:**
- Consolidació llistes per comprensió
- `raise`: concepte, sintaxi, diferència amb `try/except`
- `TypeError` vs `ValueError`: quan usar cada un
- Validació amb `if/elif` + `raise` per argument independent
- `except TypeError as e` + `print(e)`
- `exit()` vs `break`
- Per què un sol `try/except` cobreix dues funcions en el mateix bloc
- Principi DRY aplicat a `try/except` niats innecessaris
- `type()` vs `isinstance()`: diferència per herència
- Herència a Python: `bool` com a subclasse d'`int`

**Projectes construïts:**
- `eines/utils.py` — `conversio()` i `cerca_llista()` amb validació `raise TypeError`
- `scraping_03.py` — `except TypeError as e` + `exit()`

**Transferència autònoma destacada:**
Ha qüestionat activament si el `try/except` cobria `conversio()`. Ha raonat `type()` vs `isinstance()` a partir de l'herència. ⭐⭐

**Observació del tutor:**
El mòdul `utils.py` ara és defensiu. La distinció `raise` vs `try/except` separa el codi que funciona del codi que es pot mantenir.

---

## SESSIÓ 13 — Resum

**Data:** 28/05/2026

**Contingut treballat:**
- Classes d'errors personalitzades: sintaxi `class Nom(Exception): pass`
- Herència d'`Exception`: per què és necessària, analogia amb `bool`→`int`
- Nomenclatura semàntica: nom descriptiu del domini vs error genèric de Python
- Ruta d'accés (`utils.CadenaInvalida`) vs nom de la classe (`CadenaInvalida`)
- Captura múltiple: `except (ErrorA, ErrorB, ErrorC) as e`
- Perill de captura excessiva: per què `except Exception` és un antipatró
- Validació de valor de domini: `PuntuacioInvalida` per clau absent al diccionari
- Ordre dins la funció: definir el diccionari abans de validar-hi la clau

**Projectes construïts:**
- `eines/utils.py` — quatre classes d'error personalitzades (`CadenaInvalida`, `ClauInvalida`, `LlistaInvalida`, `PuntuacioInvalida`) aplicades a `conversio()` i `cerca_llista()`
- `scraping_03.py` — `except` actualitzat amb les quatre classes pròpies

**Errors principals:**
- Línia suelta fora de la funció (detectat autònomament)
- Validació usant `equivalencies` abans de definir-lo (detectat autònomament)

**Transferència autònoma destacada:**
Ha explicat els dos motius per usar errors personalitzats abans de la micro-lliçó. Ha detectat i corregit ambdós errors del codi de forma autònoma. Ha raonat correctament per què `except Exception` és perillós. ⭐⭐⭐

**Observació del tutor:**
Sessió de maduresa en disseny: `utils.py` ja té una API pública clara amb errors propis, com qualsevol llibreria professional.

---

## SESSIÓ 14 — Resum

**Data:** 29/05/2026

**Contingut treballat:**
- Model mental API REST vs scraping: canal oficial, estructurat, estable
- Endpoints com a contracte: el servidor pot reorganitzar internament, l'endpoint és estable
- Els 4 elements d'una crida API: URL, mètode HTTP, headers, body
- `.env` + `python-dotenv` + `os.environ.get`: carregat amb pista mínima
- GET autenticat amb headers: `{"Authorization": "Bearer TOKEN"}`
- `resposta.json()`: parsejar resposta JSON
- `raise_for_status()`: llença `HTTPError` automàticament per codis 4xx/5xx
- Distinció `requests.exceptions.ConnectionError` vs `ConnectionError` built-in
- Accés a dades niades: `element['commit']['author']['name']`
- Iteració pythònica: `for element in dades` sense índex

**Projecte construït:**
- `api_github.py` — GET autenticat a l'API de GitHub, llista de commits amb data, autor i missatge; gestió robusta d'errors amb `raise_for_status()` i captura múltiple

**Errors principals:**
- `"Authorizacion"` (error tipogràfic al header) — detectat amb pista mínima
- `resposta.json` sense parèntesis — detectat amb pista mínima
- Parèntesi de tancament del `print` mal col·locat — detectat autònomament
- `ConnectionError` built-in en lloc de `requests.exceptions.ConnectionError` — corregit amb explicació

**Transferència autònoma destacada:**
Ha construït el codi inicial quasi complet de forma autònoma ("no sé fer-ho" però el codi era quasi perfecte). Ha aplicat `raise_for_status()` + captura múltiple correctament al primer intent. ⭐⭐⭐

**Observació del tutor:**
Salt important: de scraping a API REST autenticada. El patró de gestió d'errors és ara professional. La seguretat amb `.env` s'ha interioritzat. Preparat per a POST i APIs amb autenticació avançada.

---

## SESSIÓ 15 — Resum

**Data:** 30/05/2026

**Contingut treballat:**
- GET vs POST vs PATCH: diferències conceptuals i pràctiques
- Idempotència: GET i PATCH no canvien l'estat repetidament, POST sí
- Codis HTTP: 200 OK vs 201 Created vs 403 Forbidden, famílies 2xx/4xx/5xx
- `json=` a `requests.post()`: serialització automàtica + `Content-Type: application/json`
- POST a l'API de GitHub: crear issues amb `title` i `body`
- PATCH a l'API de GitHub: modificar `state` d'una issue a `"closed"`
- Caché de servidor: per què el segon GET pot semblar desfasat
- Àmbits de tokens (scopes): 403 per permisos insuficients, renovació del token
- Refactorització DRY: funció `comprovar_issues()` que retorna dades en lloc de només imprimir
- Patró `if x in ("S", "s")` com a alternativa pythònica a `or`

**Projecte construït:**
- `api_github_post.py` — flux complet GET→POST→GET→PATCH→GET amb gestió robusta d'errors i inputs interactius

**Errors principals:**
- `json={"prova": "confirmat"}` — clau incorrecta per a l'API de GitHub (detectat amb pista)
- PATCH duplicat per issue (detectat autònomament)
- `{i}` a l'URL del PATCH en lloc de `{i['number']}` (detectat amb pista)
- Funció sense `return` (detectat autònomament)
- Token sense permisos d'escriptura → 403 (resolt autònomament)

**Transferència autònoma destacada:**
Ha detectat que la funció no retornava res i ha proposat la solució correcta. Ha simplificat `.append()` en bucle a `return issues` directament. Ha gestionat el 403 renovant el token de forma autònoma. ⭐⭐

**Observació del tutor:**
Primera sessió amb operacions d'escriptura a una API real. El flux GET→POST→PATCH és el patró central de qualsevol aplicació web. David ja el domina.

---

## SESSIÓ 16 — Resum

**Data:** 31/05/2026

**Contingut treballat:**
- Revisió deures: `git push` confirmat, OAuth explicat correctament
- OAuth: flux complet (lloc web redirigeix → usuari s'autentica a Google → Google envia token al lloc web)
- Git: conceptes `HEAD`, `main`, `origin/main` com a etiquetes que apunten a commits; branques com a decorats sobre la mateixa carpeta
- `pathlib`: `Path(__file__).parent`, operador `/`, rutes relatives vs absolutes, `.exists()`, `.mkdir(parents=True, exist_ok=True)`
- `logging`: nivells INFO/WARNING/ERROR/CRITICAL, `basicConfig` amb `filename` i `format`, `StreamHandler` per sortida dual (fitxer + pantalla)
- Integració de `pathlib` i `logging` al `scraping_03.py`

**Projectes modificats:**
- `scraping_03.py` — rutes migrades a `pathlib`, `print()` d'errors substituïts per `logging` amb nivells correctes, `StreamHandler` afegit

**Errors principals:**
- `ruda_dades` (NameError tipogràfic) — detectat autònomament
- `.exists()` sobre el fitxer en lloc de la carpeta — detectat amb pregunta guiada

**Transferència autònoma destacada:**
- Ha afegit cas `elif response.status_code == 200 and pagina > final` sense que el tutor ho demanés ⭐⭐
- Ha mantingut el `print()` de la llista de llibres correctament (informació per a l'usuari, no event de sistema) ⭐

**Observació del tutor:**
`scraping_03.py` és ara un script de producció: rutes robustes, log persistent, nivells semàntics correctes. La distinció `print` vs `logging` interioritzada sense explicació explícita.

---

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
| 12-13 | Classes d'errors personalitzades, captura múltiple, antipatrons | ✅ Completat |
| 13-14 | APIs REST, `requests` avançat, autenticació, GET autenticat | ✅ Completat |
| 14-15 | POST, body, APIs amb escriptura, autenticació avançada | ⏳ Pendent |

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


## SESSIÓ 17 — Resum

**Data:** 07/06/2026

**Contingut treballat:**
- Regex: concepte deduït per necessitat (vs implementació manual amb condicions)
- Sintaxi regex: `\d`, `\w`, `\s`, `.`, `+`, `*`, `?`, `^`, `$`, `\(`, raw strings `r"..."`
- Patró complex: definició de funció Python amb paràmetres opcionals `def\s\w+\((\w*,(\s)?)*\w*\):$`
- `re.search` vs `re.match` vs `re.findall` — casos d'ús de cada funció
- Arquitectura de projecte: disseny complet de `sahara_monitor` (connectors, eines, dades)
- `connectors/scraping.py`: scraping de Sahara Press Service, extracció de titular/URL/data/font
- Navegació DOM: `.parent` per accedir a elements fora de la jerarquia directa
- Accés a atributs HTML: `element["href"]`
- Aplicació de regex dins del scraping per extreure data (`re.search` + `.group()`)
- `eines/magatzem.py`: persistència JSON amb deduplicació per URL, creació automàtica de carpetes
- Logging centralitzat: problema del doble StreamHandler detectat i resolt

**Projectes construïts:**
- `regex_01.py` — detector de definicions de funcions Python amb regex
- `sahara_monitor/connectors/scraping.py` — connector scraping Sahara Press Service
- `sahara_monitor/eines/magatzem.py` — magatzem JSON amb deduplicació
- `sahara_monitor/proves.py` — script de proves del flux complet

**Errors principals:**
- `noticia.find("href")` en lloc d'accés per atribut `element["href"]` — detectat autònomament
- Llista per comprensió amb `.append()` redundant — detectat autònomament
- Logging configurat a cada mòdul → doble StreamHandler — detectat i resolt amb raonament correcte

**Transferència autònoma destacada:**
- Ha aplicat regex per extreure la data dins del scraping sense que el tutor ho demanés ⭐⭐⭐
- Ha raonat que `font` és estàtica i no cal scrapejar-la ⭐
- Ha dissenyat l'arquitectura completa del projecte amb criteris propis (SRP, separació dades/codi) ⭐⭐

**Observació del tutor:**
Sessió de maduresa arquitectònica. El projecte `sahara_monitor` té disseny professional des del primer dia. La transferència de regex al scraping és el millor exemple fins ara d'aprenentatge connectat.

---

## DEURES PENDENTS

- `git add`, `commit` i `push` del projecte `sahara_monitor`
- Afegir paginació a `connectors/scraping.py`

---
