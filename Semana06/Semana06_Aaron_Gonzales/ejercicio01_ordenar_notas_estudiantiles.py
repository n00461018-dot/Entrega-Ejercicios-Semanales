"""
Un profesor tiene las notas de 6 estudiantes en una lista desordenada:
[85, 42, 93, 67, 28, 75]
Se pide:
a) Ordenar la lista usando
Bubble Sort e imprimir el resultado.
b) Ordenar usando
Selection Sort e imprimir el resultado.
c) Mostrar la nota mínima, máxima y el promedio.

"""
def bubble_sort(lista):
    n = len(lista)
    for i in range(n):
        intercambiado = False
        for j in range(0, n-i-1):
            if lista[j] > lista[j+1]:
                lista[j], lista[j+1] = lista[j+1], lista[j]
                intercambiado = True
        if not intercambiado:
            break
        
def selection_sort(lista):
    n = len(lista)
    for i in range (n-1):
        idx_min = i
        for j in range(i+1, n):
            if lista[j] < lista[idx_min]:
                idx_min = j
        if idx_min != i:
            lista[i], lista[idx_min] = lista[idx_min], lista[i]
            
def estadistica_notas(lista):
    notaMin = min(lista)
    notaMax = max(lista)
    promedio = sum(lista) / len(lista)
    
    return notaMin, notaMax, promedio
                                
notasEst = [85, 42, 93, 67, 28, 75]
bubble_sort(notasEst)
print(f"Ordenamiento de la lista utilizando Bubble Sort: {notasEst}")

notasEst = [85, 42, 93, 67, 28, 75]
selection_sort(notasEst)
print(f"Ordenamiento de la lista utilizando Selection Sort: {notasEst}")

notaMin, notaMax, promedio = estadistica_notas(notasEst)

print(f"La nota mínima es: {notaMin}")
print(f"La nota máxima es: {notaMax}")
print(f"El promedio es: {promedio}")

