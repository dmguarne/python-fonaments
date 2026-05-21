import json

## Definició de la funció que mostra l'agenda:
def mostrar_persona(contacte): ## Quan invoqui la funció, al paràmetre "contacte" li hauré de donar un diccionari.
    return f"{contacte["nom"]} | {contacte["edat"]} anys | {contacte["ciutat"]}"

## Imprimeix cada diccionari:
def mostrar_agenda(agenda):
    for i, contacte in enumerate(agenda, start=1):
        print(f"{i}. {mostrar_persona(contacte)}")

with open("agenda.json", "r") as fitxer: ## Obre agenda.json i el llegeix a fitxer.
    agenda = json.load(fitxer) ## Estableix la variable agenda, que emmagatzema el contingut del fitxer
    print("Agenda:")
    mostrar_agenda(agenda) ## La funció que ja tenia en l'script anterior per pintar l'agenda.

with open("agenda.json", "w") as fitxer:
    json.dump(agenda, fitxer, ensure_ascii=False, indent=4)