def contar_palabras(parrafo):
    signos = ".,;:!?¿¡"
    stopwords = ["el", "la", "los", "las", "de", "y", "en", "un", "una"]

    for signo in signos:
        parrafo = parrafo.replace(signo, "")

    palabras = parrafo.lower().split()
    frecuencia = {}

    for palabra in palabras:
        if palabra not in stopwords:
            if palabra in frecuencia:
                frecuencia[palabra] += 1
            else:
                frecuencia[palabra] = 1

    return frecuencia


texto = "El estudiante aprende Python y el estudiante practica Python."

resultado = contar_palabras(texto)

print(resultado)