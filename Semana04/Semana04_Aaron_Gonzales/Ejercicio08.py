# Las listas/dicts se MUTAN sin 'global'
# (porque no se reasigna la referencia)

notas = []

def agregar_nota(n):
    
    notas.append(n) # ← sin 'global'
    
agregar_nota(20)
agregar_nota(15)
agregar_nota(10)

print(notas) # [20, 15, 10]