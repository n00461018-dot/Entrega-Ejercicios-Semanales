# Ejercicio 9 - Buscador inteligente con Regex

import re

# Catalogo de libros
catalogo = [
    {"titulo": "Python Basico", "autor": "Juan Perez", "año": 2020},
    {"titulo": "Aprendiendo Python", "autor": "Ana Lopez", "año": 2023},
    {"titulo": "Programacion Web", "autor": "Carlos Python", "año": 2022},
    {"titulo": "Python Avanzado", "autor": "Luis Torres", "año": 2024},
    {"titulo": "Base de Datos", "autor": "Maria Garcia", "año": 2021}
]

# Funcion para buscar libros
def buscador(catalogo, query):
    resultados = []

    for libro in catalogo:
        puntaje = 0

        # Buscar en el titulo
        if re.search(query, libro["titulo"], re.IGNORECASE):
            puntaje = puntaje + 2

        # Buscar en el autor
        if re.search(query, libro["autor"], re.IGNORECASE):
            puntaje = puntaje + 1

        # Guardar los libros que tienen coincidencias
        if puntaje > 0:
            resultado = libro.copy()
            resultado["puntaje"] = puntaje
            resultados.append(resultado)

    # Ordenar por puntaje y luego por año
    resultados.sort(
        key=lambda x: (x["puntaje"], x["año"]),
        reverse=True
    )

    return resultados


# Solicitar el texto de busqueda
query = input("Ingrese el libro o autor que desea buscar: ")

# Llamar a la funcion
encontrados = buscador(catalogo, query)

# Mostrar resultados
print("\nRESULTADOS DE LA BUSQUEDA")

if len(encontrados) > 0:
    for libro in encontrados:
        print("Titulo:", libro["titulo"])
        print("Autor:", libro["autor"])
        print("Año:", libro["año"])
        print("Puntaje:", libro["puntaje"])
        print("-------------------------")
else:
    print("No se encontraron resultados")