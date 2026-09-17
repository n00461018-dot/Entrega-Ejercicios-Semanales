"""
Tienes la agenda: ["Ana García", "Luis Torres", "Carlos Díaz", "María López"]
Realiza: (1) Agregar "Pedro Ruiz", (2) Buscar "Carlos Díaz" y mostrar posición, (3) Modificar "Luis Torres" por "Luis Mendoza", (4) Eliminar "Ana
García".
"""

agenda = ["Ana García", "Luis Torres", "Carlos Díaz", "María López"]

# Agregamos a Pedro Ruiz al final de la lista
agenda.append("Pedro Ruiz")

#Buscamos a Carlos Díaz y mostramos su posición en la lista
for i, valor in enumerate(agenda):
    if valor == "Carlos Díaz":
        print(f"{i} = Carlos Díaz")

#Modificamos a Luis Torres por Luis Mendoza
agenda[1] = "Luis Mendoza"

#Eliminamos a Ana García de la lista
agenda.remove("Ana García")
   
print(agenda)