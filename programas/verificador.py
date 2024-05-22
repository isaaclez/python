import sys


def main():
    valor_a = verificador_uno()
    valor_b = verificador_dos()
    print("EL RESULTADO ES:", valor_a + valor_b)


def verificador_uno():
    while True:
        try:
            valor_a = int(input("INGRESE EL VALOR A: "))
            return valor_a
        except ValueError:
            print("NO ES UN NUMERO ENTERO. VUELVA A INTENTARLO")


def verificador_dos():
    while True:
        try:
            valor_b = int(input("INGRESE EL VALOR B: "))
            return valor_b
        except ValueError:
            print("EL VALOR NO ES UN NUMERO ENTERO. VUELVA A INTENTARLO")


main()
print()

sys.exit("fin del programa")
