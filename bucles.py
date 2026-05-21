valor = int(input("Introdueix un número del 1 al 10 i prem Enter: "))
while valor < 1 or valor > 10:
    print("El número ha d'estar entre 1 i 10")
    valor = int(input("Introdueix un número del 1 al 10 i prem Enter: "))
for numero in range(1, 11):
    print(f"{valor} x {numero} = {valor * numero}")