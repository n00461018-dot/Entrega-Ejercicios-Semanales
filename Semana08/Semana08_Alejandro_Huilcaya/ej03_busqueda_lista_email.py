"""

Enunciado 3 – Búsqueda Simple en una Lista de Emails
Tienes la lista: emails = ['ana@gmail.com','luis@outlook.com','mia@gmail.com','juan@yahoo.com']
1) Imprime cuántos emails son de Gmail.
2) Muestra solo los emails que terminan en '.com'.
3) Verifica si 'luis@outlook.com' está en la lista (usa 'in').

"""

emails = ['ana@gmail.com','luis@outlook.com','mia@gmail.com','juan@yahoo.com']
gmailcont=0
for mail in emails:
    if mail.endswith("gmail.com"):
        gmailcont+=1
        
print("Cantidad de emails que son de gmail:",gmailcont)

print("Emails que terminan en .com:")
for mail in emails:
    if mail.endswith(".com"):
        print(mail)


if "luis@outlook.com" in emails:
    
    print("El correo 'luis@outlook.com' está en la lista")