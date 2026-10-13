'''
=========== Ejercicio 03 - Búsqueda Simple en una Lista de Emails ============
Tienes la lista: 
emails = ['ana@gmail.com','luis@outlook.com','mia@gmail.com','juan@yahoo.com']
1) Imprime cuántos emails son de Gmail.
2) Muestra solo los emails que terminan en '.com'.
3) Verifica si 'luis@outlook.com' está en la lista (usa 'in')
'''

emails = ["ana@gmail.com", "luis@outlook.com", "mia@gmail.com", "juan@yahoo.com"]

print("=" * 103 + "\n")
email_gmail = [email for email in emails if email.endswith("@gmail.com")]
print(f"Cantidad de emails de @gmail.com: {len(email_gmail)}\n")

emails_com = [email for email in emails if email.endswith(".com")]
print(f"Emails que terminan en '.com': {emails_com}\n")

print("¿Está el email luis@outlook.com en la lista?")
if "luis@outlook.com" in emails:
    print("El email 'luis@outlook.com' está en la lista.\n")
else:
    print("El email 'luis@outlook.com' no está en la lista.\n")

print("=" * 103)
