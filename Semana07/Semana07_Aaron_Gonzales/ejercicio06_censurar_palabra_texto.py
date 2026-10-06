"""
Dada una lista de palabras prohibidas, reemplaza cada aparición en un texto por asteriscos del mismo largo.
"""
texto = input("Ingrese su texto: ")
palabras_prohibidas = ['mierda', 'puto', 'estúpido', 'pendejo', 'idiota', 'malparido', 'mamagüevo', 'cabro', 'marica', 'maricón']

for palabra in palabras_prohibidas:
    censura = len(palabra) * '*'
    texto = texto.replace(palabra, censura)

print(texto)