"""
================== EJERCICIO 02 ==================
Crea una función es_par(numero) que retorne True 
si el número es par o False si es impar.
Luego crea otra función mostrar_paridad(numero)
(sin return) que use la primera función e imprima 
el resultado en pantalla con un mensaje .
"""
#RESOLUCIÓN

print ("\n========= VERIFICADOR DE NUMERO PAR O IMPAR =========\n")

def es_par(numero):
    if numero % 2 == 0:
        return True
    else:
        return False

while True:
    try:
        numero = int(input("Ingrese un número: "))
    except ValueError:
        print("Error: ingrese solamente un número entero.")
        continue

    def mostrar_paridad(numero):
        if es_par(numero):
            print(f"\nEl número {numero} es par.")
            print("\n" + "=" * 54)
        else:
            print(f"\nEl número {numero} es impar.")
            print("\n" + "=" * 54)

    break
mostrar_paridad(numero)




