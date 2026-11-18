## 05 Analizador de notas CSV
# Lee estudiantes.csv con el módulo csv. Calcula promedio por
# alumno, muestra el top alumno y cuántos aprobaron (prom ≥ 13).
# Tip: usa csv.DictReader y max() con lambda como key

import csv

# Se crea la función que analiza las notas del archivo
def analizar_notas(archivo):
    # Se inicializa la lista de alumnos y el contador de alumnos aprobados
    alumnos = []
    aprobados = 0

    # Se abre el archivo y se lee cada fila como diccionario usando DictReader
    with open(archivo, encoding="utf-8") as archivo_csv:
        lector_csv = csv.DictReader(archivo_csv)
        # Por cada fila se añadirá un diccionario a la lista de alumnos con el valor nombre y promedio
        for alumno in lector_csv:
            nota1 = float(alumno["nota1"])
            nota2 = float(alumno["nota2"])
            nota3 = float(alumno["nota3"])
            promedio = (nota1 + nota2 + nota3) / 3
            # Se agrega a lista de alumnos el valor nombre y promedio por cada iteración
            alumnos.append({"nombre": alumno["nombre"], "promedio": promedio})
            # Se muestra en pantalla el valor del nombre y promedio a 2 decimales
            print(f"{alumno['nombre']}: {promedio:.2f}")
            # Si el promedio del alumno es mayor o igual a 13 se aumenta en 1 el valor del contador
            if promedio >= 13:
                aprobados += 1

    # Se busca el alumno con mayor promedio usando max() con lambda
    top = max(alumnos, key=lambda a: a["promedio"])

    # Se muestra el detalle del top alumno y su promedio, asi como el total de aprobados
    print(f"Top alumno: {top['nombre']} ({top['promedio']:.2f})")
    print(f"Aprobados: {aprobados}")

# Se ejecuta la función llamando al archivo CSV creado
analizar_notas("estudiantes.csv")