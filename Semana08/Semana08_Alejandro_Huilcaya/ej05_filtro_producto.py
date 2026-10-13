"""
Enunciado 5 – Búsqueda y Filtrado de Productos
Tienes una lista de diccionarios de productos con 'nombre', 'categoria' y 'precio'.
Implementa una función buscar_productos(lista, termino) que devuelva todos los productos
cuyo nombre contenga el término de búsqueda (sin importar mayúsculas).
Además, ordena los resultados por precio de menor a mayor.
"""

# Datos de prueba
catalogo = [
    {"nombre": "Laptop gamer", "categoria": "Computación", "precio": 4500.00},
    {"nombre": "Mouse Inalámbrico", "categoria": "Accesorios", "precio": 79.90},
    {"nombre": "Laptop basica", "categoria": "Computación", "precio": 2000.50},
    {"nombre": "Teclado", "categoria": "Accesorios", "precio": 180.00}
]

def buscar_productos(lista, termino):
    termino_lower = termino.lower()
    filtrados = []

    #Se recorre la lista original y se llena la lista filtrados solo los elementos que coincidan con el nombre
    for elem in lista:
        if termino_lower in elem['nombre'].lower():
            filtrados.append(elem)
            
    #Se ordena la lista usando lambda
    ordenados = sorted(filtrados, key=lambda x: x['precio'])
    
    #Se imprime los valores de la nueva lista ordenados
    for producto in ordenados:
        print(f"- {producto['nombre']} ({producto['categoria']}): S/ {producto['precio']}")


buscar_productos(catalogo, "laptop")

