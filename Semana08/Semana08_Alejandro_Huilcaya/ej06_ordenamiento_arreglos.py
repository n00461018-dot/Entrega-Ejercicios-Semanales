"""
Enunciado 6 – Combinación de Arreglos y Ordenamiento
Tienes dos arreglos paralelos: productos (strings) y ventas (enteros).
Combínalos en una lista de diccionarios, luego:
1) Ordena por ventas de mayor a menor.
2) Imprime el ranking con posición (1°, 2°, etc.).
3) Calcula el promedio de ventas e indica cuáles están sobre la media.
"""

productos = ["Laptop Pro", "Mouse Inalámbrico", "Teclado Mecánico", "Monitor 24\"", "Audífonos Gamer"]
ventas = [120, 450, 310, 85, 290]

#Se juntan las listas y los ordenamos del más al menos vendido
combinados = [{"producto": p, "ventas": v} for p, v in zip(productos, ventas)]

#Se ordena la lista de valores combinados usando lambda
ordenados = sorted(combinados, key=lambda x: x['ventas'], reverse=True)

print("RANKING DE VENTAS")
for i, dicc in enumerate(ordenados, start=1):
    print(f"{i} - {dicc['producto']}: {dicc['ventas']} unidades")

#Se calcula la media de ventas
#Promedio de ventas
promedio = sum(ventas) / len(ventas)
print("Promedio de ventas:", promedio)

print("PRODUCTOS SOBRE LA MEDIA")
for dicc in ordenados:
    if dicc['ventas'] > promedio:
        print(f"- {dicc['producto']} ({dicc['ventas']} ventas)")