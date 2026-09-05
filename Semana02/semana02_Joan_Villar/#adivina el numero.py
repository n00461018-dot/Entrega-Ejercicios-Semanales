#adivina el numero
import random

numero_secreto = random.randint(1, 100)

intentos = 0

while True:

    numero = int(input("Adivina el numero (1-100): "))

    intentos = intentos + 1

    if numero < numero_secreto:
        print("El numero secreto es mayor")

    elif numero > numero_secreto:
        print("El numero secreto es menor")

    else:
        print("Correcto")
        print("Adivinaste en", intentos, "intentos")
        break