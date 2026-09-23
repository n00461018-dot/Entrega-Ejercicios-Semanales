"""
=========================== Ejercicio 03 ================================
                Suma de Filas y Columnas de una Matriz
Enunciado:
Dada la matriz 3x3: [[1, 2, 3],
                     [4, 5, 6],
                     [7, 8, 9]] 
— Calcular la suma de cada fila y la suma de cada columna.
===========================================================================
"""

matriz = [
    [1, 2, 3], 
    [4, 5, 6], 
    [7, 8, 9]
]

filas = len(matriz)
columnas = len(matriz[0])
print("=" * 18)

print("SUMA POR FILAS")
for i in range(filas):
    suma_de_filas = 0
    for j in range(columnas):
        suma_de_filas += matriz[i][j]
    print(f"Suma fila {i}: {suma_de_filas}")

print("=" * 18)

print("SUMA POR COLUMNAS")
for j in range(columnas):
    suma_de_columnas = 0
    for i in range(filas):
        suma_de_columnas += matriz[i][j]
    print(f"Suma columna {j}: {suma_de_columnas}")
print("=" * 18)

#Graciela Ruiz