## Crear un diccionari que representi una persona amb aquestes claus: nom, edat, ciutat
persona = {
    "nom": "David",
    "edat": 39,
    "ciutat": "Barcelona",
}

## Imprimir cada camp amb una f-string llegible
print(f"La persona es diu {persona["nom"]}, té {persona["edat"]} anys i viu a {persona["ciutat"]}")

## Afegir una clau nova: email
persona["mail"] = "dmguarne@gmail.com"

## Modificar la ciutat per una altra
persona["ciutat"] = "Madrid"

## Imprimir el diccionari sencer recorrent-lo amb .items()
for clau, valor in persona.items():
    print(f"{clau}: {valor}")
