"""
Enunciado 2 – LIMPIAR Y CONTAR:
Dada la cadena ' Python es divertido ', elimina los espacios en los extremos y cuenta cuántos caracteres tiene la
cadena limpia.

"""

cadena=" Python es divertido "
def limpiar_contar(cadena):

    print(f"La cadena con espacios tiene {len(cadena)} carácteres")
    cadenalimpia=cadena.strip()
    print(f"La cadena limpia tiene {len(cadenalimpia)} carácteres")

limpiar_contar(cadena)