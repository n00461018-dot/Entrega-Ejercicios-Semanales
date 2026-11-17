## 01 Saludo personalizado
#Crea una función saludar(nombre, saludo="Hola") que imprima
#"<saludo>, <nombre>!". Usa parámetro por defecto.
#Tip: f-string y parámetro con valor por defecto

#Se crea la función con un parametro por defecto
def saludar(nombre, saludo="Hola"):
    #Se imprime el saludo usando el fstring
    print(f"{saludo}, {nombre}!")

#Se ejecuta la función con parámetro por defecto y con parámetro personalizado
saludar("Elias Ramirez")
saludar("Ana Alfaro", "Saludos")