'''
==== Ejercicio 10 - Análisis de Texto y Estadísticas de Palabras ====
Dado un párrafo de texto, implementa un analizador completo que:
1) Extraiga todas las palabras usando regex (solo letras y apóstrofes).
2) Construya un diccionario con la frecuencia de cada palabra (sin importar mayúsculas).
3) Ordene por frecuencia (desc) y luego alfabéticamente para desempates.
4) Muestre el top 5 de palabras más frecuentes y las palabras únicas ordenadas.
'''

import re

texto = "El gato de la casa es un gato muy ágil. ¡La casa del gato no es tu casa!"

patron = r"[A-Za-záéíóúÁÉÍÓÚñÑ']+"
palabras = re.findall(patron, texto)

frecuencias = {}
for palabra in palabras:
    palabra_minuscula = palabra.lower()
    frecuencias[palabra_minuscula] = frecuencias.get(palabra_minuscula, 0) + 1

palabras_ordenadas = sorted(frecuencias.items(), key=lambda x: (-x[1], x[0]))

print("\n==== PÁRRAFO DE TEXTO ====\n")
print(texto)

print("\n==== TOP 5 PALABRAS MÁS FRECUENTES ====\n")
top_5 = palabras_ordenadas[:5]
for palabra, frec in top_5:
    print(f"'{palabra}': {frec} veces")

print("\n==== PALABRAS ÚNICAS ORDENADAS ====\n")
palabras_unicas = sorted(frecuencias.keys())
print(", ".join(palabras_unicas))
print("\n")