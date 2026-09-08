#calculadora de promedio

def calcular_promedio(notas):
    promedio = sum(notas) / cantidad
    nota_minima = min(notas)
    nota_maxima = max(notas)

    return promedio, nota_minima, nota_maxima


def mostrar_resultado(nombre, notas):
    promedio, minima, maxima = calcular_promedio(notas)

    print("----- REPORTE DE NOTAS -----")
    print("Nombre:", nombre)
    print("Notas:", notas)
    print("Promedio:", promedio)
    print("Nota mínima:", minima)
    print("Nota máxima:", maxima)


nombre = input("Ingrese el nombre del estudiante: ")

notas = []

cantidad = int(input("¿Cuántas notas desea ingresar?: "))

for i in range(cantidad):
    nota = float(input("Ingrese la nota: "))
    notas.append(nota)

mostrar_resultado(nombre, notas)