"""
EJERCICIO 06: Clase Producto con descuento

Diseña la clase Producto(nombre, precio, stock) con métodos
aplicar_descuento(%) y vender(cant). Lanza ValueError si no hay
stock.
"""

class Producto:
    def __init__(self, nombre, precio, stock):
        self.nombre = nombre
        self.precio = precio
        self.stock = stock

    def aplicar_descuento(self, porcentaje):
        if porcentaje < 0 or porcentaje > 100:
            raise ValueError("El porcentaje de descuento debe estar entre 0 y 100.")
        descuento = self.precio * (porcentaje / 100)
        self.precio -= descuento

    def vender(self, cantidad):
        if cantidad > self.stock:
            raise ValueError("No hay suficiente stock para realizar la venta.")
        self.stock -= cantidad
        return self.precio * cantidad

# Producto en stock
producto = Producto("Laptop", 2500, 10)
producto.aplicar_descuento(15)  # Aplica un 15% de descuento
total_venta = producto.vender(2)  # Vende 2 unidades
print(f"Producto: {producto.nombre}")
print(f"Total de la venta: S/. {total_venta:.2f}, Stock restante: {producto.stock}")

# Producto sin stock
# producto_sin_stock = Producto("Smartphone", 1500, 0)
# producto_sin_stock.aplicar_descuento(10)  # Aplica un 10% de descuento
# total_venta_sin_stock = producto_sin_stock.vender(1)  # Intenta vender 1 unidad
