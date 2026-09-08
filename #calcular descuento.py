#calcular descuento

def calcular_descuento(precio, porcentaje):
    descuento = precio * porcentaje / 100
    precio_final = precio - descuento
    return precio_final

precio = 100
porcentaje = 20

resultado = calcular_descuento(precio, porcentaje)

ahorro = precio - resultado

print("Precio original:", precio)
print("Precio final:", resultado)
print("Ahorro:", ahorro)
