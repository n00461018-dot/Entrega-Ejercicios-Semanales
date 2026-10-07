logs = [
    '192.168.1.10 - - [06/Oct/2026:10:15:20] "GET /index.html HTTP/1.1" 200 1024',
    '192.168.1.20 - - [06/Oct/2026:10:16:10] "POST /login HTTP/1.1" 404 512'
]

for linea in logs:
    datos = linea.split()

    ip = datos[0]
    metodo = datos[5].replace('"', '')
    ruta = datos[6]
    estado = datos[8]

    print("IP:", ip)
    print("Método:", metodo)
    print("Ruta:", ruta)
    print("Código de estado:", estado)
    print("----------------------")