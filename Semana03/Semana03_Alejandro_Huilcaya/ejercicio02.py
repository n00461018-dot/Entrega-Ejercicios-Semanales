def es_par(num):
    
    return num % 2 == 0


def mostrar_paridad(num):

    if es_par(num):
        print(f"El número {num} es par")
    else:
        print(f"El número {num} es impar")    

lista_test = [50, 40, 1, 15, 17,23]

for i in lista_test:
    mostrar_paridad(i)
