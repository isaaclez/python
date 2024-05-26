estudiantes = []

with open("alumnos.csv") as file:
    for line in file:
        nombre, casa = line.rstrip().split(",")
        estudiante = {"nombre": nombre, "casa": casa}
        estudiantes.append(estudiante)

def dame_nombre(estudiante):
    return estudiante["nombre"]

for estudiante in sorted(estudiantes, key=dame_nombre):
    print(f"{estudiante['nombre']} esta en {estudiante['casa']}")