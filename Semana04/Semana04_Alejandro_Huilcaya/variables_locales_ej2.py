
def promedio(numeros):
    total = sum(numeros) # local
    n = len(numeros) # local
    return total / n if n else 0
print(promedio([10, False, 30]))