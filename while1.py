promt = "\nIngresa el texto que quieras..."
promt += "\nIngresa 'salir' para salir del juego..."

message = ""

while message != "salir":
    message = input(promt)
    
    if message != "salir":
        print(message)