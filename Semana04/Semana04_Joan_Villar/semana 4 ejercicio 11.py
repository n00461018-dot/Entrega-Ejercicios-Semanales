def crear_interruptor():
    estado = False

    def cambiar():
        nonlocal estado
        estado = not estado
        return "ON" if estado else "OFF"
    return cambiar
switch = crear_interruptor()
print(switch()) # ON
print(switch()) # OFF
print(switch()) # ON