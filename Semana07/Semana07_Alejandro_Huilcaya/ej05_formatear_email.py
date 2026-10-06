"""
Enunciado 5 – VALIDAR Y FORMATEAR CORRE ELECTRÓNICO:
Escribe una función que reciba un email, lo limpie (strip+lower), verifique que contiene '@' y '.' y retorne el dominio.
"""
mail = input("Ingrese un email: ")

def validar_email(mail):

    email_base = mail.strip().lower()

    #Se valida que el email tenga solo 1 @
    if email_base.count("@") == 1:

        #Se divide en dos la cadena
        usuario, dominio = email_base.split("@")
        
        #Se divide en base al punto y se arma una lista
        partes_dominio = dominio.split(".")

        #Se valida que se tenga valores antes y despues del punto
        #Se valida que los valores tengan caracteres
        if len(partes_dominio) > 1 and len(partes_dominio[0]) > 0 and len(partes_dominio[-1]) > 0:
            return dominio
            
    return "El email ingresado no cumple las condiciones"

print("Dominio:", validar_email(mail))