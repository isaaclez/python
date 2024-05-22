# end="" llama a la ultima linea del codigo y la sube donde esta 
name = input("What's your name? ")
print("hello,", end="") 
print(name)

# el slash invertido mas comilla ( \" ) sirve para indicar comillas y evitar que el codigo de error
print("hello, \"friend\"")

# la "f" indica a python que trate esta cadena de manera especial haciendo que respete su caracter de variable frente a las comillas
name = input("What's your name? ")
print(f"hello, {name}. Como etas ?")

# strip Remove whitespace from the str # Title () Aplica mayuscula al inicio de cada palabra
name = input("What's your name? ").strip().title() 
firts, second, last = name.split(" ")
print("hello", second)

# round() es la funcion que redondea el resultado 
x = float(input("x: ")) 
y = float(input("y: "))

z = round(x / y)
print(z)
# imprimira un numero entero aproximado

# round( ,2) define con el 2 la cantidad de decimales que va a imprimir
x = float(input("x: ")) 
y = float(input("y: "))

z = round(x / y, 2)
print(z)
#imprimira un numero con dos decimales

#podemos indicarle que ponga una coma cada 1,000
x = float(input("x: ")) 
y = float(input("y: "))

z = round(x * y)
print(f"{z:,}")