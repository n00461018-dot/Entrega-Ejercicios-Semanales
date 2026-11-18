# Funciones de orden superior
temperaturas = [0, 10, 20, 30, 40]

fahrenheit = list(map(lambda c: c * 9 / 5 + 32, temperaturas))

numeros = [1, 4, 7, 8, 10, 13, 16]
pares = list(filter(lambda x: x % 2 == 0, numeros))

desordenados = [25, 8, 15, 3, 20]
ordenados = sorted(desordenados)

print("Celsius:", temperaturas)
print("Fahrenheit:", fahrenheit)
print("Números pares:", pares)
print("Ordenados:", ordenados)