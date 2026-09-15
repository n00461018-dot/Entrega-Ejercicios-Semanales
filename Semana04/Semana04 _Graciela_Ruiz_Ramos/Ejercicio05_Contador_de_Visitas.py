visitas = 0 # global
def registrar_visita():
    global visitas
    visitas += 1
    print(f"Visita #{visitas} registrada")

registrar_visita() # Visita #1
registrar_visita() # Visita #2
print(f"Total: {visitas} visitas.") # Total: 2