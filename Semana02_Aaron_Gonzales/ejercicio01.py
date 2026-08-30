""" 
Escribe un programa que solicite la base y altura de un rectángulo y calcule su área
(A = base x altura) y su perímetro (P = 2 x (base + altura)). Muestra los resultados formateados.
""" 

base = float(input("Ingrese la base del rectángulo: "))
altura = float(input("Ingrese la altura del rectángulo: "))

area = base*altura
perimetro = 2*(base + altura)

print(f"El área del rectángulo es {area}")
print(f"El perímetro del rectángulo es {perimetro}")