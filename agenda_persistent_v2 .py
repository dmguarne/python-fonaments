import json

## Definició de la funció que mostra l'agenda:
def mostrar_persona(contacte): ## Quan invoqui la funció, al paràmetre "contacte" li hauré de donar un diccionari.
    return f"{contacte["nom"]} | {contacte["edat"]} anys | {contacte["ciutat"]}"

## Imprimeix cada diccionari:
def mostrar_agenda(agenda):
    print("Agenda:\n")
    for i, contacte in enumerate(agenda, start=1):
        print(f"{i}. {mostrar_persona(contacte)}")

## Funció per demanar les dades d'un nou contacte i crear el diccionari:
def demanar_contacte():
    nom = ""
    ciutat = ""
    while not nom:
        nom = input("Introdueix el nom de la persona a afegir: ")
    valid = False
    while not valid:
        try:
            edat = int(input("Introdueix l'edat: "))
            valid = True
        except ValueError:
            print("L'edat ha de ser un número.")
    while not ciutat:
        ciutat = input("Introdueix la ciutat: ")
    contacte_nou = {
        "nom": nom,
        "edat": edat,
        "ciutat": ciutat,
    }
    return contacte_nou

def afegir_contacte(agenda):
    afegir = input("Vols afegir un nou contacte? (S/N)? ") ## Demana a l'usuari un input per decidir si afegir nou contacte
    while afegir == "S" or afegir == "s": ## Només interpreta "sí" si l'usuari tecleja "s" o "S"
        agenda.append(demanar_contacte()) ## Afegeix a la llista el diccionari generat per la funció demanar_contacte()
        mostrar_agenda(agenda) ## Mostra l'agenda actualitzada
        afegir = input("Vols afegir un nou contacte? (S/N)? ")
    else:
        print("Gràcies per la teva col·laboració") ## Finalitza la interacció amb l'usuari.

def eliminar_contacte(agenda):
    repetir = True
    trobat = False ## Variable per comprovar la cerca.
    while repetir and not trobat:
        eliminar = input("Introdueix el nom: ")        
        for i, contacte in enumerate(agenda, start=1):
            if contacte["nom"] == eliminar: ## Cerca només dins de la clau "nom"
                trobat = True
                agenda.remove(contacte)
                print("Contacte eliminat.")
        if not trobat:
            repetir = input("Contacte no trobat. Vols cercar un altre nom? S/N ")
            if repetir != "S" and repetir != "s":
                repetir = False
            else:
                print("Gràcies per la teva col·laboració")

try:
    with open("agenda.json", "r") as fitxer: ## Obre agenda.json i el llegeix a fitxer.
        agenda = json.load(fitxer) ## Estableix la variable agenda, que emmagatzema el contingut del fitxer
except FileNotFoundError:
    agenda = []
except json.JSONDecodeError:
    print("El fitxer agenda.json està corromput.")
    agenda = []

mostrar_agenda(agenda) ## La funció que ja tenia en l'script anterior per pintar l'agenda.

accio = "0"
while accio != "3":
    accio = input("Escull què vols fer:\n" 
    "1. Afegir contacte\n" 
    "2. Esborrar contacte\n"
    "3. Res\n")
    if accio == "1":
        afegir_contacte(agenda)
    elif accio == "2":
        eliminar_contacte(agenda)
    elif accio != "1" and accio != "2" and accio != "3":
        print("Input incorrecte")
if accio == "3":
    print("Gracies per la teva col·laboració")

mostrar_agenda(agenda)

try:
    with open('agenda.json', 'w') as fitxer: ## Obre agenda.json en mode escriptura per actualitzar-lo.
        json.dump(agenda, fitxer, ensure_ascii=False, indent=4) ## Bolca el contingut actualitzat d'agenda al json sobreescrivint el contingut previ.
except PermissionError:
    print("No tens permisos per desar el fitxer.")
except OSError:
    print("Error del sistema.")