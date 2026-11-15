"""
EJERCICIO 01: Saludo personalizado

Crea una función saludar(nombre, saludo="Hola") que imprima
"<saludo>, <nombre>!". Usa parámetro por defecto.
"""

def saludar(nombre, saludo="Hola"):
    print(f"{saludo}, {nombre}!")
    
nombre_usuario = input("Introduce tu nombre: ")
saludar(nombre_usuario)