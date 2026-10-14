# Ejercicio 5 - Busqueda y filtrado de productos

# Lista de productos
productos = [
    {"nombre": "Laptop Lenovo", "categoria": "Tecnologia", "precio": 2500},
    {"nombre": "Mouse Logitech", "categoria": "Tecnologia", "precio": 80},
    {"nombre": "Laptop HP", "categoria": "Tecnologia", "precio": 2200},
    {"nombre": "Teclado", "categoria": "Accesorios", "precio": 120},
    {"nombre": "Laptop Asus", "categoria": "Tecnologia", "precio": 2800}
]

# Funcion para buscar productos
def buscar_productos(lista, termino):
    resultados = []

    for producto in lista:
        if termino.lower() in producto["nombre"].lower():
            resultados.append(producto)

    resultados.sort(key=lambda producto: producto["precio"])

    return resultados

# Solicitar el producto a buscar
busqueda = input("Ingrese el producto que desea buscar: ")

# Llamar a la funcion
encontrados = buscar_productos(productos, busqueda)

# Mostrar los resultados
print("RESULTADOS DE LA BUSQUEDA")

if len(encontrados) > 0:
    for producto in encontrados:
        print(producto["nombre"], "- Precio: S/", producto["precio"])
else:
    print("No se encontraron productos")