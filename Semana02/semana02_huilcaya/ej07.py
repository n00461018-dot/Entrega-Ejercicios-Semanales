import random

rnd=random.randint(1,100)
contador=0

print("----------Adivina el numero aleatorio----------")

while True:

    guess=int(input("Ingresa un numero: "))
    contador+=1
    if guess>rnd:
        print("                       ")
        print("El numero ingresado es mayor que el aleatorio")
        print("Intento Nro:",contador)
        print("                       ")

    if guess<rnd:
        print("El numero ingresado es menor que el aleatorio")
        print("Intento Nro:",contador)
        print("                       ")

    if guess==rnd:
        print(f"Encontraste el numero aleatorio <{rnd}>")
        print("Intento Nro:",contador)
        break


