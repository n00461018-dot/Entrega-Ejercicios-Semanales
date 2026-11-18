"""
================ Ejercicio 04 ================

Función contar_vocales(texto) que cuente 
cuántas vocales (a,e,i,o,u incluyendo tildes) 
contiene el texto, sin importar mayúsculas. 

Tip: convierte a lower() y recorre con in
"""

def contar_vocales(texto):
    texto = texto.lower()
    vocales = "aeiouáéíóúàèìòùäëïöü"
    contador = 0
    for letra in texto:
        if letra in vocales:
            contador += 1
    return contador

while True:
    try:
        texto = input("Ingrese un texto: ")
        break
    except ValueError:
        print("Error: Por favor, ingrese un texto válido.")
        continue

print(f"El texto ingresado contiene {contar_vocales(texto)} vocales.")