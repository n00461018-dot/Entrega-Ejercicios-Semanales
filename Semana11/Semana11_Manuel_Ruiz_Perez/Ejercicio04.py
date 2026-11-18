## 04 Contador de vocales
# Función contar_vocales(texto) que cuente cuántas vocales (a,e,i,o,u
# incluyendo tildes) contiene el texto, sin importar mayúsculas.
# Tip: convierte a lower() y recorre con in

# Se crea la función que cuenta las vocales (incluyendo tildes y mayúsculas) en un texto
def contar_vocales(texto):
    # Se define la cadena que contiene todas las vocales válidas a buscar
    vocales = "aeiouáéíóúü"
    contador = 0
    
    # Se convierte el texto a minúsculas para unificar criterios y se recorre carácter por carácter
    for caracter in texto.lower():
        # Se verifica si el carácter actual se encuentra dentro del conjunto de vocales
        if caracter in vocales:
            contador += 1
            
    return contador

# Se ejecutan pruebas de la función con diferentes textos y frases
print(f"Vocales en 'Programación': {contar_vocales('Programación')}")
print(f"Vocales en 'Universidad Privada del Norte': {contar_vocales('Universidad Privada del Norte')}")