"""

Enunciado 9 – ANALIZAR FRECUENCIA DE PALABRAS:

Escribe una función que reciba un párrafo de texto y retorne un diccionario con la frecuencia de cada palabra,

ignorando signos de puntuación, mayúsculas y palabras vacías (stopwords).



"""

stop_words = [
    "el", "la", "los", "las", "un", "una", "unos", "unas", "este", "esta", "esto",
    "y", "e", "ni", "o", "u", "pero", "porque", "si", "no",
    "a", "con", "de", "desde", "en", "entre", "para", "por", "según", "sin", "sobre",
    "que", "me", "se", "te", "es", "son","yo","tuve"
]

parrafo = "una vez, yo tuve una casa en una (zona) alejada y con animales de casa#"
special_characters = "!@#$%^&*()-+?_=,<>/"

def analizar_frecuencia(parrafo):
    #Parrafo a minusculas
    parrafo_min = parrafo.lower()
        
    #Se borra los caracteres especiales del parrafo
    for signo in special_characters:
        parrafo_min = parrafo_min.replace(signo, "")
        
    #Separamos el parrafo en palabras
    palabras = parrafo_min.split()
        
    #Se recorre cada palabra del parrafo para ver la frecuencia
    frecuencias = {}
    for palabra in palabras:
        if palabra not in stop_words:
            if palabra in frecuencias:
                #Se aumenta en 1 el valor de la palabra repetida
                frecuencias[palabra] += 1
            else:
                #Se asigna valor 1 a la palabra no repetida
                frecuencias[palabra] = 1
                
    return frecuencias

resultado = analizar_frecuencia(parrafo)
print(resultado)