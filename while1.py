promt = "\nIngresa el texto que quieras..."
promt += "\nIngresa 'salir' para salir del juego..." #prompt es la variable que le usamos para indicarle al usuario lo que debe insertar

message = "" #está vacío porque el usuario insertará algo

while message != "salir": #mientras el mensaje sea diferente a "salir"
    message = input(promt) #ingresa el mensaje
    
    if message != "salir": #si el mensaje es disferente a "salir" entonces...
        print(message) #imprime el mensaje