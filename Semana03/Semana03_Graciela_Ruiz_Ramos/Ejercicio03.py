"""
=========================== EJERCICIO 03 ===========================
Escribe una función calcular_promedio(notas) que reciba una lista de 
notas y retorne el promedio, la nota mínima y la nota máxima.
Además crea una función mostrar_resultado(nombre, notas) sin retorno
que muestre un reporte formateado.
"""

#Resolución

def calcular_promedio(notas):
    promedio = sum(notas) / len(notas)
    minima = min(notas)
    maxima = max(notas)
    return promedio, minima, maxima

print("\n======== Calculadora de Promedios ========\n")
nombre_usuario = input("Ingresa el nombre del estudiante: ")

while True:
    try:
        cantidad_notas = int(input("¿Cuántas notas vas a ingresar?: "))
        if cantidad_notas >= 0:
            break
        print("Error: no se aceptan letras")
        print("=" * 51)
    except ValueError:
        print("Error: no se aceptan letras")
        print("=" * 51)

lista_notas = []
for i in range(cantidad_notas):
    while True:
        try:
            nota = float(input(f"Ingresa la nota {i + 1} (0 a 20): "))
            
        except ValueError:
            print("Error: no se aceptan letras")
            print("=" * 51)
            continue

        if 0 <= nota <= 20:
            lista_notas.append(nota)
            break  # Sale del bucle de validación y pasa a la siguiente nota
        else:
            print("Error:Nota fuera de rango. Debe estar entre 0 y 20.")
            print("=" * 51)

def mostrar_resultado(nombre, notas):
    prom, mn, mx = calcular_promedio(notas)
    
    print("\n" + "=" * 30)
    print(f"\n====== Reporte de Notas ======\n")
    print(f"Estudiante       : {nombre}")
    print(f"Notas ingresadas : {notas}")
    print(f"Promedio         : {prom:.2f}")
    print(f"Nota mínima      : {mn}")
    print(f"Nota máxima      : {mx}")
    print("\n" + "=" * 30)


mostrar_resultado(nombre_usuario, lista_notas)