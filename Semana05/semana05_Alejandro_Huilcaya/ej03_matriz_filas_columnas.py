"""
Dada la matriz 3×3: [[1,2,3],[4,5,6],[7,8,9]] — Calcular y mostrar la suma de cada fila y la suma de cada columna.
"""


matriz=[
[1,2,3],
[4,5,6],
[7,8,9]
]

def calcular_sumas_matriz(matriz):
    row = len(matriz)
    cols = len(matriz[0])
    fila_sum = 0

    for i in range(row):
        # Se suma los valores de cada elemento en la fila
        fila_sum = sum(matriz[i])
        print(f"Suma fila {i}: {fila_sum} |", end=" ")

    for i in range(cols):
        # Se reinicia a 0 en cada nueva columna
        colum_sum = 0
        # Recorre y suma cada elemento de la columna i por cada fila
        for j in range(row):
            colum_sum += matriz[j][i]

        print(f"| Suma columna {i}: {colum_sum} ", end=" ")


calcular_sumas_matriz(matriz)