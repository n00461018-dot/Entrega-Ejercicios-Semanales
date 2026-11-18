"""
============ Ejercicio 06 ============

Diseña la clase Producto(nombre, precio, stock) 
con métodos aplicar_descuento(%) y vender(cant).
Lanza ValueError si no hay stock

Tip: implementa __str__ para print(producto)
"""

class Producto:
    def __init__(self, nombre, precio, stock):
        self.nombre = nombre
        self.precio = precio
        self.stock = stock

    def aplicar_descuento(self, pct):
        self.precio *= (1 - pct / 100)

    def vender(self, cantidad):
        if cantidad > self.stock:
            raise ValueError(f"Sin stock suficiente de {self.nombre}. Stock actual: {self.stock}")
        self.stock -= cantidad
        return self.precio * cantidad

    def __str__(self):
        return f"[{self.nombre}] Precio: S/.{self.precio:.2f} | Stock: {self.stock}"

# Ejemplo de uso:
p = Producto("Tablets", 1300, 12)
p.aplicar_descuento(15)  # 15% de descuento
print(p)                 # Muestra formato gracias a __str__
total = p.vender(2)      # Vende 2 unidades
print(f"Total venta: S/.{total:.2f}")
print("---- Despues de la venta ----")
print("Stock restante:", p.stock)
print(p)                 # Muestra stock actualizado