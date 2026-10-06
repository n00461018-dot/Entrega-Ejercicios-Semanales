"""
Dado un log de servidor web (formato Apache), extrae IP, método HTTP, ruta y código de estado de cada línea usando solo métodos de strings.

"""

log = """192.168.1.10 - - [05/Oct/2026:10:00:12] "GET /inicio HTTP/1.1" 200 1234
10.0.0.15 - - [05/Oct/2026:10:01:05] "POST /contacto HTTP/1.1" 404 532
172.16.0.4 - - [05/Oct/2026:10:02:40] "GET /productos HTTP/1.1" 500 2048"""

def procesar_log(log_texto):
    
    #Se separa el log por cada salto de linea y se recorre
    for linea in log_texto.splitlines():
        #Se dividen los elementos de la linea con espacio
        partes = linea.split()
        
        #Se obtiene la IP ubicada en el indice 0
        ip = partes[0]
        #Se extrae el método HTTP limpiando la comilla doble inicial
        metodo = partes[5].replace('"', '')
        #Se extrae la ruta de la peticion
        ruta = partes[6].replace('"', '')
        #Se extrae el codigo de estado HTTP 
        estado = partes[8]
        
        #Se imprimen los datos de la linea
        print("IP:", ip, "| Método:", metodo, "| Ruta:", ruta, "| Estado:", estado)

procesar_log(log)