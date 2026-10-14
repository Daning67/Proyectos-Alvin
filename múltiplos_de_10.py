#7-3. Múltiplos de diez: Pide al usuario un número y luego informa si el número es múltiplo de 10 o no.

number = input("Ingresa un número: ")
numer = int(number)

if numer % 10 == 0:
    print(f"El número {number} es múltiplo de 10.")
else:
    print(f"El número {number} NO es múltiplo de 10.")