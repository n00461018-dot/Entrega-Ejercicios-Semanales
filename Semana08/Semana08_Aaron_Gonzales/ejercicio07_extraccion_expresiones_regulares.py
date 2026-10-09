"""
Enunciado 7 – Extracción con Expresiones Regulares

Dada una lista de strings con información mezclada como:
['Ana García - edad:25 - tel:987654321', 'Luis Pérez - edad:30 - tel:912345678']
Usa expresiones regulares para extraer el nombre, la edad y el teléfono de cada registro
y almacénalos en una lista de diccionarios.
"""

import re

informacion = ['Ana García - edad:25 - tel:987654321', 'Luis Pérez - edad:30 - tel:912345678']

exp_reg = r"^(.+?)\s*-\s*edad:(\d+)\s*-\s*tel:(\d+)"
lista_inf = []

for info in informacion:
    coincidencia = re.search(exp_reg, info)
    if coincidencia:
        nombre = coincidencia.group(1).strip()
        edad = int(coincidencia.group(2))
        telefono = coincidencia.group(3)
        
        lista_inf.append({
            'nombre': nombre,
            'edad': edad,
            'telefono': telefono,
        })

print(lista_inf)