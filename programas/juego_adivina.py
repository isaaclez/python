
import random

def juego_adivinanzas():
    numero_secreto = random.randint(1, 10)
    intentos = 0
    while True :
        intento = int(input("Adivina el numero entre 1 y 10: "))
        intentos += 1
        if intento < numero_secreto:
            print("Demasiado bajo, intenta de nuevo.")
        elif intento > numero_secreto:
            print("Demasiado alto, intentalo de nuevo.")
        else:
            print(f"CORRECTO! LO LOGRASTE EN {intentos} INTENTOS!")
            break

juego_adivinanzas()