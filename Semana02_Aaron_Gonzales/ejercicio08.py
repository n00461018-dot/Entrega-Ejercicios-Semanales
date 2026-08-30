""" 
Solicita N notas al usuario. Calcula el promedio, la nota más alta, la más baja
y cuántos estudiantes aprobaron (nota >= 11).
"""

numeroNotas = int(input("Ingrese la cantidad de notas a revisar: "))
sumaNotas = 0
notaAlta = 0
notaBaja = 20
estuAprob = 0

for i in range (numeroNotas):
    nota = float(input("Ingrese la nota: "))
    sumaNotas += nota
    if nota > notaAlta:
        notaAlta = nota
    if nota <= notaBaja: 
        notaBaja = nota
    if nota >= 11:
        estuAprob += 1
    promedio = sumaNotas / numeroNotas
    
print(f"El promedio de las notas es: {round(promedio,2)}" )
print(f"La nota más alta es: {notaAlta}")
print(f"La nota más baja es: {notaBaja}")
print(f"La cantidad de estudiantes que aprobaron es de: {estuAprob}")        
