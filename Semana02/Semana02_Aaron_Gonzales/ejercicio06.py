"""
Solicita un número N y muestra todos los números primos desde 2 hasta N. 
Para cada número, verifica si es divisible entre 2 y hasta su raíz cuadrada. 
"""

num = int(input("Ingrese un número: "))

for i in range (2, num + 1):
    esPrimo = True
    sqrt = int(i ** 0.5)
    for x in range (2, sqrt + 1):
        if i % x == 0:
            esPrimo = False
            break
    if esPrimo:
        print(f"{i} es primo.")
    else:
        print(f"{i} no es primo.")
    
        