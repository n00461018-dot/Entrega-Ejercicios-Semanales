"""
Solicita un número y muestra su tabla de multiplicar
del 1 al 10 usando una estructura repetitiva Para.
"""

numSolicitado = int(input("Ingrese un número: "))

for i in range (1, 11):
    print(f"{numSolicitado} x {i} = {numSolicitado*i}")