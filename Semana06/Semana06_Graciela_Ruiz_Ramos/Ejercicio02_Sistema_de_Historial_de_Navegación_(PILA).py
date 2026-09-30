'''
======== EJERCICIO 2 – SISTEMA DE HISTORIAL DE NAVEGACIÓN (Pila) =======
Simula el historial de un navegador web usando una Pila (Stack).
El usuario visita páginas y puede retroceder.
a) Implementar visitar(url) → agrega la página a la pila y muestra la pila actual.
b) Implementar retroceder() → quita la última página y muestra a dónde regresó.
c) Implementar pagina_actual() → muestra la página actual sin quitarla.
d) Probar con: Google → YouTube → GitHub → retroceder → retroceder.
'''

historial = []

def visitar(url):
    historial.append(url)
    print(f"\n[+] Visitando: {url}")

def retroceder():
    if historial:
        pagina_eliminada = historial.pop()
        print(f"\n[-] Retrocediendo... Salimos de: {pagina_eliminada}")
        pagina_actual()
    else:
        print("\n[!] El historial está vacío. No puedes retroceder más.")

def pagina_actual():
    if historial:
        print(f"[*] Página actual: {historial[-1]}")
    else:
        print("[*] No hay páginas abiertas (Página de inicio).")

def mostrar_historial():
    if historial:
        print(f"\n[PILA ACTUAL]: {historial} <-- (El último es tu posición actual)")
    else:
        print("\n[PILA ACTUAL]: []")

continuar = 's'

while continuar == 's' or continuar == 'si':
    print("\n" + "="*35)
    print("         NAVEGADOR WEB ")
    print("="*35)
    print("1. Visitar nueva página")
    print("2. Retroceder (Atrás)")
    print("3. Ver página actual")
    print("4. Ver estado del historial (Pila)")
    
    opcion = input("\nElige una opción (1-4): ")
    
    if opcion == '1':
        nueva_url = input("Ingresa la URL o nombre de la página (ej. google.com): ")
        visitar(nueva_url)
    elif opcion == '2':
        retroceder()
    elif opcion == '3':
        pagina_actual()
    elif opcion == '4':
        mostrar_historial()
    else:
        print("\n[!] Opción no válida. Por favor, intenta de nuevo.")

    print("\n" + "-"*35)
    respuesta = input("¿Deseas continuar navegando? (s/n): ")
    
    continuar = respuesta.strip().lower()

print("\nCerrando navegador... ¡Hasta luego y gracias por practicar!")