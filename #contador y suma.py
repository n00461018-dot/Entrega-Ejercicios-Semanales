#contador y suma
contador = 0
suma = 0

for numero in range(1, 21):
    if numero % 2 == 0:
        contador = contador + 1
        suma = suma + numero

print("Numeros pares:", contador)
print("Suma total:", suma)