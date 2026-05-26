## Definició de la funció que mostra l'agenda:
def mostrar_persona(contacte): ## Quan invoqui la funció, al paràmetre "contacte" li hauré de donar un diccionari.
    return f"{contacte["nom"]} | {contacte["edat"]} anys | {contacte["ciutat"]}"

## Imprimeix cada diccionari:
def mostrar_agenda(agenda):
    for i in range(len(agenda)): ## Recorre la llista amb un for i.
        print(f"{i + 1}. {mostrar_persona(agenda[i])}")
        

## Crear una llista de diccionaris — cada element és un diccionari amb nom, edat i ciutat:
## Afegir 3 contactes a la llista:
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

## Definir la llista agenda:
agenda = [persona01, persona02, persona03]

## Mostrar l'agenda a l'usuari:
print("Agenda:")
mostrar_agenda(agenda)

## Demana a l'usuari introduir un nom:
cerca = input("Introdueix un nom a buscar: ")
trobat = False ## Variable per comprovar la cerca.

## Executa la cerca:
for i in range(len(agenda)):
    if agenda[i]["nom"] == cerca: ## Cerca només dins de la clau "nom"
        trobat = True
        print(f"{i + 1}. {mostrar_persona(agenda[i])}")  ## Mostra el registre on ha trobat el nom.
## Un cop acabat el bucle, si no ha trobat la persona, ho notifica a l'usuari:
if not trobat:
    print("Persona no trobada.")



 
