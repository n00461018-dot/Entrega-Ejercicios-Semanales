'''
======== Ejercicio 05 - Búsqueda y Filtrado de Productos ========
Tienes una lista de diccionarios de productos con 'nombre', 'categoria' y 'precio'.
Implementa una función buscar_productos(lista, termino) que devuelva todos los productos
cuyo nombre contenga el término de búsqueda (sin importar mayúsculas).
Además, ordena los resultados por precio de menor a mayor.
'''
productos = [
    {'nombre': 'Laptop', 'categoria': 'Electrónica', 'precio': 1200.00},
    {'nombre': 'Smartphone', 'categoria': 'Electrónica', 'precio': 800.00},
    {'nombre': 'Tablet', 'categoria': 'Electrónica', 'precio': 600.00},
    {'nombre': 'Zapatos', 'categoria': 'Ropa', 'precio': 100.00},
    {'nombre': 'Camiseta', 'categoria': 'Ropa', 'precio': 25.00}
]

def buscar_productos(lista, termino):
    productos_filtrados = [producto for producto in lista if termino.lower() in producto['nombre'].lower()]
    return productos_filtrados

print("\n" + "=" * 42 + "\n")
termino_busqueda = input("Ingrese el término de búsqueda para los productos: ")
resultados = sorted(buscar_productos(productos, termino_busqueda), key=lambda x: x['precio'])

print(f"\nResultados para la búsqueda: '{termino_busqueda}'")
for producto in resultados:
    print(f"Nombre: {producto['nombre']}, Categoría: {producto['categoria']}, Precio: ${producto['precio']:.2f}")

print("\n" + "=" * 42 + "\n")
