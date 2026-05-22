import json

## Definició de la funció que mostra l'agenda:
def mostrar_persona(contacte): ## Quan invoqui la funció, al paràmetre "contacte" li hauré de donar un diccionari.
    return f"{contacte["nom"]} | {contacte["edat"]} anys | {contacte["ciutat"]}"

## Imprimeix cada diccionari:
def mostrar_agenda(agenda):
    for i, contacte in enumerate(agenda, start=1):
        print(f"{i}. {mostrar_persona(contacte)}")

## Funció per demanar les dades d'un nou contacte i crear el diccionari:
def demanar_contacte():
    nom = input("Introdueix el nom de la persona a afegir: ")
    edat = int(input("Introdueix l'edat: "))
    ciutat = input("Introdueix la ciutat: ")
    contacte_nou = {
        "nom": nom,
        "edat": edat,
        "ciutat": ciutat,
    }
    return contacte_nou

with open("agenda.json", "r") as fitxer: ## Obre agenda.json i el llegeix a fitxer.
    agenda = json.load(fitxer) ## Estableix la variable agenda, que emmagatzema el contingut del fitxer

print("Agenda:")
mostrar_agenda(agenda) ## La funció que ja tenia en l'script anterior per pintar l'agenda.

afegir = input("Vols afegir un nou contacte? (S/N)? ") ## Demana a l'usuari un input per decidir si afegir nou contacte
while afegir == "S" or afegir == "s": ## Només interpreta "sí" si l'usuari tecleja "s" o "S"
    agenda.append(demanar_contacte()) ## Afegeix a la llista el diccionari generat per la funció demanar_contacte()
    mostrar_agenda(agenda) ## Mostra l'agenda actualitzada
    afegir = input("Vols afegir un nou contacte? (S/N)? ")
else:
    print("Gràcies per la teva col·laboració") ## Finalitza la interacció amb l'usuari.

with open('agenda.json', 'w') as fitxer: ## Obre agenda.json en mode escriptura per actualitzar-lo.
    json.dump(agenda, fitxer, ensure_ascii=False, indent=4) ## Bolca el contingut actualitzat d'agenda al json sobreescrivint el contingut previ.