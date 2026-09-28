
# Notas de los 6 estudiantes
notas = [85, 42, 93, 67, 28, 75]


# A) Ordenamiento usando Bubble Sort
bubble = notas.copy()

for i in range(len(bubble)):
    for j in range(len(bubble) - 1 - i):

        # Si la nota de la izquierda es mayor,
        # se cambian de posición
        if bubble[j] > bubble[j + 1]:
            aux = bubble[j]
            bubble[j] = bubble[j + 1]
            bubble[j + 1] = aux

print("Notas ordenadas con Bubble Sort:")
print(bubble)


# B) Ordenamiento usando Selection Sort
selection = notas.copy()

for i in range(len(selection)):

    # Al inicio suponemos que la menor está en i
    menor = i

    for j in range(i + 1, len(selection)):

        if selection[j] < selection[menor]:
            menor = j

    # Cambiamos la posición de la nota menor
    aux = selection[i]
    selection[i] = selection[menor]
    selection[menor] = aux

print("\nNotas ordenadas con Selection Sort:")
print(selection)


# C) Nota mínima, máxima y promedio

nota_minima = min(notas)
nota_maxima = max(notas)
promedio = sum(notas) / len(notas)

print("\nNota mínima:", nota_minima)
print("Nota máxima:", nota_maxima)
print("Promedio:", promedio)


#Resultado:

#Notas ordenadas con Bubble Sort:
#[28, 42, 67, 75, 85, 93]

#Notas ordenadas con Selection Sort:
#[28, 42, 67, 75, 85, 93]

#Nota mínima: 28
#Nota máxima: 93
#Promedio: 65.0