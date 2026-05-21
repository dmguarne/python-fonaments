## Crear una llista buida
## Demanar 3 noms a l'usuari amb input() i afegir-los a la llista
## Mostrar quants noms hi ha a la llista
## Mostrar el primer i l'últim nom

llista = []
for i in range(3):
    llista.append(input("Escriu un nom propi: "))
print(f"La llista té {len(llista)} elements.")
print(f"El primer element és '{llista[0]}'.")
print(f"L'últim element és '{llista[-1]}'.")

print("La llista completa és:")
## Recorre la llista amb un for i imprimeix cada nom amb el seu número d'ordre.
for i in range(len(llista)):
    print(f"{i + 1}. {llista[i]}")

## Demana a l'usuari un nom per buscar. Si el nom és a la llista, imprimeix "Trobat". Si no hi és, imprimeix "No trobat".
cerca = input("Cerca un nom a la llista: ")
resultat = False
for i in range(len(llista)):
    if llista[i] == cerca:
        resultat = True
if resultat == True:
    print("Trobat.")
else:
    print("No trobat.")

##Afegeix una quarta funcionalitat al llistes.py: permetre a l'usuari eliminar un nom de la llista. Si el nom existeix, l'elimina i mostra la llista actualitzada. Si no existeix, ho indica.
## Investiga el mètode .remove() de les llistes Python.
## Després fes git add i git commit -m "missatge descriptiu" de tot.
