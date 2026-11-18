"""
============= Ejercicio 07 =============

Sin for/while: usa map() para convertir Celsius→Fahrenheit, 
filter() para solo pares, sorted() con lambda para ordenar 
dicts por campo.

Tip: list(map(lambda x: ..., lista)) — sin bucles explícitos
"""

#map(): Convertir Celsius a Fahrenheit [C * 9/5 + 32]
celsius = [0, 10, 20, 30, 40]
fahrenheit = list(map(lambda c: c * 9/5 + 32, celsius))
print("Fahrenheit:", fahrenheit)

#filter(): Filtrar solo números pares
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
pares = list(filter(lambda x: x % 2 == 0, numeros))
print("Pares:", pares)

#sorted() con lambda: Ordenar lista de diccionarios por edad
personas = [
    {"nombre": "Carlos", "edad": 25},
    {"nombre": "Ana", "edad": 22},
    {"nombre": "Beatriz", "edad": 28}
]
personas_ordenadas = sorted(personas, key=lambda p: p['edad'])
print("Ordenados por edad:", personas_ordenadas)