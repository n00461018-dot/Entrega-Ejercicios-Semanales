#texto

texto= "Este es un texto con una palabra mala."

prohibidas = ["mala"]

for palabra in prohibidas:
    texto = texto.replace(palabra, "*" * len(palabra))

print(texto)