"""

Enunciado 2 – Ordenamiento Alfanumérico de Nombres
Dada la lista de nombres: ['Carlos','ana','Beatriz','david','Elena']
1) Imprímela sin modificar.
2) Ordénala alfabéticamente ignorando mayúsculas con sort().
3) Crea una nueva lista ordenada en orden descendente usando sorted().
4) Muestra los resultados de cada paso.

"""

nombres=['Carlos','ana','Beatriz','david','Elena']

print("Lista sin modificar:")
print("  ",nombres)

print("Se ordena alfabéticamente ignorando mayúsculas con sort():")
nombres.sort(key=str.lower)
print("  ",nombres)

print("Se crea una nueva lista ordenada en orden descendente usando sorted():")
nueva= sorted(nombres,key=str.lower,reverse=True)
print("  ",nueva)
