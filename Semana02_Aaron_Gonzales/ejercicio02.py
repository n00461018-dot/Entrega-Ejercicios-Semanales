"""
Solicita dos números enteros al usuario y determina cuál es el mayor. Si son iguales,
indica que son iguales. Usa estructuras condicionales.
"""

num1 = int(input("Ingrese el primero número entero: "))
num2 = int(input("Ingrese el segundo número entero: "))

if num1 > num2:
    print(f"El {num1} es mayor que el {num2}. ({num1} > {num2}) ")
elif num2 > num1: 
    print(f"El {num2} es mayor que el {num1}. ({num2} > {num1}) ")
else:
    print(f"Ambos números son iguales. ({num1} = {num2})")