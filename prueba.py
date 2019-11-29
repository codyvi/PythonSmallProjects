import math
#Pablo Gonzalez A00828065, Alfonso García A00829532, Rodrigo Perez A00828427
#Función principal
def menu (accion_principal,total_residencial,total_dinero,total_empresarial, cliente, lectactual, lectanterior, lectotal):

#opción del menú núm. 1
    if (accion_principal== 1):
        # datos (saque lo de bold en internet)
        print('\033[1m'"CONTROL DE INGRESOS DE COMISION FEDERAL DE ELECTRICIDAD")
        cliente = input('\033[0m'"Escriba el tipo de cliente (Residencial o Empresarial): ")
#a través de un while generamos un sistema que no permite que a los usuarios escribir otra cosa que no sea empresarial y residencial.
        while (cliente != "residencial" and cliente != "empresarial"):
            print("Tipo de cliente no valido, ")
            cliente = input("Ingresa un tipo de cliente nuevamente: ")
        lectactual = int(input("Escriba la lectura actual de electricidad en KW: "))
        lectanterior = int(input("Escriba la lectura anterior de electricidad en KW: "))
        lectotal = lectactual - lectanterior
        return cliente, lectactual, lectanterior, lectotal
        # datos con descuentos


#Sección 2 del menú
    if (accion_principal== 2 ):
        intento=input("ingresa la contraseña")
        contador_intentos = 3
        if intento == clave_acceso:
            if cliente == "residencial":
                total_residencial += 1
                

                if (lectactual > lectanterior and lectotal < 799 and lectotal > 400):
                    print("La cantidad de kilovatios consumidos es ", lectactual, " y el cliente tiene que pagar ",((lectactual * 35) - (lectanterior * 35)) * .75, "pesos porque tuvo un 25% de descuento.")
                    total_dinero += ((lectactual * 35) - (lectanterior * 35)) * .75
                elif (lectactual > lectanterior and lectotal > 0 and lectotal <= 399):
                    print("Si la lectura actual es ", lectactual, "y la lectura anterior ", lectanterior,
                          "el total es de", ((lectactual * 35) - (lectanterior * 35)) * .60, "pesos")
                    total_dinero += ((lectactual * 35) - (lectanterior * 35)) * .60
                else:
                    print("Si la lectura actual es ", lectactual, "y la lectura anterior ", lectanterior,
                          "el total es de", ((lectactual * 35) - (lectanterior * 35)), "pesos")
                    total_dinero += ((lectactual * 35) - (lectanterior * 35))

            elif (cliente == "empresarial"):
                total_empresarial += 1
                print("Si la lectura actual es ", lectactual, "y la lectura anterior ", lectanterior, "el total es de",
                      (lectactual * 60) - (lectanterior * 60), "pesos")
                total_dinero += (lectactual * 60) - (lectanterior * 60)
#Con un while hacemos que si se ingresa la contraseña más de tres veces el programa se cierra.
        while intento != clave_acceso:
            contador_intentos -= 1
            if contador_intentos <= 0:
                print("Excediste el número de intentos. Gracias por usar el programa, hasta luego. ")
                break;
            print("contraseña incorrecta")
            intento = input("Ingresa la contraseña nuevamente: ")
        
        if (cliente == 'residencial'):
            return total_dinero, total_residencial
        elif(cliente == 'empresarial'):
            return total_dinero, total_empresarial

#Opción 3 del menú comienza
    if (accion_principal==3):
        print("Bienvenido al resumen de clientes")
        print("El día de hoy " + str(total_residencial) +" clientes residenciales y, " + str(total_empresarial) +  " clientes empresariales han utilizado el programa.")
        print("Hoy se han acumulado " + str(total_dinero) + " de pesos.")

#inicia el programa

clave_acceso=input("Crea tu clave de acceso: ")
print("Bienvenido al menú principal")
print("1. Entrada de datos ")
print("2. Control de ingresos")
print("3. Resumen de clientes")
print("4. Salir")
#Se establecen las variables para el contador de personas que utilizaron el empresarial, el residencial y el dinero total que se recudará en el programa.
total_dinero = 0
total_residencial = 0
total_empresarial = 0
cliente = ""
lectactual = 0
lectanterior = 0
lectotal = 0
total_dinero = 0
#selecciona la opción del menú
accion_principal= int(input("Selecciona el número de la acción que quieres tomar: "))
contador_programa = 0
#Con este while la funcion menú se repite a menos que se seleccione la ocpión 4 que es la opción de salir.
while accion_principal != 4:
    if(accion_principal == 1):
        cliente, lectactual, lectanterior, lectotal = menu(accion_principal, total_residencial, total_dinero, total_empresarial, cliente, lectactual, lectanterior, lectotal)
    elif(accion_principal == 2):
        if(cliente == 'residencial'):
            total_dinero, total_residencial = menu(accion_principal, total_residencial, total_dinero, total_empresarial, cliente, lectactual, lectanterior, lectotal)
        elif(cliente == 'empresarial'):
            total_dinero, total_empresarial = menu(accion_principal, total_residencial, total_dinero, total_empresarial, cliente, lectactual, lectanterior, lectotal)
    elif(accion_principal == 3):
        menu(accion_principal, total_residencial, total_dinero, total_empresarial, cliente, lectactual, lectanterior, lectotal) 
    print("Bienvenido al menú principal")
    print("1. Entrada de datos ")
    print("2. Control de ingresos")
    print("3. Resumen de clientes")
    print("4. Salir")
    
    accion_principal = int(input("Selecciona el número de la acción que quieres tomar: "))
 
    

print("Gracias por usar el programa, hasta ")