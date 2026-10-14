# Ejercicio 8 - Sistema de calificaciones

# Lista de estudiantes
estudiantes = ["Carlos", "Ana", "Luis", "Maria"]

# Diccionario con materias y notas
notas = {
    "Matematica": [15, 18, 14, 17],
    "Programacion": [16, 19, 13, 18],
    "Base de Datos": [17, 18, 15, 16]
}

# Funcion para calcular el promedio por materia
def promedio_materia(lista_notas):
    total = 0

    for nota in lista_notas:
        total = total + nota

    return total / len(lista_notas)


# Funcion para encontrar al mejor estudiante
def mejor_estudiante(lista_notas, estudiantes):
    mayor_nota = lista_notas[0]
    nombre_mejor = estudiantes[0]

    for i in range(len(lista_notas)):
        if lista_notas[i] > mayor_nota:
            mayor_nota = lista_notas[i]
            nombre_mejor = estudiantes[i]

    return nombre_mejor, mayor_nota


# Funcion para generar el reporte general
def reporte_general(estudiantes, notas):
    reporte = []

    for i in range(len(estudiantes)):
        total = 0

        for materia in notas:
            total = total + notas[materia][i]

        promedio = total / len(notas)

        reporte.append({
            "nombre": estudiantes[i],
            "promedio": promedio
        })

    # Ordenar de mayor a menor
    reporte.sort(key=lambda x: x["promedio"], reverse=True)

    print("\nRANKING GENERAL")

    posicion = 1

    for estudiante in reporte:
        print(posicion, "-", estudiante["nombre"],
              "- Promedio:", round(estudiante["promedio"], 2))
        posicion = posicion + 1


# Mostrar promedios por materia
print("PROMEDIOS POR MATERIA")

for materia in notas:
    promedio = promedio_materia(notas[materia])
    print(materia, "- Promedio:", round(promedio, 2))


# Mostrar mejor estudiante de cada materia
print("\nMEJOR ESTUDIANTE POR MATERIA")

for materia in notas:
    nombre, nota = mejor_estudiante(notas[materia], estudiantes)
    print(materia, "-", nombre, "- Nota:", nota)


# Mostrar ranking general
reporte_general(estudiantes, notas)