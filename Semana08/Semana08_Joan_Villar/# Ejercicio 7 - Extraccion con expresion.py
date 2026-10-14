# Ejercicio 7 - Extraccion con expresiones regulares

import re

# Lista con informacion de personas
registros = [
    "Ana García - edad:25 - tel:987654321",
    "Luis Pérez - edad:30 - tel:912345678"
]

# Lista vacia para guardar los datos
personas = []

# Recorrer cada registro
for registro in registros:

    nombre = re.search(r"^(.+?) - edad:", registro)
    edad = re.search(r"edad:(\d+)", registro)
    telefono = re.search(r"tel:(\d+)", registro)

    # Guardar los datos en un diccionario
    if nombre and edad and telefono:
        persona = {
            "nombre": nombre.group(1),
            "edad": int(edad.group(1)),
            "telefono": telefono.group(1)
        }

        personas.append(persona)

# Mostrar los resultados
print("LISTA DE PERSONAS")

for persona in personas:
    print("Nombre:", persona["nombre"])
    print("Edad:", persona["edad"])
    print("Telefono:", persona["telefono"])
    print("------------------------")

print("Lista de diccionarios:")
print(personas)