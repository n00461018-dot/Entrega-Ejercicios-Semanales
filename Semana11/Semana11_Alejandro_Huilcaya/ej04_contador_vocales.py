## 04 Contador de vocales
#Función contar_vocales(texto) que cuente cuántas vocales (a,e,i,o,u
#incluyendo tildes) contiene el texto, sin importar mayúsculas.
#Tip: convierte a lower() y recorre con in

#Se crea la función para contar las vocales de un texto
def contar_vocales(texto):
    #Se agrega las vocales y sus valores con tilde
    vocales = "aeiouáéíóú"
    #Se inicializa el contador en 0
    contador = 0
    #Se convierte el texto a minúsculas para contar los valores en mayúscula
    texto = texto.lower()
    #Se recorre cada letra y se cuenta si es vocal
    for letra in texto:
        if letra in vocales:
            contador += 1
    return contador

#Se prueba la función con cadenas de texto
print(contar_vocales("Funciones con contador en python"))
print(contar_vocales("Educacion"))