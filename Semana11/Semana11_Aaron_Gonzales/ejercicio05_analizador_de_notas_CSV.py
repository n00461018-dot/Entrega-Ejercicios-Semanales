"""
EJERCICIO 05: Analizador de notas CSV

Lee estudiantes.csv con el módulo csv. Calcula promedio por
alumno, muestra el top alumno y cuántos aprobaron (prom ≥ 13).
"""

import csv

with open("estudiantes.csv", "r") as file:
    reader = csv.DictReader(file)
    alumnos = []
    for row in reader:
        alumno = {
            "nombre": row["nombre"],
            "notas": [int(nota) for nota in row["notas"].split(",")]
        }
        alumnos.append(alumno)

promedios = []
for alumno in alumnos:
    promedio = sum(alumno["notas"]) / len(alumno["notas"])
    promedios.append((alumno["nombre"], promedio))

top_alumno = max(promedios, key=lambda x: x[1])
print(f"El alumno con el mejor promedio es: {top_alumno[0]} con un promedio de {top_alumno[1]:.2f}")

aprobados = sum(1 for _, promedio in promedios if promedio >= 13)
print(f"Cantidad de alumnos que aprobaron: {aprobados}")
