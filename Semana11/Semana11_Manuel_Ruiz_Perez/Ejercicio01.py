##Saludo personalizado 

def saludar(nombre, saludo="Hola"):
    
    print(f"{saludo}, {nombre}!")

# 1. Usando el parámetro por defecto ("Hola")
saludar("Manuel") 
# Salida: Hola, Manuel!

# 2. Especificando un saludo personalizado
saludar("Manuel", "Buenos días") 
# Salida: Buenos días, Manuel!