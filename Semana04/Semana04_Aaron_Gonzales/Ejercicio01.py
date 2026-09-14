def contar_vocales(texto):
    
    vocales = "aeiouAEIOU"
    conteo = 0 # local
    for letra in texto:
        if letra in vocales:
            conteo += 1
    return conteo

print(contar_vocales("Aaron Keneth Gonzales Cortez")) # 10 vocales