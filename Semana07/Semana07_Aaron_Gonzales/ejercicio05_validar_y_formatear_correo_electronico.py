"""
Escribe una función que reciba un email, lo limpie (strip+lower), verifique que contiene '@' y '.' y retorne el dominio.
"""
def obtener_dominio(email):
    email_limpio = email.strip().lower()
    if '@' in email_limpio and '.' in email_limpio:
        dominio = email_limpio.split("@")[1]
        return dominio
    else:
        return "Email inválido. "
    
    
    
email = input("Ingrese su email: ")

print(f"El dominio es: {obtener_dominio(email)}")

