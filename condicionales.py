# uso del "or"

nombre = input("Cual es tu nombre: ")

if nombre == "Harry" or nombre == "Ron" or nombre == "Hermione":
    print("Eres de Griffindor!")
elif nombre == "Draco":
    print("Eres de Slitherin")
else:
    print("Quien?")

#uso de "Match"

nombre = input("Cual es tu nombre: ")

match nombre:
    case "Harry":
        print("Eres de Grifindor!")
    case "Ron":
        print("Eres de Grifindor!")
    case "Hermion":
        print("Eres de Grifindor!")
    case "Draco":
        print("Eres de Slitherin!")
    case _:
        print("Quien?")

#uso de "Match" de forma mas ordenada 

nombre = input("Cual es tu nombre: ")

match nombre:
    case "Harry" | "Ron" | "Hermion" :
        print("Eres de Grifindor!")
    case "Draco":
        print("Eres de Slitherin!")
    case _:
        print("Quien?")
