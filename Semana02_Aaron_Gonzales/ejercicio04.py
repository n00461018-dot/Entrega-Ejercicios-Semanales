"""
Usa una estructura para recorrer los números del 1
al 20. Por cada número par encontrado, incremente un contador
y acumule la suma. Al finalizar muestra cuántos números pares hay
y su suma tota
"""

contador = 0
suma = 0

for i in range (1,21):
    if i % 2 == 0:
        contador += 1
        suma += i
        
print(f"Hay {contador} números pares.")
print(f"La suma de los números pares del 1 al 20 es igual a: {suma}")