"""
Enunciado9 – BuscadorInteligente con Regex y Ordenamiento

Implementa una función buscador(catalogo, query) que reciba una lista de diccionarios
con campos 'titulo', 'autor' y 'año'. La función debe:
1) Buscar el query en título y autor (regex, case-insensitive).
2) Ponderar resultados: coincidencia en título vale 2 puntos, en autor 1 punto.
3) Retornar resultados ordenados por puntaje (mayor a menor) y luego por año.
"""

import re

catalogo = [
    {'titulo': 'Python desde cero', 'autor': 'Ana Garcia', 'año': 2022},
    {'titulo': 'Programacion avanzada', 'autor': 'Luis Perez', 'año': 2020},
    {'titulo': 'Python para todos', 'autor': 'Carlos Ruiz', 'año': 2024},
    {'titulo': 'Bases de datos', 'autor': 'Ana Python', 'año': 2021},
    {'titulo': 'Introduccion a Python', 'autor': 'Luis Perez', 'año': 2019}
]

def buscador(catalogo, query):
    resultados = []
    patron = re.compile(re.escape(query), re.IGNORECASE)

    for libro in catalogo:
        puntaje = 0

        if patron.search(libro['titulo']):
            puntaje += 2

        if patron.search(libro['autor']):
            puntaje += 1

        if puntaje > 0:
            libro_resultado = libro.copy()
            libro_resultado['puntaje'] = puntaje
            resultados.append(libro_resultado)

    resultados.sort(key=lambda libro: (-libro['puntaje'], libro['año']))

    return resultados


resultados = buscador(catalogo, 'Python')

print('RESULTADOS DE LA BUSQUEDA')
print('-'*45)

for libro in resultados:
    print('Titulo:', libro['titulo'])
    print('Autor:', libro['autor'])
    print('Año:', libro['año'])
    print('Puntaje:', libro['puntaje'])
    print('-'*45)
