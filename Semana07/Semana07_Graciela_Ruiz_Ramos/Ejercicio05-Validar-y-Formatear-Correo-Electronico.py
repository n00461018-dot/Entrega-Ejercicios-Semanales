'''
===== Ejercicio 05 - Validar y Formatear Correo Electrónico =====
Escribe una función que reciba un email, lo limpie (strip+lower),
verifique que contiene '@' y '.' y retorne el dominio.
'''

correo = input("Ingrese su correo electronico: ")

while True:
    if '@' in correo and '.' in correo:
        correo = correo.strip().lower()
        dominio = correo.split('@')[1]
        print(f"El dominio del correo es: {dominio}")
        break
    else:
        print("Correo inválido. Asegúrese de que contiene '@' o '.'")
        correo = input("Ingrese su correo electronico: ")