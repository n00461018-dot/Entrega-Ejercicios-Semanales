"""
===================== EJERCICIO 08 =====================
Solicita N notas al usuario. Calcula el promedio, la
nota más alta, la más baja y cuántos estudiantes
aprobaron (nota >= 11). Muestra estadísticas completas.
"""
#Resolucion del ejercicio

notas = int(input("Cantidad de notas: "))
while notas <= 0:
    print("La cantidad de notas debe ser mayor a 0.")
    notas = int(input("Ingrese una cantidad válida: "))

suma = 0
nota_max = -1.0
nota_min = 21.0
aprobados = 0
desaprobados = 0 

for i in range(1, notas + 1):
    num = float(input(f"Ingrese la nota {i} de {notas}: "))

    while num < 0 or num > 20:
            print("Error: La nota debe estar entre 0 y 20.")
            num = float(input(f"Reingrese la nota {i} de {notas}: "))

    suma += num

    if num >= 11:
        aprobados += 1
    else:
        desaprobados += 1

    if num > nota_max:
        nota_max = num
    elif num < nota_min:
        nota_min = num

promedio = suma/notas

print("\n" + "=" * 35)
print(f"{'ESTADÍSTICAS COMPLETAS':^35}")
print("=" * 35)
print(f"Total de notas registradas : {notas}")
print(f"Promedio general           : {promedio:.2f}")
print(f"Nota más alta              : {nota_max:.2f}")
print(f"Nota más baja              : {nota_min:.2f}")
print(f"Estudiantes aprobados      : {aprobados}")
print(f"Estudiantes desaprobados   : {desaprobados}")
print("=" * 35)


