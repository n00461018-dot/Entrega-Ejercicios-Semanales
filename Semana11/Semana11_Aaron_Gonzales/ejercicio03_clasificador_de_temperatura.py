"""
EJERCICIO 03: Clasificador de temperatura

Función clasificar_temperatura(temp) que retorne "Frío" (<10),
"Fresco" (<20), "Cálido" (<30) o "Caliente" (≥30).
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
    
temperaturas = [5, 15, 25, 35]
for temp in temperaturas:
    print(f"La temperatura {temp}°C es: {clasificar_temperatura(temp)}")