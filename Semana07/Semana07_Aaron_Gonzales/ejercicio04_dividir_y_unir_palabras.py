"""
Dada la cadena 'rojo,verde,azul,amarillo', separa los colores, ponlos en mayúsculas y únelos con ' | ' como separador.
"""

cadena = 'rojo,verde,azul,amarillo'.upper()
lista = cadena.split(",")
resultado = " | ".join(lista)

print(resultado)