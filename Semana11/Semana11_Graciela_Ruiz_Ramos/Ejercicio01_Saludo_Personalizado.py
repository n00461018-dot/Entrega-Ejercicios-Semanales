"""
================ Ejercicio 01 =========================
Crea una función saludar(nombre, saludo="Hola") que
imprima "<saludo>, <nombre>!".
Usa parámetro por defecto.

Tip: f-string y parámetro con valor por defecto
"""

def saludar(nombre,saludo="Hola"):
    return f"¡{saludo}, {nombre}! Ten un hermoso dia."


nombre = input("Introduce tu nombre: ")
print(saludar(nombre))