"""


Enunciado 4 – Lista de Diccionario de Estudiantes

Crea una lista de diccionarios para 4 estudiantes con los campos: "nombre", "carrera" y "promedio".

Imprime el nombre y promedio de cada estudiante.

Luego muestra el nombre del estudiante con el promedio más alto.


""" 

estudiantes = [
    {"nombre": "Alejandro", "carrera": "Ing sistemas", "promedio": 13},
    {"nombre": "Valeria", "carrera": "Ing software", "promedio": 15},
    {"nombre": "Karina", "carrera": "Ing industrial", "promedio": 18},
    {"nombre": "Mateo", "carrera": "Ing civil", "promedio": 16}
]

prom_alto = 0
nombre_prom_alto = ""

for i in range(len(estudiantes)):

    print(f"Nombre: {estudiantes[i]["nombre"]} | Promedio: {estudiantes[i]["promedio"]}")
    
    #Si el promedio actual es mayor al registrado se actualiza la nota y se guarda su nombre en la variable nombre_prom_alto
    if estudiantes[i]["promedio"] > prom_alto:
        prom_alto = estudiantes[i]["promedio"]
        nombre_prom_alto = estudiantes[i]["nombre"]

#Mostrar el nombre del estudiante con el promedio más alto
print(" ")
print(f"El estudiante con el promedio más alto es: {nombre_prom_alto} con {prom_alto}")