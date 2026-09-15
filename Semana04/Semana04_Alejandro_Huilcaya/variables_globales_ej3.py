inventario = [] # global
def agregar(producto):
    global inventario
    inventario.append(producto)
def mostrar():
    for p in inventario:
        print(f" - {p}")
    print("Total de inventario: ",len(inventario))
agregar("Laptop")
agregar("Mouse")
mostrar()
# - Laptop