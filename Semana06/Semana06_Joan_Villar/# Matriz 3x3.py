# Matriz 3x3

matriz = [
    [1, 3, 4],
    [5, 8, 9],
    [2, 6, 7]
]

print("Matriz original:")

for i in range(3):
    print(matriz[i])


# Recorremos toda la matriz
for i in range(3):
    for j in range(3):
        
        # Comparamos con los siguientes elementos
        for x in range(3):
            for y in range(3):
                
                if matriz[i][j] < matriz[x][y]:
                    
                    aux = matriz[i][j]
                    matriz[i][j] = matriz[x][y]
                    matriz[x][y] = aux


print("Matriz ordenada:")

for i in range(3):
    print(matriz[i])