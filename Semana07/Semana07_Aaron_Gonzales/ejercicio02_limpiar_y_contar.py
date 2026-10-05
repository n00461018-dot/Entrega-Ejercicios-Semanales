"""
Dada la cadena ' Python es divertido ', elimina los espacios en los extremos y cuenta cuántos caracteres tiene la
cadena limpia.
"""

cadena = ' Python es divertido '

sin_espacios = cadena.strip()
longitud = len(sin_espacios)

print(f"La cadena limpia es '{sin_espacios}' y tiene {longitud} caracteres.")