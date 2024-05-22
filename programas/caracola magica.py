#caracola magica
import random
import os
import time

def randomFunc():
    input("Cual es tu pregunta? ")
    print("La respuesta es: ")

    respuesta = ""
    selec = random.randint(0, 9)
    #print(f"El valor del random es: {selec}")
    #time.sleep(3)
    
    if selec <5:
        print("si")
    else:
        print("no")
    
    return(True)

while True:
    os.system('cls' if os.name == 'nt' else 'clear')
    randomFunc()
    exitStr = int(input ("Quieres salir? (0/1)"))
    print(type(exitStr))
    if exitStr == 0 :
        exit()