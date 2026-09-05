"""
========================== EJERCICIO 05 ==========================
Solicita dos números y un operador (+,-, *, /). Usa una estructura
Según para determinar la operación. Maneja el caso de división por
cero con una condicional.
"""
#Resolucion del ejercicio

primero = float(input("Ingrese el primer número: "))
segundo = float(input("Ingrese el segundo número: "))
operador = input("Escoje un operador (+, -, *, /): ").strip()

match operador:
    case "+":
        suma = primero + segundo
        print(f"El resultado es: {suma}")
    case "-":
        resta = primero - segundo
        print(f"El resultado es: {resta}")
    case "*":
        multiplicacion = primero * segundo
        print(f"El resultado es: {multiplicacion}")
    case "/":
        if segundo == 0:
            print("Error: No se puede dividir entre cero.")
        else:
            dividir = primero / segundo
            float(print(f"El resultado es: {dividir}"),2)
    case _:
        print("Error: operador no válido.")
        print("Use +, -, * o /")







