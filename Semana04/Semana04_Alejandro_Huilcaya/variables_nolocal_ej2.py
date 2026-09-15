def crear_acumulador():
    total = 0
    def acumular(valor):
        nonlocal total
        total += valor
        return total
    return acumular

suma = crear_acumulador()
print(suma(10)) # 10
print(suma(5)) # 15