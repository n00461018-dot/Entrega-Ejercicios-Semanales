## 07 Funciones de orden superior
# Sin for/while: usa map() para convertir Celsius a Fahrenheit, filter()
# para solo pares, sorted() con lambda para ordenar dicts por campo.
# Tip: list(map(lambda x: ..., lista)) sin bucles explícitos

# 1. Uso de map() para convertir una lista de temperaturas de Celsius a Fahrenheit
temperaturas_celsius = [0, 15, 25, 30, 37]
# Fórmula: (°C * 9/5) + 32
temperaturas_fahrenheit = list(map(lambda c: (c * 9/5) + 32, temperaturas_celsius))

print("--- 1. map() - Conversión de Celsius a Fahrenheit ---")
print(f"Celsius: {temperaturas_celsius}")
print(f"Fahrenheit: {temperaturas_fahrenheit}")


# 2. Uso de filter() para extraer únicamente los números pares de una lista
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
numeros_pares = list(map(int, filter(lambda x: x % 2 == 0, numeros))) # También se puede usar list(filter(...)) directamente

print("\n--- 2. filter() - Filtrar números pares ---")
print(f"Originales: {numeros}")
print(f"Pares: {list(filter(lambda x: x % 2 == 0, numeros))}")


# 3. Uso de sorted() con lambda para ordenar una lista de diccionarios por un campo específico
estudiantes = [
    {"nombre": "Ana", "promedio": 14.5},
    {"nombre": "Manuel", "promedio": 18.0},
    {"nombre": "Elias", "promedio": 12.0},
    {"nombre": "Carlos", "promedio": 16.5}
]

# Se ordenan los estudiantes de mayor a menor promedio usando 'key' con lambda
estudiantes_ordenados = sorted(estudiantes, key=lambda est: est["promedio"], reverse=True)

print("\n--- 3. sorted() con lambda - Ordenar diccionarios por campo ---")
print("Estudiantes ordenados por promedio (descendente):")
for est in estudiantes_ordenados:
    print(f"- {est['nombre']}: {est['promedio']}")