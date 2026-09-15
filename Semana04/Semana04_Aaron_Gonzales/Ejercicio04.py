def funcion_a():
    valor = 50 # local a funcion_a
    return valor
def funcion_b():
    valor = 100 # local a funcion_b (independiente)
    return valor
print(funcion_a(), funcion_b()) # 50 100