"""
================== EJERCICIO 02 ==================
Crea una función es_par(numero) que retorne True 
si el número es par o False si es impar.
Luego crea otra función mostrar_paridad(numero)
(sin return) que use la primera función e imprima 
el resultado en pantalla con un mensaje .
"""
#RESOLUCIÓN

numero = int(input("Ingrese un número: "))

def es_par(numero):
    if numero % 2 == 0:
        return True
    else:
        return False


def mostrar_paridad(numero):
    if es_par(numero):
        print(f"El número {numero} es par.")
    else:
        print(f"El número {numero} es impar.")

mostrar_paridad(numero)




