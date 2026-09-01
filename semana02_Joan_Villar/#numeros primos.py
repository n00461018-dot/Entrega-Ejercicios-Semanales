#numeros primos
N = int(input("Ingrese un numero N: "))

for numero in range(2, N + 1):

    primo = True

    for divisor in range(2, int(numero ** 0.5) + 1):

        if numero % divisor == 0:
            primo = False
            break

    if primo:
        print(numero)