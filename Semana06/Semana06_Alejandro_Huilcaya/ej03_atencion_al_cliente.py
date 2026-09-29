from collections import deque

cola = deque()

def tomar_turno(cliente):
    #El cliente se agrega al final de la cola
    cola.append(cliente)
    print(f"Cliente {cliente} entra a la cola.")

def atender():
    #Solo se atiende si hay clientes esperando
    if cola:
        #Dequeue: sale el cliente que está al frente (el primero en llegar)
        cliente = cola.popleft()
        print(f"Cliente {cliente} atendido")
    else:
        print("No hay clientes en cola")


def mostrar_cola():
    #Se muestra el total de cola
    print("Clientes esperando:", len(cola))
    print("Cola:", list(cola))


#4 clientes entran
tomar_turno("Ana")
tomar_turno("Luis")
tomar_turno("María")
tomar_turno("Carlos")
mostrar_cola()

#Se atienden 2
atender()
atender()
mostrar_cola()

#Entra 1 más
tomar_turno("Sofía")
mostrar_cola()

#Se atienden todos
atender()
atender()
atender()
mostrar_cola()