## 06 Clase Producto con descuento
# Diseña la clase Producto (nombre, precio, stock) con métodos
# aplicar_descuento(%) y vender(cant). Lanza ValueError si no hay stock.
# Tip: implementa __str__ para print(producto)

# Se define la clase Producto para gestionar la información de inventario, precios y ventas
class Producto:
    def __init__(self, nombre, precio, stock):
        self.nombre = nombre
        self.precio = precio
        self.stock = stock

    # Método para aplicar un porcentaje de descuento al precio del producto
    def aplicar_descuento(self, porcentaje):
        if porcentaje < 0 or porcentaje > 100:
            raise ValueError("El porcentaje de descuento debe estar entre 0 y 100.")
        descuento = self.precio * (porcentaje / 100)
        self.precio -= descuento

    # Método para realizar una venta disminuyendo el stock, lanzando error si no hay suficiente
    def vender(self, cantidad):
        if cantidad > self.stock:
            raise ValueError(f"Stock insuficiente. Stock actual de '{self.nombre}': {self.stock} unidades.")
        if cantidad <= 0:
            raise ValueError("La cantidad a vender debe ser mayor a cero.")
        
        self.stock -= cantidad
        print(f"Venta exitosa: {cantidad} unidad(es) de '{self.nombre}'. Stock restante: {self.stock}")

    # Método especial __str__ para personalizar la representación en texto del objeto al usar print()
    def __str__(self):
        return f"Producto: {self.nombre} | Precio: ${self.precio:.2f} | Stock: {self.stock} unidades"

# --- Ejemplos de prueba y casos de uso ---
print("--- Creando producto inicial ---")
p1 = Producto("Laptop Gamer", 1200.00, 5)
print(p1)

print("\n--- Aplicando 10% de descuento ---")
p1.aplicar_descuento(10)
print(p1)

print("\n--- Realizando una venta de 2 unidades ---")
p1.vender(2)

print("\n--- Intentando vender mas unidades de las disponibles (genera ValueError) ---")
try:
    p1.vender(10)
except ValueError as e:
    print(f"Error controlado: {e}")