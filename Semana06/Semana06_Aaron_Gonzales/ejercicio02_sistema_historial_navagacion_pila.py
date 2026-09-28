"""
Simula el historial de un navegador web usando una Pila (Stack). El usuario visita páginas y puede retroceder.
a) Implementar visitar(url) → agrega la página a la pila y muestra la pila actual.
b) Implementar retroceder() → quita la última página y muestra a dónde regresó.
c) Implementar pagina_actual() → muestra la página actual sin quitarla.
d) Probar con: Google → YouTube → GitHub → retroceder → retroceder.

"""

def visitar(lista, url):
    lista.append(url)
    print(f"Pila actual: {lista}\n")
    
def retroceder(lista):
    if len(lista) <= 1:
        print("No hay páginas anteriores para retroceder.\n")
    else:
        eliminar = lista.pop(-1)
        print(f"Saliste de {eliminar}, regresando a {lista[-1]}\n")
        
def pagina_actual(lista):
    if len(lista) == 0:
        print("El navegador está en una pestaña en blanco.\n")
    else:
        print(f"Actualmente estás en {lista[-1]}\n")
    
paginas_web = []
while True:
    print("--- NAVEGADOR WEB ---")
    print("1. Visitar nueva página")
    print("2. Retroceder")
    print("3. Ver página actual")
    print("4. Salir del programa")
    
    try:
        opcion = int(input("Opción elegida: "))
        match opcion:
            case 1:
                web = input("Ingrese la página web a visitar: ").strip()
                if web:
                    visitar(paginas_web, web)
                else:
                    print("ERROR: La página web no puede estar vacía.\n")
            case 2:
                retroceder(paginas_web)
            case 3:
                pagina_actual(paginas_web)
            case 4:
                print("Saliendo del programa...")
                break
            case _:
                print("ERROR: Selecciona una opción valida (1-4).\n")
    except ValueError:
        print("ERROR: Debe ingresar un número entero.\n")