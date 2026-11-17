## 08 Importar módulo propio
#Importa matematicas_utils con alias mu y crea
#reporte_geometrico(radios) que muestre área y perímetro de cada
#círculo en una tabla.
#Tip: import matematicas_utils as mu — usa mu.area_circulo(r)

#Se importa el módulo propio con el alias mu
import matematicas_utils as mu

#Se crea la función que usa la función area_circulo y calciula 
def reporte_geometrico(radios):
    #Se muestra el encabezado con los valores
    print(f"{'Radio':<7}{'Área':<10}{'Perímetro':<10}")
    #Se recorre cada radio para calcular área y perímetro usando area_circulo
    for radio in radios:
        area = mu.area_circulo(radio)
        perimetro = 2 * mu.pi * radio
        #Por cada valor calculado se muestra el radio, área y perímetro
        print(f"{radio:<7}{area:<10.2f}{perimetro:<10.2f}")

#Se ejecuta la función dandole una lista de radios
reporte_geometrico([1,2,5,10,4,12,15])