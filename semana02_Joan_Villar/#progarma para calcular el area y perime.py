#progarma para calcular el area y perimetro de un rectangulo
base = float(input("ingrese la base: "))
altura = float(input("ingtese la altura: "))

#operacion del area 
area = base * altura

#operacion del perimetro
perimetro = 2* (base + altura)

#imprimir resultados 
print ("******resultados******")
print (f"Area: {area}")
print (f"Perimetro: {perimetro}")
print ("**********************")