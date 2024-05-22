def main ():
    x = int(input("Ingrese un numero: "))
    y = int(input("Ingrese un numero: "))
    if numero_mayor(x,y):
        print(f"{x}Es el numero mayor")
    elif numero_mayor(y):
        print(f"{y}Es el numero mayor")

def numero_mayor(x,y):
    if x > y: 
        print(f"{x}Es el numero mayor")
    elif y > x:
        print(f"{y}Es el numero mayor")

main()
