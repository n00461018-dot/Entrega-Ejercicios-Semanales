"""
============= EJERCICIO 02 =================
Solicita dos números enteros al usuario y
determina cuál es el mayor. Si son iguales,
indica que son iguales. Usa estructuras
condicionales.
"""
#Resolucion del ejercicio

def pedir_entero(mensaje):
    while True:
        try:
            return int(input(mensaje))
        except ValueError:
            print("Error: Ingrese un número entero válido (sin decimales).\n")

Primero = pedir_entero("Ingrese el primer número: ")
Segundo = pedir_entero("Ingrese el segundo número: ")

if Primero > Segundo:
    print("El número mayor es", Primero)
elif Segundo > Primero:
    print("El número mayor es", Segundo)
else:
    print("Son números iguales.")