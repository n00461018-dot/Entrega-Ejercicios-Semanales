"""
Enunciado 2 – Ordenamiento Alfanumérico de Nombres

Dada la lista de nombres: ['Carlos','ana','Beatriz','david','Elena']
1) Imprímela sin modificar.
2) Ordénala alfabéticamente ignorando mayúsculas con sort().
3) Crea una nueva lista ordenada en orden descendente usando sorted().
4) Muestra los resultados de cada paso.
"""

nombres = ['Carlos','ana','Beatriz','david','Elena']

print(f'Lista de nombres sin moodificar: {nombres}')

nombres.sort()

print(f'Lista de nombres ordenados alfabéticamente ignorando mayúsculas: {nombres}')

descendente = sorted(nombres, reverse = True)

print(f'Nueva lista ordenada en orden descendente: {descendente}')