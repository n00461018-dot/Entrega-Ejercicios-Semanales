"""
Simula el sistema de turnos de un banco usando una Cola (Queue). Los clientes esperan en orden de
llegada.
a) Implementar tomar_turno(cliente) → cliente entra a la cola.
b) Implementar atender() → el primer cliente de la cola es atendido (sale).
c) Implementar mostrar_cola() → mostrar cuántos esperan y sus nombres.
d) Simular: 4 clientes entran, se atienden 2, entra 1 más, se atienden todos.
"""

from collections import deque

def tomar_turno(cola, cliente):
    cola.append(cliente)
    print(f"Cliente {cliente} tomó su turno.\n")
    
def atender(cola):
    if not cola:
        print("No hay ningún cliente actualmente.\n")
    else:
        atendido = cola.popleft()
        print(f"Atendiendo a {atendido}\n")
    
def mostrar_cola(cola):
    if cola: 
        nombres = ", ".join(cola)
        print(f"Están en espera {len(cola)} clientes. Los clientes son: {nombres}\n")
    else: 
        print("No hay nadie en cola\n")


cola = deque()
while True:
    print("--- BANCO / SISTEMA DE TURNOS ---")
    print("1. Agregar un nuevo cliente")
    print("2. Atender")
    print("3. Mostrar cola")
    print("4. Salir del programa")
        
    try:
        opcion = int(input("Opción elegida: "))
        match opcion:
            case 1:
                usuarios = input("Ingrese el nombre del cliente: ").strip()
                if usuarios:
                    tomar_turno(cola, usuarios)
                else:
                    print("ERROR: Tiene que haber al menos un usuario.\n")
            case 2:
                atender(cola)
            case 3:
                mostrar_cola(cola)
            case 4:
                print("Saliendo del programa...")
                break
            case _:
                print("ERROR: Selecciona una opción valida (1-4).\n")
    except ValueError:
        print("ERROR: Debe ingresar un número entero.\n")
            
    

