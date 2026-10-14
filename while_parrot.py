promt = "\nIngresa el texto que quieras..."
promt += "\nIngresa 'salir' para salir del juego..." #prompt es la variable que le usamos para indicarle al usuario lo que debe insertar

message = "" #está vacío porque el usuario insertará algo

active = True #es nuestra bandera
while active: #mientras nuestra bandera esté activa
    message = input(promt) #pedir al usuario que ingrese el mensaje
    
    if message == "salir": #si el mensaje es igual a "salir" entonces...
        active = False #desactivar la bandera y terminar el bucle
    else: #si la bandera no se desactiva, entonces...
        print(message) #imprimir el mensaje