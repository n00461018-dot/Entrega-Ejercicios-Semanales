# Ejercicio 6 - Combinacion de arreglos y ordenamiento

# Arreglos paralelos
productos = ["Arroz", "Azucar", "Leche", "Aceite"]
ventas = [120, 85, 150, 95]

# Combinar los arreglos en una lista de diccionarios
lista_productos = []

for i in range(len(productos)):
    lista_productos.append({
        "producto": productos[i],
        "ventas": ventas[i]
    })

# Ordenar por ventas de mayor a menor
lista_productos.sort(key=lambda x: x["ventas"], reverse=True)

# Mostrar ranking de ventas
print("RANKING DE VENTAS")

posicion = 1

for producto in lista_productos:
    print(str(posicion) + "°", producto["producto"], "- Ventas:", producto["ventas"])
    posicion = posicion + 1

# Calcular el promedio de ventas
total = 0

for venta in ventas:
    total = total + venta

promedio = total / len(ventas)

print("------------------------")
print("Promedio de ventas:", promedio)

# Mostrar productos con ventas superiores al promedio
print("PRODUCTOS SOBRE EL PROMEDIO")

for producto in lista_productos:
    if producto["ventas"] > promedio:
        print(producto["producto"], "- Ventas:", producto["ventas"])