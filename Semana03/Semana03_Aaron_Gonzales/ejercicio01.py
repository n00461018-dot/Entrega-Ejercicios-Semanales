"""
Escribe una función llamada calcular_descuento(precio, porcentaje) que reciba el 
precio original de un producto y el porcentaje de descuento, y retorne el precio
final después del descuento. Luego muestra el ahorro obtenido
"""

def calcular_descuento(precio, porcentaje):
    descuento = porcentaje * 0.01
    ahorro = precio * descuento
    precioFinal = precio - ahorro
    return precioFinal

precioUser = float(input("Ingrese el precio del producto: "))
while True:
    try:
        porcDesc = int(input("Ingrese el porcentaje de descuento (%): "))
        if 0 <= porcDesc <= 100:
            print(f"El precio final después del descuento es de S/. {calcular_descuento(precioUser, porcDesc)} soles.")
            print(f"Ahorraste S/. {precioUser - calcular_descuento(precioUser, porcDesc)} soles.")
            break
        else: 
            print("Ingrese un valor entre 0 y 100.")
    except ValueError:
        print("ERROR: Ingrese un valor númerico.")