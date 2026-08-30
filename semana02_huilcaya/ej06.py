import math

print ("----------Numeros primos hasta N-----------")
n = int(input("Ingresa N: "))
print("Numeros primos encontrados:\n")
if n >= 2:
    
    #Si n es 2 o mayor que 2 incluir el numero 2 en la lista a mostrar
    print(2)
    
    # Evaluar en caso n sea 3 o mayor
    for num in range(3, n + 1):
        
        #Validamos solo los numeros impares del rango
        if num % 2 != 0:

            #Calculamos la raiz
            raiz = int(math.sqrt(num))

            #Se evaluara un divisor Imparpara cada raiz
            divisor = 3

            #Variable para indicar si el numero es primo
            primo = 1

            #Evaluamos solo los divisores iguales o menores que la raiz del numero
            while divisor <= raiz:

                #Validamos si da una division exacta (No es primo)
                if num % divisor == 0:

                    #El numero no es primo
                    primo = 0
                    #Salimos del bucle
                    break
                #Aumentamos de 2 en 2 para solamente probar con divisores impares (3,5,7,9 etc)
                divisor = divisor + 2

            #Si la variable primo se mantiene en 1, imprimimos el numero del rango
            if primo==1:
                print(num)
    #Salto de linea para el siguiente numero
    print()

else:
    #En caso ser un numero menor a 2
    print("No se encontraron numeros primos")
