# DESCUENTOS APLICADOS
print()
precio_producto = float(input("INGRESE EL PRECIO DEL PRODUCTO: "))
print()
print("CATEGORIAS")
print()
print("ALIMENTOS")
print("NIÑOS")
print("MODA")
print("LICORES")
print("DEPORTE")
print("COMIDA PREPARADA")
print()
categoria = input("INGRESE LA CATEGORIA DEL PRODUCTO: ")
print()
categoria_mayuscula = categoria.lower().strip()

descuento_alimentos = precio_producto * 20 / 100
precio_final_alimentos = precio_producto - descuento_alimentos

descuento_moda = precio_producto * 15 / 100
precio_final_moda = precio_producto - descuento_moda

descuento_licores = precio_producto * 30 / 100
precio_final_licores = precio_producto - descuento_licores

descuento_deporte = precio_producto * 20 / 100
precio_final_deporte = precio_producto - descuento_deporte

if categoria_mayuscula == "alimentos":
    print("DESCUENTO:-",round(descuento_alimentos,2),"€")
    print()
    print("EL PRECIO FINAL ES:",round(precio_final_alimentos,2),"€")
elif categoria_mayuscula == "moda":
    print("DESCUENTO:-",round(descuento_moda,2),"€")
    print()
    print("EL PRECIO FINAL ES:",round(precio_final_moda,2),"€")
elif categoria_mayuscula == "licores":
    print("DESCUENTO:-",round(descuento_licores,2),"€")
    print()
    print("EL PRECIO FINAL ES:",round(precio_final_licores,2),"€")
elif categoria_mayuscula == "deporte":
    print("DESCUENTO:-",round(descuento_deporte,2),"€")
    print()
    print("EL PRECIO FINAL ES:",round(precio_final_deporte,2),"€")
elif categoria_mayuscula == "niños" or categoria_mayuscula == "comida preparada":
    print("LA CATEGORIA NO TIENE DESCUENTO")
    print()
    print("EL PRECIO FINAL ES:",round(precio_producto,2),"€")
else:
    print("PERDONA, NO CONTAMOS CON ESA CATEGORIA")