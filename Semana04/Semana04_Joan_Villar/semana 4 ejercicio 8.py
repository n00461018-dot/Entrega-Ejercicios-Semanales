# Las listas/dicts se MUTAN sin 'global'
# (porque no se reasigna la referencia)
notas = []
def agregar_nota(n):
    notas.append(n) # ← sin 'global'
agregar_nota(95)
print(notas) # [95]