matriz=[
[1,3,4],
[5,8,9],
[2,6,7]         
]
print("Matriz inicial:",matriz)

def ordenar_matriz_asc(matriz):
    filas = len(matriz)
    columnas = len(matriz[0])

    #recorrer cada fila usando i
    for i in range(filas):
        #recorrer cada columna usando j
        for j in range(columnas):

            #se crea el valor minimo como matriz[i][j] de forma temporal
            min_i = i
            min_j = j

            #revisar el resto de la fila actual
            for l in range(j, columnas):
                #si el elemento en la fila actual es menor, actualiza min_i y min_j
                if matriz[i][l] < matriz[min_i][min_j]:
                    min_i = i
                    min_j = l

            #se recorre las siguientes filas (i+1) usando k
            for k in range(i + 1, filas):
                #recorrer las columnas usando l
                for l in range(columnas):
                    #si encuentra un elemento menor en las filas inferiores, guarda k y l como minimo
                    if matriz[k][l] < matriz[min_i][min_j]:
                        min_i = k
                        min_j = l

            #se intercambian los valores de la matriz
            matriz[i][j], matriz[min_i][min_j] = matriz[min_i][min_j], matriz[i][j]

ordenar_matriz_asc(matriz)
print("Matriz ordenada",matriz)


