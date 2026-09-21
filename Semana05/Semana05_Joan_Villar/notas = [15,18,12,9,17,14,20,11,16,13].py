notas = [15,18,12,9,17,14,20,11,16,13]

promedio = sum(notas) / len(notas)
nota_alta = max(notas)
nota_baja = min(notas)

aprobados = 0
print()

for nota in notas:
    if nota >= 11:
        aprobados += 1

print("promedio:", promedio)
print("nota mas alta:", nota_alta)
print("nota mas baja:", nota_baja)
print("aprovados:", aprobados)