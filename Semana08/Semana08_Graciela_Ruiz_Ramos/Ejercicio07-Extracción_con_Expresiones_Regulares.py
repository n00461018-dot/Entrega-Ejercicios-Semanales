'''
======= Ejercicio 07 - Extracción con Expresiones Regulares =======
Dada una lista de strings con información mezclada como:
['Ana García - edad:25 - tel:987654321', 'Luis Pérez - edad:30 - tel:912345678']
Usa expresiones regulares para extraer el nombre, la edad y el teléfono de cada registro
y almacénalos en una lista de diccionarios.
'''

import re

datos_crudos = [
    'Ana García - edad:25 - tel:987654321', 
    'Luis Pérez - edad:30 - tel:912345678'
]

registros_limpios = []

patron = r'([A-Za-z áéíóúÁÉÍÓÚñÑ]+) - edad:(\d+) - tel:(\d+)'

for texto in datos_crudos:
    match = re.search(patron, texto)
    
    if match:
        nombre = match.group(1)
        edad = int(match.group(2))
        telefono = match.group(3)
        
        registros_limpios.append({
            'Nombre': nombre,
            'Edad': edad,
            'Teléfono': telefono
        })
print("\n==== REGISTROS CRUDOS ====\n")
for registro in datos_crudos:
    print(registro)

print("\n==== REGISTROS LIMPIOS ====\n")
for registro in registros_limpios:
    print(registro)

print("\n" + "=" * 42 + "\n")