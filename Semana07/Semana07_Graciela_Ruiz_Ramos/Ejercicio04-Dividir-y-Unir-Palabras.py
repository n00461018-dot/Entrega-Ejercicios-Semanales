'''
=== Ejercicio 04 - Dividir y Unir Palabras ===
Dada la cadena 'rojo,verde,azul,amarillo',
separa los colores, ponlos en mayúsculas y 
únelos con ' | ' como separador.
'''

cadena = 'rojo,verde,azul,amarillo'
cadena_separada = cadena.split(',')
cadena_mayusculas = [color.upper() for color in cadena_separada]
separador = " | ".join(cadena_mayusculas)

print(f"Cadena original: '{cadena}'")
print(f"Colores separados: {cadena_separada}")
print(f"Colores en mayúsculas: {cadena_mayusculas}")
print(f"Separador y resultado final: '{separador}'")
