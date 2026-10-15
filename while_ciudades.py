prompt = "\nIngresa el nombre de la ciudad que visitaste: "
prompt += "\n(Si quieres salir ingresa 'salir') "

while True:
    city = input(prompt)
    
    if city == "salir":
        break
    else:
        print(f"Amé visitar la ciudad de {city.title()}.")