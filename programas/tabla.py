#LOOPS
s = float(input("DIGITE EL NUMERO A MULTIPLICAR: "))
w = int(input("DESDE QUE NUMERO QUIERES MULTIPLICARLO: "))
y = int(input("HASTA QUE NUMERO DESEAS MULTIPLICARLO?: "))
condicion = input("EL NUMERO ES UN ENTERO? SI/NO: ")
condicion_minuscula = condicion.lower().strip()

if condicion_minuscula == "si":
    for x in range(w,y+1):
        print (f"{x} x {round(s)} =",int(x * s))

elif condicion_minuscula == "no": 
    for x in range(w,y+1):
        print (f"{x} x {s} =",round(x * s,2))
else:
    print("SOLO ADMITO COMO RESPUESTA: SI/NO")