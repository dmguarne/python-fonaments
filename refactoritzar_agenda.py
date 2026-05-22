import json

with open("agenda.json", "r") as fitxer: ## Obre agenda.json i el llegeix a fitxer.
    agenda = json.load(fitxer) ## Estableix la variable agenda, que emmagatzema el contingut del fitxer

for i, contacte in enumerate(agenda, start=1):
    contacte["edat"] = int(contacte["edat"]) ## Converteix eel contingut de la clau 'edat' a int.

with open('agenda.json', 'w') as fitxer: ## Obre agenda.json en mode escriptura per actualitzar-lo.
    json.dump(agenda, fitxer, ensure_ascii=False, indent=4) ## Bolca el contingut actualitzat d'agenda al json sobreescrivint el contingut previ.