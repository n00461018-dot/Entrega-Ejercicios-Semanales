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
    {'titulo': 'El señor de los anillos', 'autor': 'J.R.R. Tolkien', 'año': 1954},
    {'titulo': 'Cien años de soledad', 'autor': 'Gabriel García Márquez', 'año': 1967},
    {'titulo': 'El amor en los tiempos del cólera', 'autor': 'Gabriel García Márquez', 'año': 1985},
    {'titulo': 'Crónica de una muerte anunciada', 'autor': 'Gabriel García Márquez', 'año': 1981},
    {'titulo': 'Vida de Gabriel', 'autor': 'Antonio Ruiz', 'año': 2010},
    {'titulo': 'La llamada de Cthulhu', 'autor': 'H.P. Lovecraft', 'año': 1928},
]

def buscador(catalogo, query):
    resultados = []
    patron = query.lower()
    
    for libro in catalogo:
        puntaje = 0
        
        if re.search(patron, libro['titulo'].lower()):
            puntaje += 2
            
        if re.search(patron, libro['autor'].lower()):
            puntaje += 1
            
        if puntaje > 0:
            resultados.append({
                'titulo': libro['titulo'],
                'autor': libro['autor'],
                'año': libro['año'],
                'puntaje': puntaje,
            })
    
    año = sorted(resultados, key=lambda x: x['año'], reverse=True)
    resultado = sorted(resultados, key=lambda x: x['puntaje'], reverse=True)
    return resultado

busqueda = 'gabriel'
coincidencias = buscador(catalogo, busqueda)

print('-'*76)
print("RESULTADOS DE BÚSQUEDA".center(76))
print("-" * 76)
print(f"{'PTS'.center(5)} | {'AÑO'.center(6)} | {'TÍTULO'.ljust(35)} | {'AUTOR'.ljust(25)}")
print("-" * 76)

for r in coincidencias:
    pts = str(r['puntaje']).center(5)
    año = str(r['año']).center(6)
    titulo = r['titulo'].ljust(35)
    autor = r['autor'].ljust(25)
    
    print(f"{pts} | {año} | {titulo} | {autor}")   
print("-" * 76)