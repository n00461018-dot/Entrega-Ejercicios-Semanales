# numeros y operador
numero1 = float(input("Ingrese el primer numero: "))
numero2 = float(input("Ingrese el segundo numero: "))

#operacion 
operador = input("Ingrese un operador (+, -, *, /): ")

#casos
match operador:

    case "+":
        resultado = numero1 + numero2
        print("Resultado:", resultado)

    case "-":
        resultado = numero1 - numero2
        print("Resultado:", resultado)

    case "*":
        resultado = numero1 * numero2
        print("Resultado:", resultado)

    case "/":
        if numero2 != 0:
            resultado = numero1 / numero2
            print("Resultado:", resultado)
        else:
            print("No se puede dividir entre cero")

    case _:
        print("Operador no valido")