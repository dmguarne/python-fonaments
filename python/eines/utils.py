class PuntuacioInvalida(Exception):
    pass

class CadenaInvalida(Exception):
    pass
class ClauInvalida(Exception):
    pass
class LlistaInvalida(Exception):
    pass




def conversio(numero): # Funció per convertir una paraula en número. L'argument que agafa és la paraula.
    equivalencies = { # Diccionari d'equivalències.
        "One" : 1,        
        "Two" : 2,
        "Three" : 3,
        "Four" : 4,
        "Five" : 5,
    }
    if not numero in equivalencies:
        raise PuntuacioInvalida("La puntuació ha de constar a 'equivalencies'")
    return equivalencies[numero] # Retorna el valor associat a la clau.

# Funció per comprovar si un str es troba dins d'una llista de diccionaris
def cerca_llista(terme, clau, llista):
    if type(terme) != str:
        raise CadenaInvalida("El primer argument ha de ser un string.")
    elif type(clau) != str:
        raise ClauInvalida("El segon argument ha de ser un string.")
    elif type(llista) != list:
        raise LlistaInvalida("El tercer argument ha de ser una llista.")
    return terme in [element[clau] for element in llista] # Construeix una llista per comprensió amb tots els valors de la clau "clau" i hi busca el terme. llista és la llista original de diccionaris que hem passat com a argument. element és cada diccionari.