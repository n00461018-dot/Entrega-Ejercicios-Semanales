MODO_DEBUG = True # global (constante)
def procesar(dato):
    if MODO_DEBUG: # lectura sin 'global'
        print(f"[DEBUG] Procesando: {dato}")
    return dato.upper()
procesar("hola") # [DEBUG] Procesando: hola
