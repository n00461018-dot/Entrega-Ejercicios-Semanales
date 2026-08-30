print("----------Calculadora Basica----------")
num1=int(input("Ingrese el numero 1: "))
num2=int(input("Ingrese el numero 2: "))
op= input("Ingrese un operador (+ , -, * , /): ")
nombre= ""
rpta=0

match op:
    
    case "+":
        rpta=num1+num2
        nombre= "suma"
        
    case "-":
        rpta=num1-num2
        nombre= "resta"
    case "*":
        rpta=num1*num2
        nombre= "multiplicacion"
    case "/":
        if num2==0:
            print("No se puede dividir por 0")
            nombre="operacion"
            rpta="Invalida"
        else:
            rpta=num1/num2
            nombre= "division"
            
print(f"Resultado de la {nombre} es:",rpta)