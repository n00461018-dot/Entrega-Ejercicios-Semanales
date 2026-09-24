"""
Simula el historial de un navegador web usando una Pila (Stack). El usuario visita páginas y puede retroceder.
a) Implementar visitar(url) → agrega la página a la pila y muestra la pila actual.
b) Implementar retroceder() → quita la última página y muestra a dónde regresó.
c) Implementar pagina_actual() → muestra la página actual sin quitarla.
d) Probar con: Google → YouTube → GitHub → retroceder → retroceder.

"""

def visitar(lista, url):
    lista.append(url)
    print(lista)
    
paginas_web = []

web = input("Ingrese una página web: ")
visitar(paginas_web, web)
    
while True:
    continuar = input("¿Desea agregar otra página web? (s/n): ").lower()
    if continuar == "s":
        continue
    elif continuar == "n":
        break
    else: 
        print("ERROR: Ingrese 's' para SÍ o 'n' para NO")
    
 