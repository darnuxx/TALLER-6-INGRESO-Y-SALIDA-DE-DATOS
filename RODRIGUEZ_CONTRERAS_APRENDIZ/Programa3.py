import os
import csv

print("===== LISTA DE ARCHIVOS =====")

ruta = "."

for archivo in os.listdir(ruta):

    if os.path.isfile(archivo):

        nombre, extension = os.path.splitext(archivo)

        print(f"Nombre: {nombre}")
        print(f"Extension: {extension}")
        print(f"Ruta: {os.path.abspath(archivo)}")
        print("-" * 40)

print("\n===== DATOS DEL CSV =====")

with open("Usuarios.csv", "r", encoding="utf-8") as archivo_csv:

    lector = csv.DictReader(archivo_csv, delimiter=';')

    for usuario in lector:

        print(f"Nombres: {usuario['Nombres']}")
        print(f"Apellidos: {usuario['Apellidos']}")
        print(f"Dependencia: {usuario['Dependencia']}")
        print(f"Estado: {usuario['Estado']}")

        total_columnas = len(usuario)

        print(f"Cantidad de columnas: {total_columnas}")

        print("-" * 40)
