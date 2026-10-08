"""
Enunciado 5 – Búsqueda y Filtrado de Productos

Tienes una lista de diccionarios de productos con 'nombre', 'categoria' y 'precio'.
Implementa una función buscar_productos(lista, termino) que devuelva todos los productos
cuyo nombre contenga el término de búsqueda (sin importar mayúsculas).
Además, ordena los resultados por precio de menor a mayor.
""" 

productos = [
    {'nombre': 'Laptop', 'categoria': 'Informática', 'precio': 2000},
    {'nombre': 'Computadora', 'categoria': 'Informática', 'precio': 3000},
    {'nombre': 'Lavadora', 'categoria': 'Electrodomésticos', 'precio': 849},
    {'nombre': 'Refrigeradora', 'categoria': 'Informática', 'precio': 1800},
]

def buscar_productos(lista, termino):
    encontrados = []
    for prod in lista:
        if termino.lower() in prod['nombre'].lower(): 
            encontrados.append(prod)
    
    encontrados_ordenados = sorted(encontrados, key=lambda p: p['precio'])
    return encontrados_ordenados

busqueda = buscar_productos(productos, 'ora')
print(busqueda)
