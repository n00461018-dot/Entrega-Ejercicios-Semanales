#dominio

def validar_email(email):
    email = email.strip().lower()

    if "@" in email and "." in email:
        partes = email.split("@")
        dominio = partes[1]
        return dominio
    else:
        return "Correo no válido"


correo = input("Ingrese su correo: ")

resultado = validar_email(correo)

print("Dominio:", resultado)