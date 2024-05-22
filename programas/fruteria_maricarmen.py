#fruteria

print()
print("FRUTERIA MARICARMEN!")
print()
print("PLATANO")
print("POMELO")
print("MANZANA")
print("DURAZNOS")
print("PERA")
print("NARANJA")
print()

fruta = input("QUE FRUTA TE APETECE HOY?: ")
fruta_mayuscula = fruta.lower().strip()
print()
cantidad = int(input("CUANTAS PIEZAS DESEAS?: "))
print()

if fruta_mayuscula == "platano":
    costo_platano = round(cantidad * 0.5, 1)
    print("PRECIO TOTAL: ",costo_platano,"€")
elif fruta_mayuscula == "pomelo":
    costo_pomelo = round(cantidad * 0.4, 1)
    print("PRECIO TOTAL: ",costo_pomelo,"€")
elif fruta_mayuscula == "manzana" or fruta_mayuscula == "naranja":
    costo_manzana_naranja = round(cantidad * 0.3, 1)
    print("PRECIO TOTAL: ",costo_manzana_naranja,"€")
elif fruta_mayuscula == "durazno" or fruta_mayuscula == "pera":
    costo_durazno_pera = round(cantidad * 0.2, 1)
    print("PRECIO TOTAL: ",costo_durazno_pera,"€")
else :
    print("NO DISPONEMOS DE ESE PRODUCTO")

if 1<= cantidad <=5:
    print ("NECESITAS UNA BOLSA PEQUEÑA ")
elif 6<= cantidad <= 10:
    print ("NECESITAS UNA BOLSA MEDIANA ")
elif 11<= cantidad <= 15:
    print ("NECESITAS UNA BOLSA GRANDE ")
elif 15< cantidad:
    print ("NECESITAS UNA BOLSA GRANDE MAS UNA BOLSA EXTRA ")
else:
    print()
