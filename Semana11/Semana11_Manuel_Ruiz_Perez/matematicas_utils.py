import math

def area_circulo(radio):
    """Calcula y retorna el área de un círculo dado su radio."""
    return math.pi * (radio ** 2)

def perimetro_circulo(radio):
    """Calcula y retorna el perímetro (circunferencia) de un círculo dado su radio."""
    return 2 * math.pi * radio