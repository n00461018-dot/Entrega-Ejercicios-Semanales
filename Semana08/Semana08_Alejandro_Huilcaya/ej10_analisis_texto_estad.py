"""
enunciado diez analisis de texto y estadisticas de palabras
dado un parrafo de texto implementa un analizador completo que
extraiga todas las palabras usando regex solo letras y apostrofes
construya un diccionario con la frecuencia de cada palabra sin importar mayusculas
ordene por frecuencia desc y luego alfabeticamente para desempates
muestre el top cinco de palabras mas frecuentes y las palabras unicas ordenadas
"""

import re

parrafo = (
    "hoy me levanté tarde porque no sonó mi alarma, "
    "así que tuve que correr al tren porque no quería llegar tarde "
    "y mi mochila estaba abierta sin que me diera cuenta"
)

def analizar_texto(texto):
    #extraer palabras usando regex
    palabras_extraidas = re.findall(r"[a-zA-ZáéíóúÁÉÍÓÚñÑ']+", texto)
    
    #se crea un diccionario de frecuencias
    frecuencias = {}
    for palabra in palabras_extraidas:
        palabra_minuscula = palabra.lower()
        if palabra_minuscula in frecuencias:
            frecuencias[palabra_minuscula] += 1
        else:
            frecuencias[palabra_minuscula] = 1
            
    #Se ordena por frecuencia descendente y alfabeticamente
    lista_frecuencias = list(frecuencias.items())
    palabras_ordenadas = sorted(lista_frecuencias, key=lambda item: (-item[1], item[0]))
    
    #Se obtiene el top cinco y las palabras unicas ordenadas
    top_cinco = palabras_ordenadas[:5]
    palabras_unicas = sorted(list(frecuencias.keys()))
    
    #Se imprime el resultado
    print("TOP 5 PALABRAS FRECUENTES")
    for palabra, frecuencia in top_cinco:
        print(f"- {palabra}: {frecuencia} veces")
        
    print("\nPALABRAS ÚNICAS ORDENADAS ALFABÉTICAMENTE")
    for palabra in palabras_unicas:
        print(f"- {palabra}")


analizar_texto(parrafo)