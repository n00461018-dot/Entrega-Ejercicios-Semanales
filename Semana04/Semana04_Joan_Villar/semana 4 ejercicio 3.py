def celsius_a_fahrenheit(c):
    factor = 9 / 5 # local
    fahrenheit = c * factor + 32 # local
    return fahrenheit
print(celsius_a_fahrenheit(100))
print(celsius_a_fahrenheit(0))
# respuesta 212.0
# respuesta 32.0