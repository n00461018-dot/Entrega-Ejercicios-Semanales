"""
============================== EJERCICIO 04 ==============================
Usa una estructura Para para recorrer los números del 1 al 20.
Por cada número par encontrado, incremente un contador y acumule la suma.
Al finalizar muestra cuántos números pares hay y su suma total.
"""
#Resolucion del ejercicio

contador_pares = 0
suma_pares = 0

for i in range (1,21):
    if i % 2 == 0:
        contador_pares += 1
        suma_pares += i

print("\n" + "=" * 30)
print(f"Cantidad de números pares encontrados: {contador_pares}")
print(f"Suma total de los números pares: {suma_pares}")
print("=" * 30 + "\n")