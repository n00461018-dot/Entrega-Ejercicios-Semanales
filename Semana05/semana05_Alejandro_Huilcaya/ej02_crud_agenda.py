"""
Tienes la agenda: ["Ana García", "Luis Torres", "Carlos Díaz", "María López"]
Realiza: (1) Agregar "Pedro Ruiz", (2) Buscar "Carlos Díaz" y mostrar posición, (3) Modificar "Luis Torres" por "Luis Mendoza", (4) Eliminar "Ana
García".
"""

agenda=["Ana Garcia", "Luis Torres", "Carlos Diaz", "Maria Lopez"]

# Funcion crud
def crud(agenda):

    # Variables para agregar y eliminar
    usuario_agregar="Pedro Ruiz"
    usuario_eliminar="Ana Garcia"
    agenda.append(usuario_agregar)
    print(f"01. Se agrega {usuario_agregar} a agenda")

    #Bucle para tomar indice y modificar valores dentro de la agenda
    for i in range(len(agenda)):
        if agenda[i]=="Carlos Diaz":
            print(f"02. Se encontró contacto {agenda[i]} en la posición: {i+1}")

        if agenda[i]=="Luis Torres":
            print("03. Se cambia apellido para Luis Mendoza")
            agenda[i]="Luis Mendoza"

    #Eliminar elemento de agenda
    agenda.remove(usuario_eliminar)
    print(f"04. Se elimina a contacto {usuario_eliminar}")

    #Mostrar la agenda
    print(agenda)

#Ejecutamos la funcion con la lista agenda
crud(agenda)