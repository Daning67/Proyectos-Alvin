#7-2. Asientos en restaurantes: Escribe un programa que pregunte al usuario cuántas personas hay en su grupo de cena. Si la respuesta es más de ocho, imprime un mensaje diciendo que tendrán que esperar una mesa. Si no, informa que su mesa está lista.

asientos = input("¿Cuántas personas hay en tu grupo de cena?")
asientos = int(asientos)

if asientos > 8:
    print("Tendrán que esperar una mesa...")
else:
    print("Tu mesa está lista")