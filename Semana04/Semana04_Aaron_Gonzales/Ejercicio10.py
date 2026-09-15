def crear_acumulador():
    
    total = 0
    
    def acumular(valor):
        nonlocal total
        total += valor
        return total
    return acumular

suma = crear_acumulador()

print(suma(20)) # 20
print(suma(10)) # 30