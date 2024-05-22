#programa para saber si un numero es primo

print()
numero = int(input("ESCRIBA UN NÚMERO: "))

reciduo = numero % 2

print()
if reciduo !=0 :
   print("EL NÚMERO ES PRIMO")
elif numero == 2:
    print("EL NÚMERO ES PRIMO")
else :
   print("EL NÚMERO NO ES PRIMO")

print()

