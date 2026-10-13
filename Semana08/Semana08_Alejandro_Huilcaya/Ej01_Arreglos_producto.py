"""

Enunciado 1 – Registro de Productos con Arreglos Paralelos
Crea tres arreglos paralelos para almacenar información de 4 productos: nombres, precios y cantidades en stock.
Imprime un reporte que muestre cada producto con su precio y cantidad en una sola línea por producto.
Además, calcula e imprime el precio total del inventario (precio × cantidad para todos).

"""

listas_nombres=["Laptop","Mouse","Monitor","Teclado"]
listas_precios=[2000,150,400,150]
listas_stock=[5,10,2,5]

precio_total=0

for i in range(len(listas_nombres)):
    print(f"Producto: {listas_nombres[i]} | Precio: {listas_precios[i]} | Stock: {listas_stock[i]}")
    precio_total+=listas_precios[i]*listas_stock[i]

print(f"Precio total del inventario de productos: {precio_total}")