## 02 Calculadora básica
#Función calcular(a, b, operador) que soporte +, -, *, /. Retorna el
#resultado o None con mensaje de error si el operador no es válido o
#hay división por cero.
#Tip: usa if/elif y valida b ≠ 0 en división

#Se crea la funcion calcular para las operaciones de la calculadora
def calcular(a, b, operador):
    if operador == "+":
        return a + b
    elif operador == "-":
        return a - b
    elif operador == "*":
        return a * b
    elif operador == "/":
        #En caso el divisor sea 0 mostrará un mensaje de error
        if b == 0:
            print("No es posible dividir un valor entre 0")
            return None
        return a / b
    else:
        print("Operador ingresado no es válido")
        return None


#Se prueba la función con los operadores disponibles en la calculadora
print(calcular(23, 3, "+"))
print(calcular(12, 5, "-"))
print(calcular(94, 2, "*"))
print(calcular(30, 6, "/"))
print(calcular(11, 0, "/"))
print(calcular(16, 3, "%"))