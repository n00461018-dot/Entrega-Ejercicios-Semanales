cola = []

def tomar_turno(cliente):
    cola.append(cliente)
    print(cliente, "tomo un turno")

def atender():
    if len(cola) > 0:
        cliente = cola.pop(0)
        print("Atendiendo a:", cliente)
    else:
        print("No hay clientes")

def mostrar_cola():
    print("Clientes esperando:", len(cola))
    print("Cola:", cola)


# Entran 4 clientes
tomar_turno("Juan")
tomar_turno("Pedro")
tomar_turno("Maria")
tomar_turno("Ana")

mostrar_cola()

# Se atienden 2
atender()
atender()

# Entra 1 cliente mas
tomar_turno("Luis")

mostrar_cola()

# Se atienden todos
atender()
atender()
atender()

mostrar_cola()