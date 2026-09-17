"""
Dada la matriz 3×3: [[1,2,3],[4,5,6],[7,8,9]] — Calcular y mostrar la suma de cada fila y la suma de cada columna.
"""
def calculo_suma(matriz):
    
    suma_fila = []
    suma_columna = []
    
    for i in range(0, 3):
    
        filas = 0
        columnas = 0
        
        for j in range(0 ,3):
            
            filas += matriz[i][j]
            columnas += matriz[j][i]  
            
        suma_fila.append(filas)
        suma_columna.append(columnas)
    
    return suma_fila, suma_columna
    
matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
]

suma_fila, suma_columna = calculo_suma(matriz)

for i, valor in enumerate(suma_fila):
    print(f"fila {i}: {valor}")

for i, valor in enumerate(suma_columna):
    print(f"columna {i}: {valor}")
    


