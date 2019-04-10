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
    puertaEmbarque = ""
    clase = ""
    asiento = ""

class MedioPago:
    medio = ""
    monto = 0


def menu():
    cierreMenu = False
    os.system("cls")
    while cierreMenu != True:
        os.system("cls")
        print ("1. Datos Personales\n2. Datos de Vuelo\n3. Medio de Pago\n0. Salir\n")
        seleccionMenu = input()

        if seleccionMenu == 1:
            DatosPersonales.main()
        elif seleccionMenu == 2:
            DatosVuelo.main()
        elif seleccionMenu == 3:
            MediosDePago.main()
        else:
            cierreMenu = True

