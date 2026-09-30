'''
Quitar el segundo elemento repetido de una lista
Dada una lista con elementos repetidos, se pide:
1) Identificar el segundo elemento repetido en la lista.
2) Eliminar ese segundo elemento repetido de la lista.
'''

frutas = ['uva', 'pera', 'uva', 'naranja']

print("======= ANTES =======")
print(f"Lista original: {frutas}")

primer_indice = frutas.index('uva')

segundo_indice = frutas.index('uva', primer_indice + 1)

elemento_eliminado = frutas.pop(segundo_indice)

print("\n======= DESPUÉS =======")
print(f"Se eliminó el elemento: '{elemento_eliminado}' en el índice {segundo_indice}")
print(f"Lista final: {frutas}")