def enumerar(llista): ## Definim la funció que imprimeix la llista numerada
    for i in range(len(llista)): ## Recorre la llista amb un for i imprimeix cada nom amb el seu número d'ordre.
        print(f"{i + 1}. {llista[i]}")

llista = [] ## Crear una llista buida

    
for i in range(3):
    llista.append(input("Escriu un nom propi: ")) ## Demanar 3 noms a l'usuari amb input() i afegir-los a la llista
print(f"La llista té {len(llista)} elements.") ## Mostrar quants noms hi ha a la llista
print(f"El primer element és '{llista[0]}'.") ## Mostrar el primer i l'últim nom
print(f"L'últim element és '{llista[-1]}'.") ## Mostrar el primer i l'últim nom

print("La llista completa és:")

enumerar(llista)
## Demana a l'usuari un nom per buscar. Si el nom és a la llista, imprimeix "Trobat". Si no hi és, imprimeix "No trobat".
cerca = input("Cerca un nom a la llista: ")
resultat = False
for i in range(len(llista)):
    if llista[i] == cerca:
        resultat = True
if resultat:
    print("Trobat.")
else:
    print("No trobat.")

## Demanar a l'usuari un nom per esborrar
esborrar = input("Introdueix un nom per esborrar: ")

## Comprovar si el nom existeix
existeix = False
for nom in range(len(llista)):
    if llista[nom] == esborrar:
        existeix = True
        
if existeix:
    llista.remove(esborrar) ## Esborrar el nom
    enumerar(llista) ## Mostrar la llista actualitzada
else:    
    print("El nom no existeix a la llista") ## Si no existeix, notificar-ho a l'usuari









##Afegeix una quarta funcionalitat al llistes.py: permetre a l'usuari eliminar un nom de la llista. Si el nom existeix, l'elimina i mostra la llista actualitzada. Si no existeix, ho indica.
## Investiga el mètode .remove() de les llistes Python.
## Després fes git add i git commit -m "missatge descriptiu" de tot.
