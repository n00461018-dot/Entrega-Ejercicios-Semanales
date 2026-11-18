# Clase Producto
from dataclasses import dataclass


@dataclass
class Producto:
    nombre: str
    precio: float
    stock: int

    def aplicar_descuento(self, porcentaje):
        self.precio -= self.precio * porcentaje / 100

    def vender(self, cantidad):
        if cantidad <= self.stock:
            self.stock -= cantidad
            return True

        return False


producto = Producto("Laptop", 2500, 5)

producto.aplicar_descuento(10)

print(f"Producto: {producto.nombre}")
print(f"Precio: S/ {producto.precio:.2f}")

if producto.vender(2):
    print("Venta realizada correctamente")
else:
    print("No hay suficiente stock")

print(f"Stock disponible: {producto.stock}")