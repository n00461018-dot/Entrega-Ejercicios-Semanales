def celsius_a_fahrenheit(c):
    factor = 9 / 5 # local
    fahrenheit = c * factor + 32 # local - formula de conversión de grados celsius a fahrenheit
    return fahrenheit #retornamos el valor de la variable local fahrenheit
print(celsius_a_fahrenheit(25)) # 77.0
print(celsius_a_fahrenheit(0)) # 32.0   