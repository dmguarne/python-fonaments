import re

input_usuari = input("Escriu una definició de funció vàlida: \n")

if re.search(r"def\s\w+\((\w*,(\s)?)*\w*\):$", input_usuari):
    print("Definició de funció detectada")
else:
    print("No és una definició de funció")
