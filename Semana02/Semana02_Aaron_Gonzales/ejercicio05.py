"""
Solicita dos números y un operador (+,-,*,/). Usa una estructura Según para determinar la operación.
Maneja el caso de división por cero con una condicional.
"""

num1 = float(input("Ingrese el primer número: "))
num2 = float(input("Ingrese el segundo número: "))

operador = int(input("Elija una operación \n1.Suma \n2.Resta \n3.Multiplicación \n4.División \nOperación: "))
match operador:
    case 1:
        sum = num1 + num2
        print(f"La suma de {num1} más {num2} es {sum}. ({num1} + {num2} = {sum})")
    case 2: 
        rest = num1 - num2
        print(f"La resta de {num1} menos {num2} es {rest}. ({num1} - {num2} = {rest})")
    case 3:
        mult = num1 * num2
        print(f"La multiplicación de {num1} por {num2} es {mult}. ({num1} x {num2} = {mult})")
    case 4:
        if num2 == 0:
            print("No se puede dividir entre 0.")
        else:
            div = num1/num2           
            print(f"La división de {num1} entre {num2} es {div}. ({num1} / {num2} = {div})")     
    case _:
        print("Seleccione un número de operación valido.") 
    