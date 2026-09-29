cola = []

def tomar_turno(cliente):
    cola.append(cliente)
    print(f"El cliente {cliente} ha tomado un turno.")
    print(f"Cola actual: {cola}")


def atender():
    if len(cola) > 0:
        cliente_atendido = cola.pop(0)
        print(f"Atendiendo al cliente: {cliente_atendido}")
    else:
        print("No hay clientes en espera.")


def mostrar_cola():
    print(f"Cantidad de clientes en espera: {len(cola)}")
    print(f"Clientes en la cola: {cola}")


# Entran 4 clientes
tomar_turno("Carlos")
tomar_turno("María")
tomar_turno("Pedro")
tomar_turno("Lucía")


mostrar_cola()


atender()
atender()


tomar_turno("Andrés")


mostrar_cola()


while len(cola) > 0:
    atender()


mostrar_cola()