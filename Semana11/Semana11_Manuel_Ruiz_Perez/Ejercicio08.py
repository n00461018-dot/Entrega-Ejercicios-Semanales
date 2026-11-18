## 08 Importar módulo propio
# Importa matematicas_utils con alias mu y crea
# reporte_geometrico(radios) que muestre área y perímetro de cada
# círculo en una tabla.
# Tip: import matematicas_utils as mu usa mu.area_circulo(r)

# Se importa el módulo propio creado previamente utilizando el alias 'mu'
import matematicas_utils as mu

# Se define la función que genera el reporte geométrico en formato de tabla
def reporte_geometrico(radios):
    print(f"{'Radio':<10} | {'Área':<15} | {'Perímetro':<15}")
    print("-" * 46)
    
    for r in radios:
        # Se utilizan las funciones del módulo importado mediante el alias 'mu'
        area = mu.area_circulo(r)
        perimetro = mu.perimetro_circulo(r)
        
        print(f"{r:<10} | {area:<15.2f} | {perimetro:<15.2f}")

# --- Casos de prueba ---
# Lista de radios de diferentes círculos para analizar
radios_circulos = [2, 5, 10, 15, 20]

print("--- REPORTE GEOMÉTRICO DE CIRCULOS ---")
reporte_geometrico(radios_circulos)