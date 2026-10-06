"""
Enunciado 8 – EXTRAER HASHTAGS DE UN TWEET:
Dado un texto de tweet, extrae todos los hashtags (#palabras) y devuélvelos en una lista ordenada y en minúsculas.

"""

tweet="Hola señores #bienvenidos #hola un saludo"

print ("Tweet:",tweet)

def hashtag(tweet):
    
    hash=tweet.split()
    lista=[]
    for palabra in hash:
        if palabra.startswith("#"):
            lista.append(palabra.lower())
    lista.sort()        
    
    return lista
    
lista_hashtag=hashtag(tweet)

print("Lista ordenada de hashtags encontrados en el tweet:",lista_hashtag)