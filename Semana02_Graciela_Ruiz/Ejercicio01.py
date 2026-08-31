"""
============= EJERCICIO 01 =================
Escribe un programa que solicite la base y 
altura de un rectángulo y calcule su área 
(A = base × altura) y su 
perímetro (P = 2 × (base+altura)).
Muestra los resultados formateados
"""
#Resolucion del ejercicio

base = float(input("Ingresa la base del rectangulo: "))
altura = float(input("Ingresa la altura del rectangulo: "))

area = base * altura
perimetro = 2 * ( base + altura )

print("===== RESULTADOS =====\n")
print(f"Base:       {base:>8.2f}")
print(f"Altura:     {altura:>8.2f}")
print(f"Área:       {area:>8.2f}")
print(f"Perímetro:  {perimetro:>8.2f}")