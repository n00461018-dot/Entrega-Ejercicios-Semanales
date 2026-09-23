"""
=========================== Ejercicio 01 ================================
                Estadísticas de una Lista de Notas
Enunciado:
Dado el siguiente arreglo de notas: [15, 18, 12, 9, 17, 14, 20, 11, 16, 13]
Escribir un programa que calcule: promedio, nota más alta, nota más baja y 
cuántos aprobaron (nota ≥ 11).
===========================================================================
"""

Notas = [15, 18, 12, 9, 17, 14, 20, 11, 16, 13]

Suma = 0
Nota_Max = Notas[0]
Nota_Min = Notas[0]
Aprobados = 0

for nota in Notas:
    Suma += nota
    if nota > Nota_Max:
        Nota_Max = nota
    if nota < Nota_Min:
        Nota_Min = nota

    if nota >= 11:
        Aprobados += 1

promedio = Suma / len(Notas)

print("=" * 47)
print("Estadísticas de una Lista de Notas")
print(f"Notas: {Notas}")
print("=" * 47)
print(f"Promedio de notas    : {promedio:.2f}")
print(f"Nota máxima          : {Nota_Max}")
print(f"Nota mínima          : {Nota_Min}")
print(f"Cantidad de aprobados: {Aprobados}")
print("=" * 47)

#Graciela Ruiz