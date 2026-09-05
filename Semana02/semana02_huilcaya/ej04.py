contador=0
suma=0

for i in range(1,21):
    
    if i%2==0:
        contador+=1
        suma+=i
   
print("----------Contar y sumar Pares del 1 al 20----------")
print("La cantidad de numeros pares es:",contador)
print("La suma total de numeros pares es:",suma)