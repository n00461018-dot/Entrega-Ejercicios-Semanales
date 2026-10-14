'''
======= Ejercicio 08 - Sistema de Calificaciones con Estructuras Combinadas =======
Crea un sistema que maneje un diccionario de listas donde las claves son materias
y los valores son listas de notas de estudiantes (arreglos paralelos con lista de nombres).
Implementa funciones para: calcular el promedio por materia, encontrar al mejor estudiante
de cada materia y generar un reporte ordenado por promedio general de mayor a menor.
'''

nombres = ["Ana", "Luis", "Mía", "Juan"]
sistema_calificaciones = {
    "Matemáticas": [16, 14, 19, 12],
    "Programación": [18, 15, 20, 16],
    "Física": [14, 16, 18, 15]
}

def calcular_promedios_materias(calificaciones):
    promedios = {}
    for materia, notas in calificaciones.items():
        promedio = sum(notas) / len(notas)
        promedios[materia] = round(promedio, 2)
    return promedios

def encontrar_mejores_estudiantes(nombres, calificaciones):
    mejores = {}
    for materia, notas in calificaciones.items():
        nota_maxima = max(notas)
        indice_max = notas.index(nota_maxima)
        mejor_estudiante = nombres[indice_max]
        mejores[materia] = {"estudiante": mejor_estudiante, "nota": nota_maxima}
    return mejores

def generar_reporte_ordenado(nombres, calificaciones):
    reporte = []
    
    for i in range(len(nombres)):
        suma_notas = 0
        for notas in calificaciones.values():
            suma_notas += notas[i]
            
        promedio_general = suma_notas / len(calificaciones)
        
        reporte.append({
            "nombre": nombres[i], 
            "promedio": round(promedio_general, 2)
        })
        
    reporte.sort(key=lambda x: x["promedio"], reverse=True)
    return reporte


print("\n=== Promedio por Materia ===\n")
promedios = calcular_promedios_materias(sistema_calificaciones)
for mat, prom in promedios.items():
    print(f"{mat}: {prom}")

print("\n=== Mejor Estudiante por Materia ===\n")
mejores = encontrar_mejores_estudiantes(nombres, sistema_calificaciones)
for mat, datos in mejores.items():
    print(f"{mat}: {datos['estudiante']} (Nota: {datos['nota']})")

print("\n=== Reporte General Ordenado ===\n")
reporte_final = generar_reporte_ordenado(nombres, sistema_calificaciones)
for estudiante in reporte_final:
    print(f"{estudiante['nombre']} -> Promedio General: {estudiante['promedio']}")

print("\n")