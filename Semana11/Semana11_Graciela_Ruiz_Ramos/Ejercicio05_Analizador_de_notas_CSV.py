"""
================== Ejercicio 05 ====================

Lee estudiantes.csv con el módulo csv.
Calcula promedio por alumno, muestra el top alumno y 
cuántos aprobaron (prom ≥ 13).

Tip: usa csv.DictReader y max() con lambda como key
"""

import csv

with open("estudiantes.csv", "r", encoding="utf-8", newline="") as file:
    reader = csv.DictReader(file)
    alumnos = []
    for fila in reader:
        alumno = {
            "nombre": fila["nombre"],
            "notas": [float(nota.strip()) for nota in fila["notas"].split(",")]
        }
        alumnos.append(alumno)

if not alumnos:
    print("No se encontraron alumnos en el archivo.")
else:
    promedio_general = sum(
        sum(alumno["notas"]) / len(alumno["notas"])
        for alumno in alumnos
    ) / len(alumnos)
    top_alumno = max(
        alumnos,
        key=lambda alumno: sum(alumno["notas"]) / len(alumno["notas"])
    )
    aprobados = sum(
        1 for alumno in alumnos
        if sum(alumno["notas"]) / len(alumno["notas"]) >= 13
    )

    promedio_top = sum(top_alumno["notas"]) / len(top_alumno["notas"])
    print("--- REPORTE DE NOTAS ---")
    print(f"Promedio general: {promedio_general:.2f}")
    print(f"Top alumno: {top_alumno['nombre']} con promedio: {promedio_top:.2f}")
    print(f"Cantidad de aprobados (≥ 13): {aprobados}")