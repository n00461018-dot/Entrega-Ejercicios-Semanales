'''
============ Ejercicio 09 - Buscador Inteligente con Regex y Ordenamiento =============
Implementa una función buscador(catalogo, query) que reciba una lista de diccionarios
con campos 'titulo', 'autor' y 'año'. La función debe:
1) Buscar el query en título y autor (regex, case-insensitive).
2) Ponderar resultados: coincidencia en título vale 2 puntos, en autor 1 punto.
3) Retornar resultados ordenados por puntaje (mayor a menor) y luego por año.
'''

import re

catalogo_libros = [
    {'titulo': 'El señor de los anillos', 'autor': 'J.R.R. Tolkien', 'año': 1954},
    {'titulo': 'Python a fondo', 'autor': 'Óscar Ramírez Jiménez', 'año': 2021},
    {'titulo': 'Tolkien: Hombre y Mito', 'autor': 'Joseph Pearce', 'año': 1998},
    {'titulo': 'El hobbit', 'autor': 'J.R.R. Tolkien', 'año': 1937}
]

def buscador(catalogo, query):
    resultados = []
    
    for libro in catalogo:
        puntaje = 0
        
        if re.search(query, libro['titulo'], re.IGNORECASE):
            puntaje += 2
            
        if re.search(query, libro['autor'], re.IGNORECASE):
            puntaje += 1
            
        if puntaje > 0:
            libro_resultado = libro.copy()
            libro_resultado['puntaje'] = puntaje
            resultados.append(libro_resultado)
            
    resultados.sort(key=lambda x: (-x['puntaje'], x['año']))
    
    return resultados

input_query = input("Ingrese el término de búsqueda (título o autor): ")
query_busqueda = input_query.strip()
print(f"\nResultados de búsqueda para: '{query_busqueda}' ")
encontrados = buscador(catalogo_libros, query_busqueda)

for item in encontrados:
    print(f"Puntaje: {item['puntaje']} | {item['titulo']} - {item['autor']} ({item['año']})")
print("\n")