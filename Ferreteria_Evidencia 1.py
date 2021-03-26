modo_default = "\033[m"

pedido = {}
choice = 1

SEPARADOR = ("-" * 30)

def menu():
 
    correcto=False
    num=0
    while(not correcto):
        try:
            num= int(input(" Elija la opción que desee: "))
            print(SEPARADOR)
            correcto=True
        except ValueError:
            print("¡ERROR! Introduce el número correspondiente a la opción elegida.")
     
    return num
 
salir = False
opcion = 0
 
while not salir:
    print("*** FERRETERIA ESPERANZA***")
    print(SEPARADOR)
    print(SEPARADOR)
    print ("1. Registrar una venta")
    print ("2. Consultar una venta")
    print ("3. Salir")
    print(SEPARADOR)
 
    opcion = menu()
    
 
    if opcion == 1:
        print(SEPARADOR)
        print("*** FERRETERIA ESPERANZA***")
        print ("*** Registro de nueva venta ***")
        print(SEPARADOR)
        while choice == 1:
            if pedido:
                clave = max(pedido) + 1
            else:
                clave = 1
                
            nombre=input("Nombre del artículo: ")
            descripcion=input("Descripción del artículo: ")
            cantidad=int(input("Cantidad de piezas vendidas: "))
            precio=float(input("Precio de venta: "))
            t_venta= (precio*cantidad)
            print("Total:", t_venta)
            registro = [nombre,descripcion,cantidad,precio,t_venta]
            pedido[clave] = registro
            print(SEPARADOR)
            print(f"\nSe agregaron los datos:\n {registro} con la clave {clave}")
            break
        choice = int(input(f"\n ¿Desea realizar otra acción? \n (1-SI / 0-NO): \n"))
        print(SEPARADOR)
        
    elif opcion == 2:
        clave_buscar = int(input("Dime la clave de venta que deseas consultar: "))
        print(SEPARADOR)
        if clave_buscar in pedido.keys():
            print(pedido[clave_buscar])
        else:
            print(f"Lo sentimos, la clave que ingreso no esta registrada.{modo_default}")
        choice = int(input(f"\n ¿Desea realizar otra acción? \n (1-SI / 0-NO): \n"))
        
    elif opcion == 3:
        salir = True
    else:
        print("¡ERROR! Introduce el número correspondiente a la opción elegida.")
print(SEPARADOR)       
print ("Fin del proceso.")