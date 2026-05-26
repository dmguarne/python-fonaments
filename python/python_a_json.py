import json

persona01 = {
    "nom": "David",
    "edat": 39,
    "ciutat": "Barcelona",
}

persona02 = {
    "nom": "Maria",
    "edat": 24,
    "ciutat": "Girona",
}

persona03 = {
    "nom": "Antoni",
    "edat": 55,
    "ciutat": "Mataró",
}

agenda = [persona01, persona02, persona03]

with open('agenda.json', 'w') as fitxer:
    json.dump(agenda, fitxer, ensure_ascii=False, indent=4)