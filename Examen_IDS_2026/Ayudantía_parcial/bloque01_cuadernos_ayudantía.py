#SISTEMA DE REGISTRO DE VENTAS DE CUADERNO

## Declaración de constantes
precio_cuaderno = 3.50
desc_1 = 0.00 #Compras menores a 4 cuadernos
desc_2 = 0.08 #Compras entre 5 y 9 cuadernos
desc_3 = 0.15 #Compras a partir de 10 cuadernos 
costo_r = 0.00 #Costo de envio para retiro en tienda (R)
costo_e = 2.00 #Total < 30
Subtotal_P_Desc = 30.00

## Declaración de INPUTS
cuadernos = int(input("Digite la cantidad de cuadernos: "))
if cuadernos < 0:
    print("La cantidad de cuadernos debe ser mayor que cero (0).")
        
modalidad = input("Digite la modalidad de despacho, R(Retiro) o  E(Entrega): ").upper().strip()
if modalidad not in ("R", "E"): #modalidad != "R" or modalidad != "E"
    print("La modalidad debe ser R (Retiro) o E (Entrega)")
    
    
    
#OUTPUTS

"DON'T REPEAT YOURSELF"
