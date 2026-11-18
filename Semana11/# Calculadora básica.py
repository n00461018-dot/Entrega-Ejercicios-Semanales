# Calculadora básica
def calcular(a, b, operador):
    if operador == "+":
        return a + b
    elif operador == "-":
        return a - b
    elif operador == "*":
        return a * b
    elif operador == "/":
        if b == 0:
            return "Error: no se puede dividir entre cero"
        return a / b
    else:
        return "Operador no válido"


print(calcular(10, 5, "+"))
print(calcular(10, 5, "-"))
print(calcular(10, 5, "*"))
print(calcular(10, 5, "/"))