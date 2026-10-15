sistema_abierto = True

while sistema_abierto:

    nombre = input("Ingresa tu nombre: ")
    
    if nombre == "" or nombre.isdigit():
        print(f"El nombre {nombre} es inválido...")
        continue

    edad = input("Ingresa tu edad: ")

    if not edad.isdigit():
        print(f"La edad {edad} es inválida...")
        continue
    else:
        print(f"Hola {nombre.title()}, tienes {edad} años de edad.")
    sistema_abierto = False