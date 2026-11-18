"""
==================== Ejercicio 03 =============================
Función clasificar_temperatura(temp) que retorne "Frío" (<10),
"Fresco" (<20), "Cálido" (<30) o "Caliente" (≥30).

Tip: encadena elif con los rangos del enunciado

"""

def clasificar_temperatura(temp):
    if temp < 10:
        return "Frío"
    elif temp < 20:
        return "Fresco"
    elif temp < 30:
        return "Cálido"
    else:
        return "Caliente"

while True:
    try:
        temperatura = float(input("Ingrese la temperatura: "))
        break
    except ValueError:
        print("Error: Por favor, ingrese un número válido.")
        continue

clasificacion = clasificar_temperatura(temperatura)
print(f"La temperatura de {temperatura}°C se clasifica como: {clasificacion}")
    