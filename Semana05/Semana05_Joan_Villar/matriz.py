matriz = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]]

# Suma de cada fila
for fila in matriz:
    print("Suma de fila:", sum(fila))

# Suma de cada columna
for columna in range(3):
    suma = 0

    for fila in range(3):
        suma += matriz[fila][columna]

    print("Suma de columna:", suma)