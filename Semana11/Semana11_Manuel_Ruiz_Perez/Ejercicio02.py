## 02 Calculadora básica
# Función calcular(a, b, operador) que soporte +, -, *, /. Retorna el
# resultado o None con mensaje de error si el operador no es válido o
# hay división por cero.
# Tip: f-string y parámetro con valor por defecto / usa if/elif y valida b ≠ 0 en división

# Se crea la función que recibe dos números y un operador aritmético
def calcular(a, b, operador):
    # Se evalúa el tipo de operador usando una estructura condicional if/elif
    if operador == "+":
        return a + b
    elif operador == "-":
        return a - b
    elif operador == "*":
        return a * b
    elif operador == "/":
        # Se valida que el denominador no sea cero para evitar errores de división por cero
        if b != 0:
            return a / b
        else:
            print("Error: No se puede dividir entre cero.")
            return None
    else:
        print(f"Error: Operador '{operador}' no válido.")
        return None

# Se ejecutan pruebas de la función con diferentes escenarios (operaciones válidas y errores)
print("Suma:", calcular(10, 5, "+"))
print("Resta:", calcular(10, 5, "-"))
print("Multiplicación:", calcular(10, 5, "*"))
print("División:", calcular(10, 5, "/"))
print("División por cero:", calcular(10, 0, "/"))
print("Operador inválido:", calcular(10, 5, "%"))