lineas = [
    "Joan,18,Lima",
    "Carlos,15,Trujillo",
    "Ana,17,Arequipa"
]

print("REPORTE")
print("-------")

for linea in lineas:
    datos = linea.split(",")

    nombre = datos[0]
    nota = datos[1]
    ciudad = datos[2]

    print("Nombre:", nombre)
    print("Nota:", nota)
    print("Ciudad:", ciudad)
    print()