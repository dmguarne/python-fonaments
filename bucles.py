## després de mostrar la taula de multiplicar, el programa ha de dir quants números de la taula són parells i quants són senars.
valor = int(input("Introdueix un número del 1 al 10 i prem Enter: "))
parells = 0
while valor < 1 or valor > 10:
    print("El número ha d'estar entre 1 i 10")
    valor = int(input("Introdueix un número del 1 al 10 i prem Enter: "))
for numero in range(1, 11):
    
    print(f"{valor} x {numero} = {valor * numero}")
    if int(valor * numero) / 2 == 1:
        parells = + 1

print(f"Hi ha un total de {parells} números parells")