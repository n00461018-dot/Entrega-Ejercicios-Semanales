# Ejercicio 3 - Busqueda simple en una lista de emails

# Lista de correos electronicos
emails = ['ana@gmail.com', 'luis@outlook.com', 'mia@gmail.com', 'juan@yahoo.com']

# Contar correos de Gmail
contador = 0

for email in emails:
    if email.endswith("@gmail.com"):
        contador = contador + 1

print("Cantidad de correos Gmail:", contador)

# Mostrar correos que terminan en .com
print("Correos que terminan en .com:")

for email in emails:
    if email.endswith(".com"):
        print(email)

# Verificar si un correo existe en la lista
if 'luis@outlook.com' in emails:
    print("El correo luis@outlook.com si esta en la lista")
else:
    print("El correo luis@outlook.com no esta en la lista")
