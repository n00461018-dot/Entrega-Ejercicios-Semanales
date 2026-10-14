# Ejercicio 4 - Lista de diccionarios de estudiantes

# Crear una lista con 4 estudiantes
estudiantes = [
    {"nombre": "Carlos", "carrera": "Ingenieria de Sistemas", "promedio": 16},
    {"nombre": "Ana", "carrera": "Administracion", "promedio": 18},
    {"nombre": "Luis", "carrera": "Contabilidad", "promedio": 15},
    {"nombre": "Maria", "carrera": "Enfermeria", "promedio": 17}
]

# Mostrar el nombre y promedio de cada estudiante
print("LISTA DE ESTUDIANTES")

for estudiante in estudiantes:
    print(estudiante["nombre"], "- Promedio:", estudiante["promedio"])

# Buscar el estudiante con el promedio mas alto
mayor_promedio = 0
mejor_estudiante = ""

for estudiante in estudiantes:
    if estudiante["promedio"] > mayor_promedio:
        mayor_promedio = estudiante["promedio"]
        mejor_estudiante = estudiante["nombre"]

# Mostrar el resultado
print("Estudiante con mayor promedio:", mejor_estudiante)
print("Promedio mas alto:", mayor_promedio)