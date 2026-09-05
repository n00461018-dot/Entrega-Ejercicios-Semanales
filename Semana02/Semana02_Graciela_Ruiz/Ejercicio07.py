"""
==================== EJERCICIO 07 ====================
Genera un número aleatorio entre 1 y 100. El usuario
debe adivinarlo. En cada intento, indica si el número
secreto es mayor o menor. Cuenta los intentos.
"""
#Resolucion del ejercicio

import random
intentos = 0

numero_azar = random.randint(1, 100)

while True:
    numero_usuario = int(input("Ingrese un número: "))
    intentos += 1
    if numero_azar>numero_usuario :
        print("El número es mayor.")
    elif numero_azar<numero_usuario :
        print("El número es menor.")
    else:
        print("¡Encontraste el número!")
        print(f"Lo encontraste en {intentos} intentos.")
        break


 