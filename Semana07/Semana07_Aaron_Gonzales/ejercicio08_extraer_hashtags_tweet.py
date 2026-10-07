"""
Dado un texto de tweet, extrae todos los hashtags (#palabras) y devuélvelos en una lista ordenada y en minúsculas.
"""

tweet = 'El otro día fui a comer pizza y estaba deliciosa #díadepizza #DELICIOSO #comida #grasa #AYUDA'.lower()

palabras = tweet.split()
fila = []

for hashtag in palabras:
    if hashtag.startswith("#"):
        fila.append(hashtag)

print(fila)
