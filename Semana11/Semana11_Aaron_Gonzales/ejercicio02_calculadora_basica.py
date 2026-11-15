"""
EJERCICIO 02: Calculadora básica

Función calcular(a, b, operador) que soporte +, -, *, /. Retorna el
resultado o None con mensaje de error si el operador no es válido o
hay división por cero.
"""

def calcular(a, b, operador):
    while True:
        if operador == "+":
            return a + b
        elif operador == "-":
            return a - b
        elif operador == "*":
            return a * b
        elif operador == "/":
            if b != 0:
                return a / b
            else:
                print("Error: División por cero.")
                return None
        else:
            print("Error: Operador no válido.")
            return None

while True:
    try: 
        primer_numero = float(input("Introduce el primer número: "))
        break
    except ValueError:
        print("Error: Entrada no válida. Por favor, introduce un número válido.")

while True:
    try:
        segundo_numero = float(input("Introduce el segundo número: "))
        break
    except ValueError:
        print("Error: Entrada no válida. Por favor, introduce un número válido.")
        
operador = input("Introduce el operador (+, -, *, /): ")
   
resultado = calcular(primer_numero, segundo_numero, operador)
if resultado is not None:
    print(f"Resultado: {resultado}")
        
    