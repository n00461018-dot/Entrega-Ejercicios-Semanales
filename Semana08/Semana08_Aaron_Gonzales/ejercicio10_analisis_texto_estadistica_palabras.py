"""
Enunciado 10 – Análisis de Texto y Estadísticas de Palabras

Dado un párrafo de texto, implementa un analizador completo que:
1) Extraiga todas las palabras usando regex (solo letras y apóstrofes).
2) Construya un diccionario con la frecuencia de cada palabra (sin importar mayúsculas).
3) Ordene por frecuencia (desc) y luego alfabéticamente para desempates.
4) Muestre el top 5 de palabras más frecuentes y las palabras únicas ordenadas.
"""

import re

parrafo = """Muchos años después, frente al pelotón de fusilamiento, el coronel Aureliano Buendía había de recordar aquella tarde remota en que su padre lo llevó a conocer el hielo. 
Macondo era entonces una aldea de veinte casas de barro y cañabrava construidas a la orilla de un río de aguas diáfanas que se precipitaban por un lecho de piedras pulidas, 
blancas y enormes como huevos prehistóricos."""

patron = r"[a-zA-ZáéíóúÁÉÍÓÚñÑ']+"
palabras = re.findall(patron, parrafo)

frecuencias = {}
for p in palabras:
    palabra = p.lower()
    frecuencias[palabra] = frecuencias.get(palabra, 0) + 1

lista_frecuencias = list(frecuencias.items())

alfabeto = sorted(lista_frecuencias, key=lambda item: item[0]. lower())
ranking = sorted(alfabeto, key=lambda item: item[1], reverse=True)

top5 = ranking[:5]

pab_unicas = [palabra for palabra, cant in frecuencias.items() if cant == 1]
pab_uni_ord = sorted(pab_unicas, key=str.lower)

print("TOP 5 PALABRAS MÁS FRECUENTES".center(42))
print("-" * 42)
print(f"{'POS'.center(5)} | {'PALABRA'.ljust(20)} | {'FREQ'.center(8)}")
print("-" * 42)

for pos, (palabra, cant) in enumerate(top5):
    p_pos = f"{pos + 1}°".center(5)
    p_palabra = palabra.capitalize().ljust(20)
    p_cant = str(cant).center(8)
    print(f"{p_pos} | {p_palabra} | {p_cant}")

print("\n" + "=" * 42)
print(f"Total de palabras únicas (aparecen 1 vez): {len(pab_uni_ord)}")
print("=" * 42)
print(", ".join(pab_uni_ord))
print("=" * 42)