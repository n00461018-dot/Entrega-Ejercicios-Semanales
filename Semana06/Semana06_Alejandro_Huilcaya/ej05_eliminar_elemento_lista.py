"""
Eliminar elemento repetido de una lista

"""

def borrar_ocurrencia(lista, elemento, n):
    contador = 0
    for i, item in enumerate(lista):
        if item == elemento:
            contador += 1
            if contador == n:
                lista.pop(i)
                print(f"Se elimina el elemento {elemento} del indice {i} de la lista inicial")
                break

# Se crea la lista inicial
lista = ["Uva", "Pera", "Uva","Naranja", "Manzana", "Uva"]
print("Lista inicial:",lista)

#Se usa la función dandole el elemento y el número de ocurrencia a eliminar
borrar_ocurrencia(lista, "Uva", 2)

print("Lista final:",lista)
