def contar_vocales(texto):
    vocales = "aeiouAEIOU"
    conteo = 0 # local
    for letra in texto:
        if letra in vocales:
            conteo += 1
            if conteo == 1:
                print(f"Primera vocal encontrada: {letra}")
    return conteo
print(contar_vocales("Hola Mundo")) # 4