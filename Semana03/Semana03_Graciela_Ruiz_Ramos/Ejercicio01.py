"""
============================== EJERCICIO 01 ==============================
Escribe una función llamada calcular_descuento(precio, porcentaje)
que reciba el precio original de un producto y el porcentaje de descuento,
y retorne el precio final después del descuento.
Luego muestra el ahorro obtenido.
"""
__author__ = "Graciela Ruiz Ramos"

def calcular_descuento(precio, porcentaje):
    descuento = precio * (porcentaje / 100)
    precio_final = (precio - descuento)
    ahorro = precio - precio_final
    return precio_final, ahorro

while True:
    try:
        precio = float(input("Ingrese el precio original del producto: "))
    except ValueError:
        print("Error: ingrese solamente un número para el precio.")
        continue

    if precio < 0:
        print("Error: Por favor, ingrese valores válidos.")
        continue

    while True:
        try:
            porcentaje = float(input("Ingrese el descuento: "))
        except ValueError:
            print("Error: ingrese solamente números para el porcentaje.")
            continue

        if porcentaje < 0 or porcentaje > 100:
            print("Error: el porcentaje debe estar entre 0 y 100.")
            continue

        break

    precio_final, ahorro = calcular_descuento(precio, porcentaje)
    
    print(f"El precio final es: {precio_final:.2f}")
    print(f"El ahorro obtenido es: {ahorro:.2f}")

    break