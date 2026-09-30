historial = []

def visitar(pagina):
    historial.append(pagina)
    print("Visitando:", pagina)
    print("Historial:", historial)


def retroceder():
    if len(historial) > 1:
        historial.pop()
        print("Regresó a:", historial[-1])
    else:
        print("No hay páginas anteriores")


def pagina_actual():
    if len(historial) > 0:
        print("Página actual:", historial[-1])
    else:
        print("No hay página actual")


# Prueba
visitar("Google")
visitar("YouTube")
visitar("GitHub")

retroceder()
retroceder()

pagina_actual()