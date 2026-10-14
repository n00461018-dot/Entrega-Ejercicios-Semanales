"""
Enunciado 9 – Buscador Inteligente con Regex y Ordenamiento
Implementa una función buscador(catalogo, query) que reciba una lista de diccionarios
con campos 'titulo', 'autor' y 'año'. La función debe:
1) Buscar el query en título y autor (regex, case-insensitive).
2) Ponderar resultados: coincidencia en título vale 2 puntos, en autor 1 punto.
3) Retornar resultados ordenados por puntaje (mayor a menor) y luego por año
"""

import re

catalogo_libros = [
    {"titulo": "Juego de tronos", "autor": "Juan Arias", "año": 2005},
    {"titulo": "Orgullo y prejuicio", "autor": "Ana Gomez", "año": 2011},
    {"titulo": "El juego del angel", "autor": "Angel Soto", "año": 2002},
    {"titulo": "La odisea", "autor": "Carlos Ruiz", "año": 2000},
    {"titulo": "Introduccion a Python", "autor": "Carlos Diaz", "año": 2023},
    {"titulo": "Cuentos de terror", "autor": "Gabriel Garcia", "año": 1995},
    {"titulo": "Python Avanzado", "autor": "Maria Medina", "año": 2021}, 
    {"titulo": "Manual de redes", "autor": "Angel Python", "año": 2019}
]

def buscador(catalogo, texto_query):
    libros_encontrados = []
    patron = re.compile(re.escape(texto_query), re.IGNORECASE)
    
    for libro in catalogo:
        puntuacion = 0
        
        #Buscamos en título (vale 2 puntos)
        if patron.search(libro['titulo']):
            puntuacion += 2
            
        #Buscamos en autor (vale 1 punto)
        if patron.search(libro['autor']):
            puntuacion += 1
            
        #Si hay coincidencia se guarda una copia del libro con el puntaje obtenido
        if puntuacion > 0:
            copia_libro = libro.copy()
            copia_libro['puntaje'] = puntuacion
            libros_encontrados.append(copia_libro)
            
    libros_ordenados = sorted(libros_encontrados, key=lambda libro: (-libro['puntaje'], libro['año']))
    return libros_ordenados


busqueda = "angel"
resultados_busqueda = buscador(catalogo_libros, busqueda)

print(f"Resultados para la query: {busqueda} ")
for libro in resultados_busqueda:
    print(f"Puntaje: {libro['puntaje']} | {libro['titulo']} - {libro['autor']} ({libro['año']})")