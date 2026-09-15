inventario = [] # global
def agregar(producto):
    global inventario
    inventario.append(producto)
def mostrar():
    for p in inventario:
        print(f" - {p}")
agregar("Laptop")
agregar("Mouse")
mostrar()
# - Laptop
# - Mouse