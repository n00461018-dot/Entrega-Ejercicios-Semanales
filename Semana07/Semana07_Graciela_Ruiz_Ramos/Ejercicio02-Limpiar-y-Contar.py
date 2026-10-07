'''
=== Ejercicio 02 - Limpiar y Contar ===
Dada la cadena ' Python es divertido ', 
elimina los espacios en los extremos y 
cuenta cuántos caracteres tiene la
cadena limpia.
'''
cadena = ' Python es divertido '
cadena_limpia = cadena.strip()
print(f"La cadena original es: '{cadena}'")
print(f"La cadena limpia es: '{cadena_limpia}'")
print(f"La cantidad de caracteres en la cadena limpia es: {len(cadena_limpia)}")