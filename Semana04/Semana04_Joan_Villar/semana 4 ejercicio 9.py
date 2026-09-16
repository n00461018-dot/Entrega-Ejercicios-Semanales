def generador_id():
    ultimo_id =0

    def nuevo_id():
        nonlocal ultimo_id
        ultimo_id += 1
        return f"ID-{ultimo_id:04d}"
    return nuevo_id
gen = generador_id()
print(gen())
print(gen())
print(gen())
print(gen())
print(gen())
print(gen())