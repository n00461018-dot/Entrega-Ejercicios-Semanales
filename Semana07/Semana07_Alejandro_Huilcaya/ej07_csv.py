"""
Enunciado 7 – PARSEAR DATOS CSV MANUALMENTE:
Dadas varias líneas CSV con formato 'nombre,nota,ciudad', extrae la información y muestra un reporte formateado.

"""
datos_csv = """nombre,nota,ciudad
Juan,8,Lima
María,12,Ica
Carlos,19,Lima"""

# Lista para las filas del csv
filas = []

# Se recorre el csv (texto) usando splitline para separar cada fila y agregarlo a la lista filas

for linea in datos_csv.strip().splitlines():
    filas.append(linea.split(","))

# El encabezado en el indice 0 de la lista
encabezados = filas.pop(0)

# Se imprimen los valores del encabezado con un separador
print(" | ".join(encabezados))
print("-" * 25)

# Buclepara imprimir cada fila usando join y un separador
for fila in filas:
    print(" | ".join(fila))