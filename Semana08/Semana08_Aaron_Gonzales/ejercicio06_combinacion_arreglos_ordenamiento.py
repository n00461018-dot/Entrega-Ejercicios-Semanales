"""
Enunciado 6 – Combinación de Arreglos y Ordenamiento

Tienes dos arreglos paralelos: productos (strings) y ventas (enteros).
Combínalos en una lista de diccionarios, luego:
1) Ordena por ventas de mayor a menor.
2) Imprime el ranking con posición (1°, 2°, etc.).
3) Calcula el promedio de ventas e indica cuáles están sobre la media.
"""

productos = ['Laptop', 'Teclado', 'Monitor', 'Mouse', 'Auriculares']
ventas = [2000, 150, 850, 300, 400]

lista_prod = [
    {'nombre': prod, 'ventas': cant}
    for prod, cant in zip(productos, ventas)
]

ranking = sorted(lista_prod, key=lambda x: x['ventas'], reverse=True)

print('-'*40)
print('=========  RANKING DE VENTAS  =========')
print('-'*40)
for posc, item in enumerate(ranking):
    print(f'{posc+1}° |   {item['nombre'].ljust(12)}    :   {item['ventas']} unidades')
    
total_ventas = sum(ventas)
promedio = total_ventas / len(ventas)
print('-'*40)
print(f'Promedio general de ventas: {promedio:.1f} unidades')
print('-'*40)
print('Productos con ventas sobre la media:')
for item in ranking:
    if item['ventas'] > promedio:
        diff = item['ventas'] - promedio
        print(f'{item['nombre']} ({item['ventas']} unidades, +{diff:.1f} sobre la media)')
print('-'*40)