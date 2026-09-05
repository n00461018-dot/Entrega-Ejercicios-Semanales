"""
================ EJERCICIO 03 ================
Solicita un número y muestra su tabla de
multiplicar del 1 al 10 usando una estructura
repetitiva Para.
"""
#Resolucion del ejercicio

print("\n" + "=" * 30)
tabla = int(input("Ingrese el número a multiplicar: "))
print("=" * 30 )
print(f"{'TABLA DEL ' + str(tabla):^30}")
print("=" * 30)

for i in range(1,11):
    multiplicacion = tabla * i
    linea = (f"{tabla} x {i:>2} = {multiplicacion:>2}")
    print(f"{linea:^30}")

print("=" * 30)

