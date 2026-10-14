# Ejercicio 2 - Ordenamiento alfanumerico de nombres

# Lista original
nombres = ['Carlos', 'ana', 'Beatriz', 'david', 'Elena']

# Mostrar lista original
print("Lista original:")
print(nombres)

# Ordenar la lista alfabeticamente
nombres.sort(key=str.lower)
print("Lista ordenada alfabeticamente:")
print(nombres)

# Crear una nueva lista en orden descendente
nombres_descendente = sorted(nombres, key=str.lower, reverse=True)
print("Lista en orden descendente:")
print(nombres_descendente)
