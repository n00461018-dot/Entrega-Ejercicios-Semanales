"""
Enunciado 3 – Búsqueda Simple en una Lista de Emails

Tienes la lista: emails = ['ana@gmail.com','luis@outlook.com','mia@gmail.com','juan@yahoo.com']
1) Imprime cuántos emails son de Gmail.
2) Muestra solo los emails que terminan en '.com'.
3) Verifica si 'luis@outlook.com' está en la lista (usa 'in').
"""

emails = ['ana@gmail.com','luis@outlook.com','mia@gmail.com','juan@yahoo.com']

son_gmail = 0

for gmail in emails:
    if '@gmail.com' in gmail:
        son_gmail += 1

print(f'Hay {son_gmail} emails con dominio gmail.com')

lista_com = []

for com in emails:
    if '.com' in com:
        lista_com.append(com)
        
print(f'Los emails que terminan en ".com" son los siguientes: {lista_com}')

email = 'luis@outlook.com'
if email in emails:
    print(f'El correo "{email}" está en la lista "emails"')
else:
    print(f'El correo "{email}" no está en la lista "emails"')
    