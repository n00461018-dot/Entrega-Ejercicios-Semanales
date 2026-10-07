'''
=== Ejercicio 06 - Censurar Palabra en un Texto ===
Dada una lista de palabras prohibidas, reemplaza 
cada aparición en un texto por asteriscos del 
mismo largo.
'''

lista_prohibida = ["malo", "feo", "tonto", "cojudo", "mierda", "puto", "carajo"]
texto = input("Ingrese un texto: ")

if len(texto.strip()) == 0:
    print("El texto está vacío.")
else:
    texto_censurado = texto
    
    for palabra in lista_prohibida:
        longitud = len(palabra)
        asteriscos = "*" * longitud
        texto_censurado = texto_censurado.replace(palabra, asteriscos)

    if texto == texto_censurado:
        print("No tiene palabras prohibidas a censurar")
    else:
        print(f"Texto final censurado: {texto_censurado}")