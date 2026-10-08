'''
==== EJERCICIO O1 - REGISTRO DE PRODUCTOS CON ARREGLOS PARALELOS ====
Crea tres arreglos paralelos para almacenar información 
de 4 productos: nombres, precios y cantidades en stock.
Imprime un reporte que muestre cada producto con su 
precio y cantidad en una sola línea por producto.
Además, calcula e imprime el precio total del 
inventario (precio × cantidad para todos).
'''

nombres = ['Celular', 'Laptop', 'Tablet', 'Televisor']
precios = [1200.0, 1865.0, 1159.0, 7750.0]
cantidades = [10, 15, 7, 18]

print("\n=== REPORTE DE INVENTARIO ===\n")
for nombre, precio, cantidad in zip(nombres, precios, cantidades):
    print(f"Producto: {nombre}, Precio: ${precio}, Stock: {cantidad}")

print("\n=== PRECIO DEL INVENTARIO ===\n")
precio_total = 0
for nombre, precio, cantidad in zip(nombres, precios, cantidades):
    precio_productos = float(precio * cantidad)
    print(f"{nombre}: ${precio} x {cantidad} = ${precio_productos}")
    precio_total += precio_productos
print(f"\nSuma total del inventario: ${precio_total}\n")

