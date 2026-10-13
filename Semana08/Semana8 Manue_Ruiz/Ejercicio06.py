"""
06 – Combinación de Arreglos y Ordenamiento

Tienes dos arreglos paralelos: productos (strings) y ventas (enteros).
Combínalos en una lista de diccionarios, luego:
1) Ordena por ventas de mayor a menor.
2) Imprime el ranking con posición (1°, 2°, etc.).
3) Calcula el promedio de ventas e indica cuáles están sobre la media.
"""

productos = ['Laptop', 'Mouse', 'Teclado', 'Monitor', 'Impresora']
ventas = [150, 320, 280, 200, 100]

lista_productos = []

for producto, venta in zip(productos, ventas):
    lista_productos.append({'nombre': producto, 'ventas': venta})

lista_productos.sort(key=lambda producto: producto['ventas'], reverse=True)

print('RANKING DE VENTAS')
print('-'*35)

total_ventas = 0

for i, producto in enumerate(lista_productos, start=1):
    print(str(i) + '°', producto['nombre'], '- Ventas:', producto['ventas'])
    total_ventas += producto['ventas']

promedio = total_ventas / len(lista_productos)

print('-'*35)
print('Promedio de ventas:', round(promedio, 2))
print('Productos sobre la media:')

for producto in lista_productos:
    if producto['ventas'] > promedio:
        print(producto['nombre'], '- Ventas:', producto['ventas'])
