"""
EJERCICIO 07: Funciones de orden superior

Sin for/while: usa map() para convertir Celsius→Fahrenheit, filter()
para solo pares, sorted() con lambda para ordenar dicts por campo.

Tip: list(map(lambda x: ..., lista)) — sin bucles explícitos
""" 

temperaturas_celsius = [0, 20, 37, 100]
temperaturas_fahrenheit = list(map(lambda x: (x * 9/5) + 32, temperaturas_celsius))
print(temperaturas_fahrenheit)

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
numeros_pares = list(filter(lambda x: x % 2 == 0, numeros))
print(numeros_pares)

estudiantes = [
    {"nombre": "Aaron", "edad": 20},
    {"nombre": "Charly", "edad": 27},
    {"nombre": "Carlos", "edad": 50}
]
estudiantes_ordenados = sorted(estudiantes, key=lambda x: x["edad"])
print(estudiantes_ordenados)
