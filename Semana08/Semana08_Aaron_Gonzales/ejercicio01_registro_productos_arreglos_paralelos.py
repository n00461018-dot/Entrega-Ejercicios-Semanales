"""
Enunciado 1 – Registro de Productos con Arreglos Paralelos

Crea tres arreglos paralelos para almacenar información de 4 productos: nombres, precios y cantidades en stock.
Imprime un reporte que muestre cada producto con su precio y cantidad en una sola línea por producto.
Además, calcula e imprime el precio total del inventario (precio × cantidad para todos).
"""

productos = ['Laptop', 'Computadora', 'Procesador', 'Ram', 'Monitor', 'Teclado', 'Mouse']
precios = [1200.50, 3250.8, 755, 1256.78, 890, 120.45, 320.9]
stock = [12, 5, 24, 10, 15, 40, 30]
total_inventario = 0

print('-'*51)
print('PRODUCTO'.ljust(15) + 'PRECIO'.rjust(12) + 'STOCK'.rjust(8) + 'SUBTOTAL'.rjust(16))
print('-'*51)

for producto, precio, cant in zip(productos, precios, stock):
    subtotal = precio * cant
    total_inventario += subtotal
    
    prod = producto.ljust(15)
    prec = f'S/. {round(precio, 2)}'.rjust(12)
    stk = str(cant).rjust(8)
    sbttl = f'S/. {round(subtotal, 2)}'.rjust(16)
    
    print(prod + prec + stk + sbttl)
    
print('-'*51)
print('TOTAL GENERAL'.ljust(35) + f'S/. {round(total_inventario, 2)}'.rjust(16)) 
print('-'*51)

