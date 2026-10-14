# Datos de los productos
nombres = ["Arroz", "Azucar", "Leche", "Aceite"]
precios = [4.50, 3.80, 5.00, 9.50]
cantidades = [10, 8, 12, 6]

total_inventario = 0

print("REPORTE DE PRODUCTOS")
print("----------------------------")

for i in range(4):
    print(nombres[i], "- Precio: S/", precios[i], "- Stock:", cantidades[i])
    total_inventario = total_inventario + precios[i] * cantidades[i]

print("----------------------------")
print("Valor total del inventario: S/", round(total_inventario, 2))
