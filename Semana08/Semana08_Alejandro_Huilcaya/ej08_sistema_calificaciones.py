"""
Enunciado 8 – Sistema de Calificaciones con Estructuras Combinadas
Crea un sistema que maneje un diccionario de listas donde las claves son materias
y los valores son listas de notas de estudiantes (arreglos paralelos con lista de nombres).
Implementa funciones para: calcular el promedio por materia, encontrar al mejor estudiante
de cada materia y generar un reporte ordenado por promedio general de mayor a menor.
"""

estudiantes = ["Ana", "Luis", "Carlos", "Sofía"]

cursos = {
    "Matemáticas": [15, 18, 12, 16],
    "Historia": [14, 12, 19, 17],
    "Programación": [18, 16, 15, 20]
}

def sistema_notas(estudiantes, cursos):

    #Promedio por curso
    promedio_cursos = {}
    for curso, notas in cursos.items():
        promedio_cursos[curso] = sum(notas) / len(notas)
    
    #Mejor estudiante por curso
    mejores = {}
    for curso, notas in cursos.items():
        max_nota = max(notas)
        max_ind = notas.index(max_nota)
        mejores[curso] = {"estudiante": estudiantes[max_ind], "nota": max_nota}
        
    #Reporte general 
    reporte_general = []
    for i, nombre in enumerate(estudiantes):

        notas_alumno = []
        for notas in cursos.values():
            notas_alumno.append(notas[i])

        prom = sum(notas_alumno) / len(notas_alumno)
        reporte_general.append({"nombre": nombre, "promedio": prom})
        
    reporte_ordenado = sorted(reporte_general, key=lambda x: x['promedio'], reverse=True)
    
    #Se muestra los resultados de los diccionarios y lista
    print("--- PROMEDIO POR CURSO ---")
    for curso, prom in promedio_cursos.items():
        print(f"- {curso}: {prom:.1f}")

    print("\n--- MEJOR ESTUDIANTE POR CURSO ---")
    for curso, info in mejores.items():
        print(f"- {curso}: {info['estudiante']} ({info['nota']})")

    print("\n--- REPORTE GENERAL ---")
    
    for i, est in enumerate(reporte_ordenado, start=1):
        print(f"{i}° {est['nombre']} - Promedio: {est['promedio']:.1f}")


sistema_notas(estudiantes, cursos)