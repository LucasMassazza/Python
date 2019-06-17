import os
import DatosPersonales
import DatosVuelo
import MediosDePago

class DatosPerosnales:
    nombre = ""
    apellido = ""
    dni = 0
    pasaporte = 0
    fechaNacimiento = ""
    mail = ""
    celular = 0

class DatosVuelo:
    origen = ""
    destino = ""
    horaInicio = ""
    horaFinal = ""
    puertaEmbarque = ""
    clase = ""
    asiento = ""
    fecha = ""

class MedioPago:
    medio = ""
    monto = 0


def menu():

    #Variables Para impresion Ticket

    datosPersonales = False
    datosVuelo = False
    medioDePago = False

    #Menu de Datos Varios
    cierreMenu = False
    os.system("cls")
    while cierreMenu != True:
        os.system("cls")
        print ("1. Datos Personales\n2. Datos de Vuelo\n3. Medio de Pago\n4. Impresion Ticket\n0. Salir\n")
        seleccionMenu = input()

        if seleccionMenu == 1:
            DatosPersonales.main()
        elif seleccionMenu == 2:
            DatosVuelo.main()
        elif seleccionMenu == 3:
            MediosDePago.main()
        elif seleccionMenu == 4:

            if datosPersonales and datosVuelo and medioDePago:
                ImpresionTicket()

        #En caso de faltar algun dato, se le muestra al usuario los datos faltantes, Falta a que se le redirija automaticamente

            else:
                if not datosPersonales:
                    os.system("cls")
                    print("Falta Ingresar algunos datos Personales... Ingreselos e intente nuevamente")

                elif not datosVuelo:
                    os.system("cls")
                    print("Falta Ingresar datos de vuelo... Ingreselos e intente nuevamente")

                elif not medioDePago:
                    os.system("cls")
                    print("No dio a conocer el medio de pago, favor de seleccionar alguno...")

        else:
            cierreMenu = True


def ImpresionTicket():
    return 0


