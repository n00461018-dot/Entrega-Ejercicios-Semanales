inventario = [] # global

def agregar(producto):
    global inventario
    inventario.append(producto)
def mostrar():
    for i in inventario:
        print(f" - {i}")
    
agregar("Laptop")
agregar("Teclado")
agregar("Mouse")
mostrar()
# - Laptop
# - Teclado 
# - Mouse
