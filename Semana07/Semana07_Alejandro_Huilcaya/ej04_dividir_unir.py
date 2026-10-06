"""
Enunciado 4 – DIVIDIR Y UNIR PALABRAS:
Dada la cadena 'rojo,verde,azul,amarillo', separa los colores, ponlos en mayúsculas y únelos con ' | ' como separador.

"""

cadena="rojo,verde,azul,amarillo"

def div_unir(cadena):

    mayus=cadena.upper()
    resultado=" | ".join(mayus.split(","))
    print(resultado)
    
div_unir(cadena)
