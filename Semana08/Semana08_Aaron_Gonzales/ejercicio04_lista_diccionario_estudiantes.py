"""
Enunciado 4 – Lista de Diccionario de Estudiantes

Crea una lista de diccionarios para 4 estudiantes con los campos: 'nombre', 'carrera' y 'promedio'.
Imprime el nombre y promedio de cada estudiante.
Luego muestra el nombre del estudiante con el promedio más alto.
""" 

estudiantes = [
    {'nombre': 'Aaron', 'carrera': 'Ing. de Sistemas', 'promedio': 19},
    {'nombre': 'Adriana', 'carrera': 'Ing. Industrial', 'promedio': 18},
    {'nombre': 'Angel', 'carrera': 'Economía', 'promedio': 20},
    {'nombre': 'Kelly', 'carrera': 'Hoteleria y Turismo', 'promedio': 16},
]

for est in estudiantes:
    print(est['nombre'], '->', est['promedio'])

prom_alto = max(estudiantes, key=lambda est: est['promedio'])
print(f'El estudiante con el promedio más alto es: {prom_alto['nombre']} ({prom_alto['promedio']})')



    
