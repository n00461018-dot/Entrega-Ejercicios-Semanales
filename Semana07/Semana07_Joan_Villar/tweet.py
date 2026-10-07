tweet = "Hoy aprendí Python #Programacion #Python #IngenieriaDeSistemas"

palabras = tweet.split()
hashtags = []

for palabra in palabras:
    if palabra.startswith("#"):
        hashtags.append(palabra.lower())

hashtags.sort()

print(hashtags)