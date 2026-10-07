"""
Dadas varias líneas CSV con formato 'nombre,nota,ciudad', extrae la información y muestra un reporte formateado.
"""

data_csv = """
Aaron, 20, Lima
Alvaro, 18, Ayacucho
Julio, 15, Puno
"""

print('-'*32)
print(f"{'NOMBRE'.ljust(10)} | {'NOTA'.center(6)} | {'CIUDAD'.rjust(10)}")
print('-'*32)

for info in data_csv.strip().splitlines():
    nombre, nota, ciudad = info.split(",")
    print(f"{nombre.ljust(10)} | {nota.center(6)} | {ciudad.rjust(10)}")

print('-'*32)
    