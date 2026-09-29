matriz = [
    [7, 100, 34],
    [22, 753, 1],
    [10, 43, 6]
]

lista = []

for fila in matriz:
    for numeros in fila:
        lista.append(numeros)
        
n = len(lista)
for i in  range(n - 1):
    for j in range(n-i-1):
        if lista[j] > lista[j+1]:
            lista[j], lista[j+1] = lista[j+1], lista[j]

k = 0
for r in range(3):
    for c in range(3):
        matriz[r][c] = lista[k]
        k += 1
        
for fila in matriz:
    print(fila)