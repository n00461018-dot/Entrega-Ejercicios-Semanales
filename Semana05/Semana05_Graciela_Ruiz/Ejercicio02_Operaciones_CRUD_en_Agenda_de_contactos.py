"""
=========================== Ejercicio 02 ================================
                Operaciones CRUD en Agenda de Contactos
Enunciado:
Tienes la agenda: ["Ana García", "Luis Torres", "Carlos Díaz", "María López"]
Realiza: 
(1) Agregar "Pedro Ruiz", 
(2) Buscar "Carlos Díaz" y mostrar posición, 
(3) Modificar "Luis Torres" por "Luis Mendoza", 
(4) Eliminar "Ana García".
===========================================================================
"""

agenda = ["Ana García", "Luis Torres", "Carlos Díaz", "María López"]
#antes de realizar las operaciones, mostramos la agenda
print("Agenda inicial:")
print(agenda)
print("=" * 47 + "\n")

print("1. Agregar 'Pedro Ruiz' al final")
agenda.append("Pedro Ruiz")
posicion_pedro = agenda.index("Pedro Ruiz")
print("Agenda después de agregar a Pedro Ruiz:") 
print(f" {agenda}")
print(f"Posición de Pedro Ruiz: {posicion_pedro}\n")
print("=" * 47 + "\n")

print("2. Buscar 'Carlos Díaz' y mostrar posición")
posicion = agenda.index("Carlos Díaz")
print(f"Posición de Carlos Díaz: {posicion}\n")
print("=" * 47 + "\n")

print("3. Modificar 'Luis Torres' por 'Luis Mendoza'")
pos_luis = agenda.index("Luis Torres")
agenda[pos_luis] = "Luis Mendoza"
print(f"Agenda después de modificar a Luis Torres por Luis Mendoza:")
print(f" {agenda}\n")
print("=" * 47 + "\n")

print("4. Eliminar 'Ana García'")
agenda.remove("Ana García")
print(f"Agenda después de eliminar a Ana García:")
print(f" {agenda}\n")
print("=" * 47 + "\n")

print("5. Mostrar la agenda final")
print(agenda)
print("\n" + "=" * 47)

#Graciela Ruiz
