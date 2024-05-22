
#funcion con ingreso de datos
def dihola():
    nombre = str(input("cual es tu nombre?: ")).upper().strip()
    print("HELLO", nombre)

dihola()

#funcion con parametro definido por una variable
def hola_con_nombre(name):
    print(f"HELLO {name}!" )

hola_con_nombre("ADA")

#funcion con multiples parametros con una setencia de retorno
def multiplica(val1, val2):
    return val1 * val2
#si la funcion incluye parametros debe proporcionar -
#el mismo numero de parametros cuando llame la funcion
print(multiplica(3,5)) 

#python interpretara que el valor de ese parametro
#es el predeterminado si no se proporciona ninguno
def suma(a, b=3):
    return a + b
result = suma(3, b=2)
#asume que ese "3" le pertence a "a"
#siempre un argumento de palabra clave "b=2" debe ir despues de uno
#que no sea palabra clave "3"
print(result)

#podemos usar una variable com ofuncion "s" asignandole ducha funcion
#a una variable "s = suma"
s = suma
result_dos = s(1,2)
print(result_dos)


