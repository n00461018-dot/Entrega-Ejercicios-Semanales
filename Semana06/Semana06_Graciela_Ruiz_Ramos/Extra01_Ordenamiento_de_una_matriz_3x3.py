'''
========== Ordenar una Matriz 3x3 ===========
Dada una matriz de 3x3 con números desordenados, se pide:
1) Ordenar todos los números de la matriz de menor a mayor.
2) Imprimir la matriz original desordenada y ordenada.
'''

def ordenar_matriz(matriz):

    lista_lineal = []
    for fila in matriz:
        for numero in fila:
            lista_lineal.append(numero)
            
    lista_lineal.sort() 
    
    matriz_ordenada = []
    indice = 0
    filas = len(matriz)       
    columnas = len(matriz[0]) 
    
    for i in range(filas):
        nueva_fila = []
        for j in range(columnas):
            nueva_fila.append(lista_lineal[indice])
            indice += 1
        matriz_ordenada.append(nueva_fila) 
        
    return matriz_ordenada

matriz_original = [
    [9, 3, 1],
    [8, 5, 9],
    [7, 0, 0]
]

print("Matriz Original (Desordenada):")
for fila in matriz_original:
    print(fila)

matriz_final = ordenar_matriz(matriz_original)

print("\nMatriz Original (Ordenada):")
for fila in matriz_final:
    print(fila)