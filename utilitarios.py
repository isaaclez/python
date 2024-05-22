
#funciones pre establecidas en python

#FUNCION MAX = INDICA CUAL ES EL MAYOR TANTO EN NUMERO COMO EN CADENA SEGUN LA CANTIDAD DE CARACTERES
p= int(input("escribe un numero: "))
a= int(input("escribe otro numero: "))
print(max(p,a))

#FUNCION MIN = INDICA CUAL ES EL MENOR, TANTO PARA NUMERO COMO PARA CADENA DE TEXTO 

y= int(input("escribe un numero: "))
l= int(input("escribe otro numero: "))
print(min(y,l))

#FUNCION LEN = INDICA LA CANTIDAD DE CARACTERES EN UNA CADENA DE TEXTO

x= str(input("escribe una palabra: "))
z= str(input("escribe otra palabra: "))
resultado = int(max(x,z))
print(resultado)
print("la palabra tiene",len(resultado),"letras")

#la funcion "sep" sirve para separar los elementos con el caracter indicado entre comillas
print("hola" * 3, sep=", ")