# Ejercicio 10 - Analisis de texto y estadisticas

import re

# Parrafo de ejemplo
texto = """
Python es un lenguaje de programacion.
Python permite crear programas y aprender programacion.
Aprender Python es importante para los estudiantes.
La programacion permite resolver problemas.
"""

# Extraer las palabras usando expresiones regulares
palabras = re.findall(r"[^\W\d_]+(?:'[^\W\d_]+)*", texto.lower())

# Crear diccionario de frecuencias
frecuencias = {}

for palabra in palabras:
    if palabra in frecuencias:
        frecuencias[palabra] = frecuencias[palabra] + 1
    else:
        frecuencias[palabra] = 1

# Ordenar por frecuencia y luego alfabeticamente
ordenadas = sorted(
    frecuencias.items(),
    key=lambda x: (-x[1], x[0])
)

# Mostrar las 5 palabras mas frecuentes
print("TOP 5 DE PALABRAS MAS FRECUENTES")

for palabra, cantidad in ordenadas[:5]:
    print(palabra, "-", cantidad, "veces")

# Mostrar palabras unicas ordenadas alfabeticamente
unicas = sorted(frecuencias.keys())

print("\nPALABRAS UNICAS ORDENADAS")

for palabra in unicas:
    print(palabra)

# Mostrar estadisticas generales
print("\nESTADISTICAS")
print("Total de palabras:", len(palabras))
print("Cantidad de palabras diferentes:", len(unicas))