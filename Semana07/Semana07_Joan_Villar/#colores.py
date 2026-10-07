#colores
colores = 'rojo,verde,azul,amarillo'

colores = colores.split(',')

colores_mayusculas = [color.upper() for color in colores]

resultado = ' | '.join(colores_mayusculas)

print(resultado)