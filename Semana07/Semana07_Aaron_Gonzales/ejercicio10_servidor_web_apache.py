"""
Dado un log de servidor web (formato Apache), extrae IP, método HTTP, ruta y código de estado de cada línea usando
solo métodos de strings.
"""

log = '192.168.1.50 - - [06/Oct/2026:21:30:15 -0500] "POST /api/login HTTP/1.1" 200 4532'

seccion = log.split('"')

ip = seccion[0].split()[0]

metodo = seccion[1].split()[0]

ruta = seccion[1].split()[1]

codigo_estado = seccion[2].split()[0]

print(f"Dirección IP: {ip}")
print(f"Método HTTP: {metodo}")
print(f"Ruta: {ruta}")
print(f"Código de estado: {codigo_estado}")