"""
================== Ejercicio 02 ===========================
Función calcular(a, b, operador) que soporte +, -, *, /.
Retorna el resultado o None con mensaje de error si el
operador no es válido o hay división por cero.

Tip: usa if/elif y valida b ≠ 0 en división
"""

def calculadora(a, b, operador):
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
            print("Error: División por cero no permitida.")
            return None
    else:
        print("Error: Operador no válido.")
        return None

while True:
    try:
        a = float(input("Introduce el primer número: "))
        break # Si sale bien, rompe el bucle
    except ValueError:
        print("¡Error! Debes ingresar un número válido (no letras).")

# Validar el segundo número
while True:
    try:
        b = float(input("Introduce el segundo número: "))
        break
    except ValueError:
        print("¡Error! Debes ingresar un número válido (no letras).")

# Validar el operador (se repite hasta que elija uno de los permitidos)
while True:
    operador = input("Introduce el operador (+, -, *, /): ")
    if operador in ["+", "-", "*", "/"]:
        break
    else:
        print("¡Error! Operador no válido. Usa solo +, -, * o /.")

resultado = calculadora(a, b, operador)
if resultado is not None:
    print(f"Resultado: {resultado}")