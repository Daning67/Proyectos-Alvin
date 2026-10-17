#SISTEMA DE REGISTRO DE VENTAS DE CUADERNO

## Declaración de constantes
precio_cuaderno = 3.50
desc_1 = 0.00 #Compras menores a 4 cuadernos
desc_2 = 0.08 #Compras entre 5 y 9 cuadernos
desc_3 = 0.15 #Compras a partir de 10 cuadernos 
descuento_venta = 0
costo_r = 0.00 #Costo de envio para retiro en tienda (R)
costo_e = 2.00 #Total < 30
Subtotal_P_Desc = 35.00
puedo_calcular = True

## Declaración de INPUTS
cuadernos = int(input("Digite la cantidad de cuadernos: ").strip())
if cuadernos < 0:
    print("La cantidad de cuadernos debe ser mayor que cero (0).")
    puedo_calcular = False
    
modalidad = input("Digite la modalidad de despacho, R(Retiro) o  E(Entrega): ").upper().strip()
if modalidad not in ("R", "E"): #modalidad != "R" or modalidad != "E"
    print("La modalidad debe ser R (Retiro) o E (Entrega)")
    puedo_calcular = False
    
if cuadernos <= 4:
    descuento_venta = desc_1
elif cuadernos <= 9:
    descuento_venta = desc_2
else:
    descuento_venta + desc_3

if puedo_calcular:
    subtotal = cuadernos * precio_cuaderno
    descuento_dolares = subtotal * descuento_venta
    valor_con_descuento = subtotal - descuento_dolares
    if modalidad == "R":
        costo_entrega = costo_r
    else:
        if valor_con_descuento >= Subtotal_P_Desc:
            costo_entrega = 0
        else:
            costo_entrega = costo_e
    print(f"La cantidad de cuadernos es: {cuadernos}")
    print(f"Subtotal es: ${subtotal:,.2f}")
    print(f"Descuento en dolares ($): ${descuento_dolares:,.2f}")
    print(f"Valor con descuento ${subtotal - descuento_dolares:,.2f}")
    print(f"Costo de envío ${costo_entrega:,.2f}")
    print(f"Total a pagar: ${valor_con_descuento + costo_entrega:,.2f}")
else:
    print("No es posible calcular.")
    
    
    
#OUTPUTS

"DON'T REPEAT YOURSELF"
