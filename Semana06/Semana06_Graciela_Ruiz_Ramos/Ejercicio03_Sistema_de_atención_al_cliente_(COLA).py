'''
============= EJERCICIO 3 – SISTEMA DE ATENCIÓN AL CLIENTE (Cola) ============
Simula el sistema de turnos de un banco usando una Cola (Queue).
Los clientes esperan en orden de llegada.
a) Implementar tomar_turno(cliente) → cliente entra a la cola.
b) Implementar atender() → el primer cliente de la cola es atendido (sale).
c) Implementar mostrar_cola() → mostrar cuántos esperan y sus nombres.
d) Simular: 4 clientes entran, se atienden 2, entra 1 más, se atienden todos.
'''

from collections import deque

cola_turnos = deque()

def tomar_turno(cliente):
    cola_turnos.append(cliente)
    print(f"Ticket emitido para: {cliente}")

def atender():
    if cola_turnos:
        cliente_atendido = cola_turnos.popleft()
        print(f"Atendiendo en ventanilla a: {cliente_atendido}")
    else:
        print("No hay clientes en espera.")

def mostrar_cola():
    print(f"Clientes en espera ({len(cola_turnos)}): {list(cola_turnos)}")

print("\n===== Ingresan 4 clientes ======")
tomar_turno("Ana")
tomar_turno("Luis")
tomar_turno("Carlos")
tomar_turno("María")
mostrar_cola()

print("\n===== Se atienden 2 clientes ======")
atender()
atender()
mostrar_cola()

print("\n===== Entra 1 cliente más ======")
tomar_turno("Pedro")
mostrar_cola()

print("\n===== Se atienden todos ======")
while cola_turnos:
    atender()