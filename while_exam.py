Estudiantes = []
nombre = input("Ingresa tu nombre: ")

sistema_abierto = True
while sistema_abierto:
    
    if nombre == "" or nombre ==  int(nombre):
        print(f"El nombre {nombre} es inválido")
        break
    else:
        print(int("Ingresa tu edad: "))