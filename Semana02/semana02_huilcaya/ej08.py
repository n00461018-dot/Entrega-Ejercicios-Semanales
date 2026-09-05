print("----------Promedio y Estadistica----------")
n=int(input("Ingrese cantidad de notas a registrar: "))
prom=0
suma=0
alta=0
baja=21
cont=0

for i in range(1,n+1):
    nota=int(input(f"Ingrese la nota {i}: "))
    suma+=nota
    if nota>alta:
        alta=nota
    
    if nota<baja:
        baja=nota

    if nota>=11:
        cont+=1
prom=round(suma/n,2)

print("                             ")
print("El promedio de notas es:",prom)
print("La nota mas alta es:",alta)
print("La nota mas baja es:",baja)
print(f"Aprobaron {cont} estudiantes")