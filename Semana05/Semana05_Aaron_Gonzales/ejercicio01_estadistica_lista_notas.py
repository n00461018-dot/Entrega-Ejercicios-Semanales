"""
Dado el siguiente arreglo de notas: [15, 18, 12, 9, 17, 14, 20, 11, 16, 13]
Escribir un programa que calcule: promedio, nota más alta, nota más baja y cuántos aprobaron (nota ≥ 11).
"""

def calculo_curso(notas): 
    
    alumnos_aprobados = 0
    promedio = sum(notas) / len(notas)
    nota_alta = max(notas)
    nota_baja = min(notas)
    
    for i, valor in enumerate(notas):
        if valor >= 11:
            alumnos_aprobados += 1
    
    return promedio, nota_alta, nota_baja, alumnos_aprobados
   
def mostrar_resultados(notas):
    
    promedio, nota_alta, nota_baja, alumnos_aprobados = calculo_curso(notas)
   
    print("")
    print("="*60)
    print("\t\tREPORTE DE NOTAS DE LOS ALUMNOS")
    print("="*60)
    print(f"\nLos estudiantes tienen un promedio de {promedio}")
    print(f"\nLa nota mínima es: {nota_baja}")
    print(f"\nLa nota máxima es: {nota_alta}")
    print(f"\nAprobaron {alumnos_aprobados} alumnos en total.\n")
    print("="*60)
    
    
    
lista_notas = [15, 18, 12, 9, 17, 14, 20, 11, 16, 13]
calculo_curso(lista_notas)
mostrar_resultados(lista_notas)