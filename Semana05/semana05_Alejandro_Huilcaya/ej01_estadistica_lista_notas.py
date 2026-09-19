"""
Dado el siguiente arreglo de notas: [15, 18, 12, 9, 17, 14, 20, 11, 16, 13]
Escribir un programa que calcule: promedio, nota más alta, nota más baja y cuántos aprobaron (nota ≥ 11).
"""

notas= [15, 18, 12, 9, 17, 14, 20, 11, 16, 13]


def estadistica(notas):
    prom=sum(notas)/len(notas)
    n_alta=notas[0]
    n_baja=notas[0]
    aprobados=0
    for nota in notas:
        if nota>n_alta:
            n_alta=nota
        if nota<n_baja:
            n_baja=nota
        if nota>=11:
            aprobados+=1

    print(f"Promedio: {prom} | Max: {n_alta} | Min: {n_baja} | Aprobados: {aprobados}")

    
estadistica(notas)