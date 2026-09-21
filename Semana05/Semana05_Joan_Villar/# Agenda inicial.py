# Agenda inicial
agenda = ["Ana García", "Luis Torres", "Carlos Díaz", "María López"]

# 1. Agregar "Pedro Ruiz"
agenda.append("Pedro Ruiz")

# 2. Buscar "Carlos Díaz" y mostrar su posición
posicion = agenda.index("Carlos Díaz")
print("Posición de Carlos Díaz:", posicion)

# 3. Modificar "Luis Torres" por "Luis Mendoza"
posicion_luis = agenda.index("Luis Torres")
agenda[posicion_luis] = "Luis Mendoza"

# 4. Eliminar "Ana García"
agenda.remove("Ana García")

# Mostrar agenda final
print("Agenda final:", agenda)