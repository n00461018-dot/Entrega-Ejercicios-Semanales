def promedio(numeros):
    total = sum(numeros) # local
    n = len(numeros) # local
    return total / n if n else 0
print(promedio([10, 20, 30])) 

#respuesta 20.0