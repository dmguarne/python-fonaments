nom = input("Escriu el teu nom i prem Enter: ")
edat = int(input("Escriu la teva edat i prem Enter: "))
while edat < 0 or edat > 120:
    print("Edat no vàlida")
    edat = int(input("Torna a introduir la teva edat i prem Enter: "))
print("Edat acceptada")
altura = float(input("Escriu la teva altura i prem Enter: "))
gos = input("Escriu el nom del teu gos i prem Enter: ") 
edat_gos = int(input("Escriu l'edat del teu gos i prem Enter: "))

if edat < 18:
    print("Ets menor d'edat")
elif edat >=18 and edat <65:
    print("Ets adult")
else:
    print("Ets jubilat")

print(f"Em dic {nom}, tinc {edat} anys i faig {altura} metres d'altura. El meu gos es diu {gos} i té {edat_gos} anys")

