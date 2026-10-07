'''
===== Ejercicio 09: Analizar Frecuencia de Palabras =====
Escribe una función que reciba un párrafo de texto y
retorne un diccionario con la frecuencia de cada palabra,
ignorando signos de puntuación, mayúsculas y palabras 
vacías (stopwords).
'''

def analizar_frecuencia(parrafo):
    parrafo_limpio = parrafo.lower()
    
    signos_puntuacion = ".,!?;:()[]\"'"
    for signo in signos_puntuacion:
        parrafo_limpio = parrafo_limpio.replace(signo, "")
        
    palabras = parrafo_limpio.split()
    
    stopwords = ["el", "la", "los", "las", "un", "una", "y", "o", "de", "en", "a", "que", "es", "con", "por", "para", "su"]
    
    frecuencias = {}
    
    for palabra in palabras:
        if palabra not in stopwords:
            if palabra in frecuencias:
                frecuencias[palabra] += 1
            else:
                frecuencias[palabra] = 1
                
    return frecuencias

texto_prueba = "Python es genial. Aprender en Python es divertido y muy útil."

resultado = analizar_frecuencia(texto_prueba)

print("=" * 23)
print("Frecuencia de palabras:")
print("=" * 23)

for palabra, cantidad in resultado.items():
    print(f"{palabra.ljust(15)} : {cantidad}")