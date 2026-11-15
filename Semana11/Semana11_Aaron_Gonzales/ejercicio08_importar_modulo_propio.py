"""
EJERCICIO 08: Importar módulo propio

Importa matematicas_utils con alias mu y crea
reporte_geometrico(radios) que muestre área y perímetro de cada
círculo en una tabla.

Tip: import matematicas_utils as mu — usa mu.area_circulo(r)
"""

import matematicas_utils as mu


def reporte_geometrico(radios):
    print(f"{'Radio':>10} | {'Área':>10} | {'Perímetro':>12}")
    print("-" * 38)
    for radio in radios:
        area = mu.area_circulo(radio)
        perimetro = mu.perimetro_circulo(radio)
        print(f"{radio:10.2f} | {area:10.2f} | {perimetro:12.2f}")


if __name__ == "__main__":
    reporte_geometrico([1, 2, 3])

