
# Calculadora de Descuento

def calcular_descuento(precio_original,porcentaje):

    desc=precio_original*(porcentaje/100)
    precio_final=precio_original - desc

    print("Ahorro obtenido:",desc)
    print("Precio final",precio_final)

    return precio_final


calcular_descuento(500,20)

