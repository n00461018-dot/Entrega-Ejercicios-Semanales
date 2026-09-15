MODO_DEBUG = True # global (constante)
def procesar(dato):
    if MODO_DEBUG: # lectura sin 'global'
        print(f"[DEBUG] Procesando: {dato}")
    return dato.upper()
print(procesar("hola")) # Asignar el retorno de la funcion
MODO_DEBUG = False     # Desactivar el DEBUG
print(procesar("adios")) 