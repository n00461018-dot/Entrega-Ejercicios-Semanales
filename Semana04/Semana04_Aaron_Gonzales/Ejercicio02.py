def promedio(numeros):
    
    total = sum(numeros) # local - se suma los números de la lista con la función built-in sum
    n = len(numeros) # local - se calcula el número de elementos que hay en la lista
    return total / n if n else 0 # se retorna el resultado de la división de la suma de los números dentro de la lista entre el número de elementos que hay en ella

print(promedio([10, 20, 30])) # 20.0