"""
=================  Ejercicio 08 ==================
Importa matematicas_utils con alias mu y crea reporte_geometrico(radios) 
que muestre área y perímetro de cada círculo en una tabla.

Tip: import matematicas_utils as mu — usa mu.area_circulo(r)
"""

import matematicas_utils as mu  # Importación con alias segun la teoría

def reporte_geometrico(radios):
    print(f"{'Radio':<10} | {'Área':<15} | {'Perímetro':<15}")
    print("-" * 46)

    for r in radios:
        area = mu.area_circulo(r)
        perimetro = mu.perimetro_circulo(r)

        print(f"{r:<10} | {area:<15.2f} | {perimetro:<15.2f}")

if __name__ == "__main__":
    reporte_geometrico([1, 2, 3])
