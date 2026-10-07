'''
== Ejercicio 07: Pasear Datos CSV Manualmente ==

Dadas varias líneas CSV con formato 
'nombre,nota,ciudad', extrae la información y 
muestra un reporte formateado.
'''
datos_csv = """Juan Perez, 15.5, Lima
Ana Gomez, 18.0, Arequipa
Luis Rojas, 12.5, Cusco"""

print("=" * 8 + " Reporte de CSV " + "=" * 8)
print(datos_csv)
print("\n" + "=" * 8 + " Reporte Formateado " + "=" * 8)

lineas = datos_csv.splitlines()

print(f"{'NOMBRE'.center(15)} | {'NOTA'.center(6)} | {'CIUDAD'.ljust(15)}")
print("=" * 36) 

for linea in lineas:
    partes = linea.split(",")
    
    nombre = partes[0].strip()
    nota = partes[1].strip()
    ciudad = partes[2].strip()
    
    print(f"{nombre.ljust(15)} | {nota.center(6)} | {ciudad.ljust(15)}")