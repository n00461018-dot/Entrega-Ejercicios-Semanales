
visitas = 0 # global
def registrar_visita(nombre):
    global visitas
    if nombre =="Alejandro":

        visitas += 1
        print(f"Visita #{visitas} de {nombre} registrada.")
    else:
        print(f"Persona {nombre} no está registrada.")
registrar_visita("Alejandro") # Visita #1
registrar_visita("Alejandro") # Visita #2
registrar_visita("Javier") # no muestra visita 
print(f"Total: {visitas}") # Total: 2