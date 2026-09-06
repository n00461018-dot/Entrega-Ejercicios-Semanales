def calcular_promedio(notas):

    prome=round(sum(notas) / len(notas),2)
    nmin=min(notas)
    nmax=max(notas)

    return prome,nmin,nmax


def  mostrar_resultado(nombre,notas):
    
    prom,mn,mx = calcular_promedio(notas)
    
    print("Calculadora de notas con Lista")    
    print(f"La nota promedio del estudiante {nombre} es {prom}")
    print(f"La nota más baja del estudiante {nombre} es {mn}")
    print(f"La nota más alta del estudiante {nombre} es {mx}")


lista_notas=[15,20,18,12,14,10,20]
mostrar_resultado("Alejandro Huilcaya",lista_notas)
