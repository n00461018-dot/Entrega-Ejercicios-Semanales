historial = []



def visitar(url):
    historial.append(url)
    print(f"Visitando: {url}")
    print(f"Historial actual: {historial}")



def retroceder():
    if len(historial) > 1:
        pagina_anterior = historial.pop()
        print(f"Retrocediendo desde: {pagina_anterior}")
        print(f"Regresaste a: {historial[-1]}")
        print(f"Historial actual: {historial}")
    else:
        print("No hay una página anterior para regresar.")



def pagina_actual():
    if len(historial) > 0:
        print(f"Página actual: {historial[-1]}")
    else:
        print("No hay ninguna página abierta.")



visitar("Google")
visitar("YouTube")
visitar("GitHub")

pagina_actual()

retroceder()
retroceder()

pagina_actual()