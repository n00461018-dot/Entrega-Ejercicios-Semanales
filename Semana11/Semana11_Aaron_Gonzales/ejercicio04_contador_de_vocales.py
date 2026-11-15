"""
EJERCICIO 04: Contador de vocales

Función contar_vocales(texto) que cuente cuántas vocales (a,e,i,o,u
incluyendo tildes) contiene el texto, sin importar mayúsculas.
"""

def contar_vocales(texto):
    # Convertir el texto a minúsculas para ignorar mayúsculas
    texto = texto.lower()
    # Definir las vocales incluyendo tildes
    vocales = "aeiouáéíóú"
    # Contar las vocales en el texto
    contador = sum(1 for letra in texto if letra in vocales)
    return contador

texto = input("Ingrese un texto: ")
print(f"El texto contiene {contar_vocales(texto)} vocales.")