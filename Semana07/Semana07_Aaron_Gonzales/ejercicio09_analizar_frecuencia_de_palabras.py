"""
Escribe una función que reciba un párrafo de texto y retorne un diccionario con la frecuencia de cada palabra,
ignorando signos de puntuación, mayúsculas y palabras vacías (stopwords).
""" 
def frecuencia_palabras(texto):
    
    stopwords = {'la', 'el', 'los', 'las', 'un', 'una', 'unos', 'unas',
            'de', 'del', 'en', 'a', 'y', 'e', 'o', 'u', 'ha', 'se',
            'ya', 'que', 'nuestra'}
    
    caracteres_especiales = "!@#$%^&*_+=-;:,."
    
    texto_min = texto.lower()
    
    for signos in caracteres_especiales:
        texto_limpio = texto_min.replace(signos, "")
        
    texto_separado = texto_limpio.split()
    
    frecuencia = {}
    for palabras in texto_separado:
        if palabras not in stopwords:
            if palabras in frecuencia:
                frecuencia[palabras] += 1
            else:
                frecuencia[palabras] = 1
    
    return frecuencia
    

parrafo = 'La tecnología se ha convertido en una herramienta fundamental en nuestra vida cotidiana, ya que facilita la comunicación, el acceso a la información y el desarrollo de diversas actividades académicas y laborales.'

print(frecuencia_palabras(parrafo))
