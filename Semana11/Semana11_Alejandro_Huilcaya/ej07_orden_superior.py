## 07 Funciones de orden superior
#Sin for/while: usa map() para convertir Celsius→Fahrenheit, filter()
#para solo pares, sorted() con lambda para ordenar dicts por campo.
#Tip: list(map(lambda x: ..., lista)) — sin bucles explícitos

#Se crea la lista de temperaturas en Celsius
celsius = [0, 10, 14,20, 25, 30,33,40,50 ,100]
print("Lista de temperaturas en celsius:",celsius)
#Se convierte a Fahrenheit con map() y lambda
fahrenheit = list(map(lambda c: c * 9 / 5 + 32, celsius))
print("Lista convertida a Fahrenheit:", fahrenheit)

pares = list(filter(lambda n: n % 2 == 0, fahrenheit))
print("Lista de pares filtrados en Fahrenheit:", pares)

#Se ordena la lista de diccionarios por edad con sorted() y lambda
temperaturas_ciudad = [
    {"ciudad": "Lima", "fahrenheit": 77.0},
    {"ciudad": "Cusco", "fahrenheit": 50.0},
    {"ciudad": "Piura", "fahrenheit": 86.0},
    {"ciudad": "Puno", "fahrenheit": 32.0},
    {"ciudad": "Arequipa", "fahrenheit": 68.0},
    {"ciudad": "Iquitos", "fahrenheit": 91.4},
    {"ciudad": "Trujillo", "fahrenheit": 73.4},
    {"ciudad": "Huaraz", "fahrenheit": 57.2},
]
orden_ciudad = sorted(temperaturas_ciudad, key=lambda p: p["ciudad"])
print("Lista de temperaturas ordenadas por ciudad:", orden_ciudad)