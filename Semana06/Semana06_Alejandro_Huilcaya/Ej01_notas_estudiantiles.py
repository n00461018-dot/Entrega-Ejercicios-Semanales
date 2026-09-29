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

def selection_sort(lista):
    #Se guarda el valor total de elementos de la lista
    n = len(lista)
    #Se recorre hasta n-1 porque el último elemento queda ordenado solo
    for i in range(n - 1):
        #Se asigna un indice del valor menor inicial
        idx_min = i
        #Se busca un valor menor en el resto de la lista
        for j in range(i + 1, n):
            if lista[j] < lista[idx_min]:
                idx_min = j
        #Se intercambia el valor en idx_min con el de la posición i solo si son diferentes
        if idx_min != i:
            lista[i], lista[idx_min] = lista[idx_min], lista[i]
    print("Selection Sort:", lista)


def bubble_sort(lista):
    n = len(lista)
    
    for i in range(n):
        #Variable para saber si la lista ya está ordenada
        intercambiado = False
        for j in range(0, n - i - 1):
            if lista[j] > lista[j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
                intercambiado = True
        #Si no hubo intercambios, se termina el recorrido
        if not intercambiado:
            break
    print("Bubble Sort:   ", lista)


def estadisticas(lista):
    minima = min(lista)
    maxima = max(lista)
    promedio = sum(lista) / len(lista)
    print("Nota mínima:", minima)
    print("Nota máxima:", maxima)
    print("Promedio:   ", round(promedio, 2))


#Lista para bubble
notas = [85, 42, 93, 67, 28, 75]
bubble_sort(notas)

#Lista para seleccion
notas = [85, 42, 93, 67, 28, 75]
selection_sort(notas)

estadisticas(notas)