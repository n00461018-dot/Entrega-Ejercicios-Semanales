"""
Enunciado 2 – Ordenamiento Alfanumérico de Nombres

Dada la lista de nombres: ['Carlos','ana','Beatriz','david','Elena']
1) Imprímela sin modificar.
2) Ordénala alfabéticamente ignorando mayúsculas con sort().
3) Crea una nueva lista ordenada en orden descendente usando sorted().
4) Muestra los resultados de cada paso.
"""

nombres = ['Carlos', 'ana', 'Beatriz', 'david', 'Elena']

print('Lista original:')
print(nombres)

nombres.sort(key=str.lower)
print('Lista ordenada ascendente:')
print(nombres)

nombres_desc = sorted(nombres, key=str.lower, reverse=True)
print('Lista ordenada descendente:')
print(nombres_desc)
