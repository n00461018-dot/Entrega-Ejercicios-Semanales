"""
======================= EJERCICIO 1 – ORDENAR NOTAS ESTUDIANTILES =========================
Un profesor tiene las notas de 6 estudiantes en una lista desordenada:
[85, 42, 93, 67, 28, 75]
Se pide:
a) Ordenar la lista usando Bubble Sort e imprimir el resultado.
b) Ordenar usando Selection Sort e imprimir el resultado.
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
    for i in range (n - 1):          
        idx_min = i                   
        for j in range (i + 1, n):     
            if lista [j] < lista[idx_min]:  
                idx_min = j            
        
        if idx_min != i:
            lista[i], lista[idx_min] = lista[idx_min], lista[i]


notas = [85, 42, 93, 67, 28, 75]

promedio = sum(notas)/len(notas)

print("=" * 32 + "\n")
notas_burbuja = notas.copy()
bubble_sort(notas_burbuja)
print(f"Ordenamiento con bubble_sort")
print(notas_burbuja, "\n")

notas_seleccion = notas.copy()
selection_sort(notas_seleccion)
print(f"Ordenamiento con selection_sort")
print(notas_seleccion, "\n")
print("=" * 32)
print(f"Nota mínima         : {min(notas)}")
print(f"Nota máxima         : {max(notas)}")
print(f"Promedio de notas   : {promedio:.2f}")
print("=" * 32)

