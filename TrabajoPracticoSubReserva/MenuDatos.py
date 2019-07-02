import os
import DatosPersonales
import DatosVuelo
import MediosDePago
import time


class DatosPerosnales:
    nombre = ""
    apellido = ""
    dni = 0
    pasaporte = 0
    fechaNacimiento = ""
    mail = ""
    celular = 0

class ClaseDatosVuelo:
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

#Variables Para impresion Ticket
datosPersonales = False
datosVuelo = False
medioDePago = False


def menu():
    from MenuPrincipal import variablesVarias
    cierreMenu = False

    os.system("cls")

    while cierreMenu != True:
        os.system("cls")
        print ("1. Datos Personales\n2. Datos de Vuelo\n3. Medio de Pago\n4. Realizar Reserva\n0. Volver al Menu Principal\n")
        seleccionMenu = input()

        if seleccionMenu == 1:
            DatosPersonales.main()
        elif seleccionMenu == 2:
            DatosVuelo.menu()
        elif seleccionMenu == 3:
            MediosDePago.main()
        elif seleccionMenu == 4:

            if datosPersonales and datosVuelo and medioDePago:

                if MedioPago.medio == "Debito":
                    variablesVarias.pagosDebito+=1
                elif MedioPago.medio == "Credito":
                    variablesVarias.pagosCredito += 1
                else:
                    variablesVarias.pagosEfectivo += 1




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



        elif seleccionMenu == 0:
            cierreMenu = True

        else:
            print "Favor ingrese una opcion valida..."
            time.sleep(3)
            os.system("cls")




