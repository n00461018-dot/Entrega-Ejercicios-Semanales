"""
Escribe una función calcular_promedio(notas) que reciba una lista de notas y retorne el promedio,
la nota mínima y la nota máxima. Además crea una función mostrar_resultado(nombre, notas) sin retorno 
que muestre un reporte formateado
"""
def calcular_promedio(notas):
    promedio = sum(notas) / len(notas)
    return promedio

def mostrar_resultado(nombre, notas):
    print("")
    print("="*60)
    print("\t\tREPORTE DE NOTAS DEL ALUMNO")
    print("="*60)
    print(f"\nAlumno seleccionado: {nombre}")
    print(f"\nEl estudiante seleccionado tiene un promedio de {calcular_promedio(notas)}")
    print(f"\nSu nota mínima es: {min(notas)}")
    print(f"\nSu nota máxima es: {max(notas)}\n")
    print("="*60)
    
alumNombre = input("Ingrese el nombre del alumno: ")
listNotas = []

while True:
    try:
        notas = float(input("Ingrese la(s) nota(s) del alumno: "))
        if 0 <= notas <= 20:
            listNotas.append(notas)
            continuar = input("¿Desea ingresar más notas? (s/n): ")
            if continuar != "s":
                break
        else: 
            print("Ingresa un número entre 0 y 20")
    except ValueError:
        print("Ingresa un valor valido ")

calcular_promedio(listNotas)
mostrar_resultado(alumNombre, listNotas)    