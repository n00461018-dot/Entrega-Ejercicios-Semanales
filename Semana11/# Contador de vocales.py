# Contador de vocales
def contar_vocales(texto):
    vocales = "aeiou"
    contador = 0

    for letra in texto.lower():
        if letra in vocales:
            contador += 1

    return contador


texto = "Hola Joan"
print(f"Cantidad de vocales: {contar_vocales(texto)}")