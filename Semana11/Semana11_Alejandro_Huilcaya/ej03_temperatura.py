## 03 Clasificador de temperatura
#Función clasificar_temperatura(temp) que retorne "Frío" (<10),
#"Fresco" (<20), "Cálido" (<30) o "Caliente" (≥30).
#Tip: encadena elif con los rangos del enunciado

#Se crea la función que clasifica según los rangos
def clasificar_temperatura(temp):
    if temp < 10:
        return "Frío"
    elif temp < 20:
        return "Fresco"
    elif temp < 30:
        return "Cálido"
    else:
        return "Caliente"

#Se prueba la función con diferentes rangos de temperaturas
print(clasificar_temperatura(7))
print(clasificar_temperatura(12))
print(clasificar_temperatura(28))
print(clasificar_temperatura(40))