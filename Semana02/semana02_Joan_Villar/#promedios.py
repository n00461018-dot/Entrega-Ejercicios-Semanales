#promedios 
N = int(input("¿Cuantas notas va a ingresar?: "))

notas = []

for i in range(N):
    nota = float(input("Ingrese la nota: "))
    notas.append(nota)

promedio = sum(notas) / N
nota_alta = max(notas)
nota_baja = min(notas)

aprobados = 0

for nota in notas:
    if nota >= 11:
        aprobados = aprobados + 1

print("****** ESTADISTICAS ******")
print("Promedio:", promedio)
print("Nota mas alta:", nota_alta)
print("Nota mas baja:", nota_baja)
print("Estudiantes aprobados:", aprobados)
print("Estudiantes desaprobados:", N - aprobados)