"""
Crea una función es_par(numero) que retorne True si el número es par o False si es impar.
Luego crea otra función mostrar_paridad(numero) (sin return) que use la primera función e 
imprima el resultado en pantalla con un mensaje.   
"""

def es_par(numero):

    if numero % 2 == 0:
        compBool = True
    else:
        compBool = False
        
    return compBool

def mostrar_paridad(numero):
    print(f"El número es {es_par(numero)}")
    
num = int(input("Ingrese un número: "))
es_par(num)
mostrar_paridad(num)