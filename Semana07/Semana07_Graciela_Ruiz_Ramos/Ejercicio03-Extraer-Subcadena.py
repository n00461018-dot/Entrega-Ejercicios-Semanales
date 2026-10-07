'''
=== Ejercicio 03 - Extraer Subcadena ===
Dada la cadena 'Análisis de Datos con Python', 
extrae las palabras 'Datos' y 'Python' usando slicing
'''

cadena = 'Análisis de Datos con Python'
subcadena_datos = cadena[12:17]
subcadena_python = cadena[22:28]
print(f"Cadena Principal: '{cadena}'")
print(f"Primera subcadena extraida es: '{subcadena_datos}'")
print(f"Segunda subcadena extraida es: '{subcadena_python}'")