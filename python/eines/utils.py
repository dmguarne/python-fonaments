def conversio(numero): # Funció per convertir una paraula en número. L'argument que agafa és la paraula.
    equivalencies = { # Diccionari d'equivalències.
        "One" : 1,        
        "Two" : 2,
        "Three" : 3,
        "Four" : 4,
        "Five" : 5,
    }
    return equivalencies[numero] # Retorna el valor associat a la clau.