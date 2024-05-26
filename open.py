
name = input("Cual es tu nombre? ")

with open("nombre.txt", "a") as file:
    file.write(f"{name}\n")
    file.close()