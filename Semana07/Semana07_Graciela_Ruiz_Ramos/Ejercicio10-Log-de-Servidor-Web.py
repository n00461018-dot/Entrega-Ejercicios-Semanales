'''
===== Ejercicio 10: Log de Servidor Web =====
Dado un log de servidor web (formato Apache),
extrae IP, método HTTP, ruta y código de 
estado de cada línea usando solo métodos de
strings.
'''

log_linea = '192.168.1.10 - - [10/Oct/2026:11:45:00 -0500] "GET /index.html HTTP/1.1" 200 1043'

partes_espacio = log_linea.split()
ip = partes_espacio[0]

partes_comillas = log_linea.split('"')

peticion = partes_comillas[1]

partes_peticion = peticion.split()
metodo = partes_peticion[0]
ruta = partes_peticion[1]

resto_linea = partes_comillas[2].strip().split()
codigo_estado = resto_linea[0]

print("=" * 30)
print("=== ANÁLISIS DE LOG DE SERVIDOR WEB ===")
print(f"Log inicial: {log_linea}")
print("=" * 30)
print("DATOS EXTRAIDOS")
print(f"IP Origen      : {ip}")
print(f"Método HTTP    : {metodo}")
print(f"Ruta solicitada: {ruta}")
print(f"Estado         : {codigo_estado}")