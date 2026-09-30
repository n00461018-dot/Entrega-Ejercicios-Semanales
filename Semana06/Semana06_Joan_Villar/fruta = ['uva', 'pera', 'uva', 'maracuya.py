fruta = ['uva', 'pera', 'uva', 'maracuya']

print("Lista original:")
print(fruta)

# Buscamos la segunda vez que aparece una fruta
for i in range(len(fruta)):
    for j in range(i + 1, len(fruta)):
        
        if fruta[i] == fruta[j]:
            fruta.pop(j)
            break
    
    else:
        continue
    
    break

print("Lista después de eliminar la segunda incidencia:")
print(fruta)