"""
================== EJERCICIO 06 ==================
Solicita un número N y muestra todos los números
primos desde 2 hasta N. Para cada número, verifica
si es divisible entre 2 y hasta su raíz cuadrada.
"""
#Resolucion del ejercicio

n = int(input("Ingrese un número: "))
print("\n" + "=" * 35)
print(f"\nEVALUACION DE NUMEROS ENTRE 2 Y {n}\n")
print("=" * 35 + "\n")

for num in range(2, n + 1):
    es_primo = True
    
    raiz = num ** 0.5

    limite = int(raiz)
    
    for i in range(2, limite + 1):
        if num % i == 0:
            es_primo = False 
            break
    
    div_entre_2 = "Sí" if (num % 2 == 0) else "No"
    
    resultado = "ES PRIMO" if es_primo else "NO ES PRIMO"
    
    print(f"Número: {num:2d} | ¿Divisible entre 2?: {div_entre_2:<2}")
    print(f"Raíz cuadrada: {raiz:.2f} | Resultado: {resultado}\n")
