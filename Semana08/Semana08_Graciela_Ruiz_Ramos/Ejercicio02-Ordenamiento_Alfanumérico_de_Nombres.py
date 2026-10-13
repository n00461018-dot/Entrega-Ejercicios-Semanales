'''
========= Ejercicio 02 - Ordenamiento Alfanumérico de Nombres =========
Dada la lista de nombres: ['Carlos','ana','Beatriz','david','Elena']
1) Imprímela sin modificar.
2) Ordénala alfabéticamente ignorando mayúsculas con sort().
3) Crea una nueva lista ordenada en orden descendente usando sorted().
4) Muestra los resultados de cada paso.

'''

Nombres = ["Carlos", "ana", "Beatriz", "david", "Elena"]

print("=" * 78 +"\n")
print(f"Lista original: {Nombres}\n")

Nombres.sort(key=str.lower)
print(f"Lista ordenada alfabeticamente: {Nombres}\n")

Nombres_descententes = sorted(Nombres, reverse=True, key=str.lower)
print(f"Lista en orden descendente: {Nombres_descententes}\n")
print("=" * 78)