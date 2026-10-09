"""
Enunciado 8 – Sistema de Calificaciones con Estructuras Combinadas

Crea un sistema que maneje un diccionario de listas donde las claves son materias
y los valores son listas de notas de estudiantes (arreglos paralelos con lista de nombres).
Implementa funciones para: calcular el promedio por materia, encontrar al mejor estudiante
de cada materia y generar un reporte ordenado por promedio general de mayor a menor.
"""

estudiantes = ['Aaron', 'Federico', 'Pablo', 'Lucia']

materias = {
    'Introducción a la Ing. de Sistemas': [19, 14, 17, 15],
    'Fundamentos de la Programación': [17, 20, 14, 8],
    'Principios de Seguridad': [18, 17, 14, 12],    
}

def calcular_promedio(notas):
    return sum(notas) / len(notas)

def mejor_estudiante(estudiante, notas):
    mejor_nota = -1
    mejor_est = ""
    for alumno, nota in zip(estudiante, notas):
        if nota > mejor_nota:
            mejor_nota = nota
            mejor_est = alumno
    
    return mejor_est, mejor_nota

def generar_reporte(materias, estudiante):
    reporte = []
    
    for mat in materias:
        notas = materias[mat]
        
        promedio = calcular_promedio(notas)
        mejor_est, mejor_nota = mejor_estudiante(estudiante, notas)
        
        reporte.append({
            'materia': mat,
            'promedio': promedio,
            'mejor_estudiante': mejor_est,
            'mejor_nota': mejor_nota
        })
    
    return sorted(reporte, key=lambda x: x['promedio'], reverse=True)

reporte_final = generar_reporte(materias, estudiantes)

print('-'*48)

print("         === REPORTE DE MATERIAS ===         ")
print('-'*48)

print(f'{"POS".ljust(4)}    |   {"MATERIA".ljust(14)}   |   {"PROMEDIO".center(10)}    |   {"DESTACADO".ljust(18)}')
print('-'*48)

for pos, item in enumerate(reporte_final):
    destacado = f"{item['mejor_estudiante']} ({item['mejor_nota']})"
    print(f"{pos + 1}° | {item['materia'].ljust(14)} | {item['promedio']} | {destacado.ljust(18)}")
print('-'*48)
