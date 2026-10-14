"""
Enunciado 7 – Extracción con Expresiones Regulares
Dada una lista de strings con información mezclada como:
['Ana García - edad:25 - tel:987654321', 'Luis Pérez - edad:30 - tel:912345678']
Usa expresiones regulares para extraer el nombre, la edad y el teléfono de cada registro
y almacénalos en una lista de diccionarios.
"""

import re

personas = [
    'Ana García - edad:25 - tel:987654321', 
    'Luis Pérez - edad:30 - tel:912345678'
]

#Patrón para capturar el nombre, la edad y el teléfono usando grupos
patron = r"^(.*?) - edad:(\d+) - tel:(\d+)$"

lista_dicc = []

for persona in personas:
    match = re.match(patron, persona)
    if match:
        nombre, edad, telefono = match.groups()
        lista_dicc.append({
            "nombre": nombre,
            "edad": int(edad),
            "telefono": telefono
        })

print("Lista de diccionarios con información de las personas:")
for persona in lista_dicc:
    print(persona)