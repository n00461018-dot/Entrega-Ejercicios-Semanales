pila = []

def visitar(url):
    #Push al final de la pila
    pila.append(url)
    print("Se ingresa a :", url)
    print("Pila actual:", pila)

def retroceder():
    #Se necesitan al menos 2 paginas para la funcion
    if len(pila) >=2:
        #Se hace pop a la pila
        pila.pop()
        print("Regresaste a:", pila[-1])
    else:
        print("Se necesitan al menos 2 paginas")

def pagina_actual():

    print("Página actual:", pila[-1])


visitar("https://www.google.com/")
visitar("https://www.youtube.com/")
visitar("https://github.com/")
pagina_actual()
retroceder()
retroceder()
print("Pila final",pila)