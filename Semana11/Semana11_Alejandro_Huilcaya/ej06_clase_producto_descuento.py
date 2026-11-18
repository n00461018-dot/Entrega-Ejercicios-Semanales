## 06 Clase Producto con descuento
#Diseña la clase Producto(nombre, precio, stock) con métodos
#aplicar_descuento(%) y vender(cant). Lanza ValueError si no hay
#stock.
#Tip: implementa __str__ para print(producto)

#Se crea la clase Producto
class Producto:
    #Se crea el método constructor que guarda los campos necesarios
    def __init__(self, nombre, precio, stock):
        self.nombre = nombre
        self.precio = precio
        self.stock = stock

    #Se crea el método que calcula y aplica el descuento al precio inicial
    def aplicar_descuento(self, porcentaje):
        self.precio = self.precio * (1 - porcentaje / 100)

    #Se crea el método que vende y descuenta el stock
    def vender(self, cantidad):
        #Se lanza error si no hay stock suficiente
        if cantidad > self.stock:
            raise ValueError("Sin stock")
        self.stock = self.stock - cantidad
        print(f"Se vendieron {cantidad} unidades del producto {self.nombre}.")

    #Se crea el método para mostrar el producto con print()
    def __str__(self):
        return f"[{self.nombre}] S/.{self.precio:.2f} Stock: {self.stock}" 


#Se crea un objeto de la clase Producto y se prueban los métodos creados
laptop = Producto("Laptop", 2500, 20)
print(laptop)
laptop.aplicar_descuento(15)
laptop.vender(2)

try:
    laptop.vender(50)
except ValueError as e:
    print(f"Error: {e}")

print(laptop)