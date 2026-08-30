"""
Genera un número aleatorio entre 1 y 100. El usuario 
debe adivinarlo. En cada intento, indica si el número secreto es mauor o menor.
Cuenta los intentos. 
"""

import random
numSecreto = random.randint(1, 100)
intentos = 0

while True:
    numUser = int(input("Ingrese un número: "))
    if numUser > numSecreto:
        print("El número secreto es menor que el número ingresado.")
        intentos += 1
    elif numUser < numSecreto:
        print("El número secreto es mayor que el número ingresado.")
        intentos += 1
    else:
        intentos += 1
        print("Encontraste el número secreto.")
        print(f"Te tomó {intentos} intentos en encontrar el número secreto.")
        break
        
