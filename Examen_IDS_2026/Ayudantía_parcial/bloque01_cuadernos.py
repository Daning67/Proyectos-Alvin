#Bloque 1 Compra de cuadernos
#Archivo bloque01_cuadernos.py · Tiempo orientativo 45 a 60 minutos"""

#Una librería universitaria vende cuadernos para el inicio del ciclo. Cada cuaderno cuesta
#$3.50. Una compra de 5 a 9 cuadernos obtiene 8% de descuento sobre el valor de los cuadernos; una 
#de 10 o más obtiene 15%. Las compras menores de 5 no reciben descuento.
print("BIENVENIDO \nSi deseas salir escribe '0'")
active = True

while active: 
    cuaderno = 3.50
    cantidad = int(input("Ingrese la cantidad de cuadernos que desea comprar: "))
    precio_total = cuaderno * cantidad
    descuento_1 = precio_total * 0.08 #De 5 a 9 cuadernos
    descuento_2 = precio_total * 0.15 #De 10 cuadernos en adelante
    
    if cantidad == 0:
        active = False
        print("Saliste del sistema")
    else:
        if cantidad < 0:
            print("Opción inválida")
        else:
            if cantidad >= 1 and cantidad <= 4:
                print(f"\nCompras menores a 5 cuadernos no aplican a descuento \nEl precio total es: ${precio_total}")
            else:
                if cantidad >= 5 and cantidad < 10:
                    print(f"El precio total es: ${precio_total} \nEl precio total con descuento es ${precio_total - descuento_1}")
                else:
                    print(f"El precio total es: ${precio_total} \nEl precio total con descuento es: ${precio_total - descuento_2}")
#La persona compradora indica una cantidad entera y elige retiro en tienda (R) o entrega (E). El
#retiro no cuesta; la entrega cuesta $2.00. Si el valor de los cuadernos después del descuento 
#llega a $30.00, la entrega es gratuita. La entrega no forma parte de la base sobre la que se
#calcula el descuento


