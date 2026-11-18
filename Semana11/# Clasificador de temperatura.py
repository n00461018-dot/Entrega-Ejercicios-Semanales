# Clasificador de temperatura
def clasificar_temperatura(temp):
    if temp <= 10:
        return "Frío"
    elif temp <= 20:
        return "Fresco"
    elif temp <= 30:
        return "Tibio"
    else:
        return "Caliente"


print(clasificar_temperatura(8))
print(clasificar_temperatura(15))
print(clasificar_temperatura(25))
print(clasificar_temperatura(35))