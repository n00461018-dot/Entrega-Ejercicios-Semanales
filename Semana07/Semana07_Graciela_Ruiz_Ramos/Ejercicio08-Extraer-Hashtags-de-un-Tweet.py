'''
===== Ejercicio 08 - Extraer Hashtags de un Tweet =====
Dado un texto de tweet,
extrae todos los hashtags (#palabras) y
devuélvelos en una lista ordenada y en minúsculas.
'''

texto_tweet = "Hoy es un gran día para aprender #Python. Me encanta la #programación y el #CÓDIGO limpio!"

palabras = texto_tweet.split()

hashtags = []

for palabra in palabras:
    if palabra.startswith("#"):
        
        hashtag_limpio = palabra.strip(".,!?").lower()
        
        if hashtag_limpio not in hashtags:
            hashtags.append(hashtag_limpio)

hashtags.sort()
print(f"Texto del tweet: {texto_tweet}")
print(f"Hashtags extraídos y ordenados: {hashtags}")