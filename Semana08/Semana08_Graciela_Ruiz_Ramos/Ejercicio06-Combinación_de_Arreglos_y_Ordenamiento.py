'''
======== Ejercicio 06 - Combinación de Arreglos y Ordenamiento ========
Tienes dos arreglos paralelos: productos (strings) y ventas (enteros).
Combínalos en una lista de diccionarios, luego:
1) Ordena por ventas de mayor a menor.
2) Imprime el ranking con posición (1°, 2°, etc.).
3) Calcula el promedio de ventas e indica cuáles están sobre la media.
'''

productos = ['Chocolates', 'Galletas', 'Bebidas', 'Frutas', 'Verduras']
ventas = [500, 300, 800, 600, 400]

lista_ventas = []
for prod, vent in zip(productos, ventas):
    lista_ventas.append({'producto': prod, 'ventas': vent})

lista_ventas.sort(key=lambda x: x['ventas'], reverse=True)

print("\n==== RANKING DE VENTAS ====\n")
posicion = 1
for item in lista_ventas:
    print(f"{posicion}° - {item['producto']}: {item['ventas']} unidades")
    posicion += 1

promedio_ventas = sum(ventas) / len(ventas)

print(f"\n==== PROMEDIO DE VENTAS: {promedio_ventas} ====\n")
print("Productos con ventas superiores al promedio:")
for item in lista_ventas:
    if item['ventas'] > promedio_ventas:
        print(f"- {item['producto']} ({item['ventas']} ventas)")
print("\n" + "=" * 42 + "\n")