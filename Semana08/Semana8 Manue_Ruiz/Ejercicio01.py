
productos = ['Laptop', 'Procesador', 'Monitor', 'Teclado']
precios = [2500.50, 750, 890, 120.45]
stock = [4, 10, 6, 20]
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
