"""

Enunciado 3 – EXTRAER SUBCADENA:
Dada la cadena 'Análisis de Datos con Python', extrae las palabras 'Datos' y 'Python' usando slicing.

"""

cadena="Análisis de Datos con Python"

def slicing(cadena):

    palabra1=cadena[12:17]
    palabra2=cadena[22:28]

    print(palabra1)
    print(palabra2)
    
slicing(cadena)