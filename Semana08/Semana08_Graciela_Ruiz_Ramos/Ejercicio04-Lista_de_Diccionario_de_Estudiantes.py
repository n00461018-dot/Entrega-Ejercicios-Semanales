'''
======= Ejercicio 04 - Lista de Diccionario de Estudiantes =======
Crea una lista de diccionarios para 4 estudiantes con los campos: 
'nombre', 'carrera' y 'promedio'.
Imprime el nombre y promedio de cada estudiante.
Luego muestra el nombre del estudiante con el promedio más alto.
'''

estudiantes = [
    {'nombre': 'Luis', 'carrera': 'Medicina', 'promedio': 20.0},
    {'nombre': 'Samantha', 'carrera': 'Psicologia', 'promedio': 18.5},
    {'nombre': 'Fernado', 'carrera': 'Ingenieria', 'promedio': 17.8},
    {'nombre': 'Dennise', 'carrera': 'Marketing', 'promedio': 16.9},
]

print("=" * 42 + "\n")
print("LISTA DE ESTUDIANTES\n".center(10))
for est in estudiantes:
    print(f"Nombre: {est['nombre']}, Promedio: {est['promedio']}")

print("\n" + "=" * 42 + "\n")
promedio_maximo = max(estudiantes, key=lambda x: x['promedio'])
print(f"Estudiante con el promedio más alto: {promedio_maximo['nombre']}")
print(f"con un promedio de {promedio_maximo['promedio']}")
print("\n" + "=" * 42)