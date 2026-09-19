"""
Dado el siguiente arreglo de notas: [15, 18, 12, 9, 17, 14, 20, 11, 16, 13]
Escribir un programa que calcule: promedio, nota más alta, nota más baja y cuántos aprobaron (nota ≥ 11).
"""

notas= [15, 18, 12, 9, 17, 14, 20, 11, 16, 13]


def estadistica(notas):
    prom=sum(notas)/len(notas)
    n_alta=notas[0]
    n_baja=notas[0]

    for nota in notas:
        if nota>n_alta:
            n_alta=nota
    print(n_alta)



estadistica(notas)