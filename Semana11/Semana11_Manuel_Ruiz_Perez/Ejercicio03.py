## 03 Clasificador de temperatura
# Función clasificar_temperatura(temp) que retorne "Frío" (<10),
# "Fresco" (<20), "Cálido" (<30) o "Caliente" (≥30).
# Tip: encadena elif con los rangos del enunciado

# Se crea la función que recibe una temperatura y evalúa su rango
def clasificar_temperatura(temp):
    # Se evalúan los rangos de temperatura utilizando una cadena de condicionales if/elif/else
    if temp < 10:
        return "Frío"
    elif temp < 20:
        return "Fresco"
    elif temp < 30:
        return "Cálido"
    else:
        return "Caliente"

# Se ejecutan pruebas de la función con diferentes valores de temperatura
print(f"Temperatura 5°C: {clasificar_temperatura(5)}")
print(f"Temperatura 15°C: {clasificar_temperatura(15)}")
print(f"Temperatura 25°C: {clasificar_temperatura(25)}")
print(f"Temperatura 35°C: {clasificar_temperatura(35)}")