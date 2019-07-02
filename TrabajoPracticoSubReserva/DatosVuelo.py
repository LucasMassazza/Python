import os
import time
import MenuDatos
from datetime import datetime, date, timedelta


def menu():
    cierreMenu = False
    while not cierreMenu:
        os.system("cls")
        print("1. Punto de Origen y Destino\n2. Fecha de Vuelo\n3. Hora de Vuelo\n4. Detalles de Asiento\n0. Atras\n")
        eleccionMenu = input()

        # Eleccion del Menu

        if eleccionMenu == 1:
            origenYDestino()

        elif eleccionMenu == 2:
            fechaVuelo()

        elif eleccionMenu == 3:
            horaVuelo()

        elif eleccionMenu == 4:
            menuAsientos()

        else:
            return 0

def origenYDestino():  # En esta funcion se ingresan los datos de Origen y Destino
    os.system("cls")

    # Menu De seccion de Origen
    cierreMenu = False

    while not cierreMenu:
        os.system("cls")
        print ("1. Origen\n2. Destino\n0. Atras\n\n")
        eleccion = input()

        # ELECCION DE ORIGEN
        if eleccion == 1:
            os.system("cls")
            print (
                "Elija el punto de Origen del Vuelo:\n\n1. Buenos Aires (BUE)\n2. Baricloche (BAR)\n3. Iguazu (IGU)\n\n")
            eleccion = input()

            if eleccion == 1:
                MenuDatos.ClaseDatosVuelo.origen = "BUE"


            elif eleccion == 2:
                MenuDatos.ClaseDatosVuelo.origen = "BAR"


            elif eleccion == 3:
                MenuDatos.ClaseDatosVuelo.origen = "IGU"

            else:

                # En caso de ingresar cualquier Verdura, Se muestra la siguiente leyenda y da unos segundos de pausa
                print ("Favor de ingresar un dato Correcto...")
                time.sleep(3)

        # ELECCION DE DESTINO
        elif eleccion == 2:
            os.system("cls")
            print (
                "Elija el punto de Destino del Vuelo:\n\n1. Buenos Aires (BUE)\n2. Baricloche (BAR)\n3. Iguazu (IGU)\n\n")
            eleccion = input()

            if eleccion == 1:
                MenuDatos.ClaseDatosVuelo.destino = "BUE"


            elif eleccion == 2:
                MenuDatos.ClaseDatosVuelo.destino = "BAR"


            elif eleccion == 3:
                MenuDatos.ClaseDatosVuelo.destino = "IGU"

            else:
                # En caso de ingresar cualquier Verdura, Se muestra la siguiente leyenda y da unos segundos de pausa
                os.system("cls")
                print ("Favor de ingresar un dato Correcto...")
                time.sleep(3)

        # ELECCION DE SALIDA
        elif eleccion == 0:

            if MenuDatos.ClaseDatosVuelo.origen == MenuDatos.ClaseDatosVuelo.destino:
                os.system("cls")
                print "Debe ingresar un Origen distinto al Destino o Viceversa..."
                time.sleep(3)
            else:
                cierreMenu = True

def fechaVuelo():
    os.system("cls")
    fecha = ""
    print "Favor ingrese una fecha de Vuelo, en el formato DD/MM/AAAA: "
    fecha = raw_input()

    fechaActual = datetime.now().date()

    if len(fecha) == 10:

        if fecha[2] and fecha[5] == "/":

            mes = fecha[3:5]
            mes = int(mes)

            dia = fecha[0:2]
            dia = int(dia)

            ano = fecha[6:10]
            ano = int(ano)

            if ano == fechaActual.year:

                if mes == fechaActual.month:

                    if numeroPar(mes):

                        if dia > fechaActual.day and dia <= 30:

                            MenuDatos.ClaseDatosVuelo.fecha = fecha

                        else:
                            os.system("cls")
                            print "Ingreso el dia de manera erronea, favor reintentar..."
                            time.sleep(3)

                    else:

                        if dia > fechaActual.day and dia <= 31:

                            MenuDatos.ClaseDatosVuelo.fecha = fecha

                        else:
                            os.system("cls")
                            print "Ingreso el dia de manera erronea, favor reintentar..."
                            time.sleep(3)

                elif mes > fechaActual.month:

                    if numeroPar(mes):

                        if 0 < dia <= 30:

                            MenuDatos.ClaseDatosVuelo.fecha = fecha

                        else:
                            os.system("cls")
                            print "Ingreso el dia de manera erronea, favor reintentar..."
                            time.sleep(3)

                    else:

                        if 0 < dia <= 31:

                            MenuDatos.ClaseDatosVuelo.fecha = fecha

                        else:
                            os.system("cls")
                            print "Ingreso el dia de manera erronea, favor reintentar..."
                            time.sleep(3)

                else:
                    os.system("cls")
                    print "Ingreso un mes menor al actual, favor intente nuevamente..."
                    time.sleep(3)

            elif ano > fechaActual.year:

                if 0 < mes <= 12:

                    if numeroPar(mes):

                        if fechaActual.day < dia <= 30:

                            MenuDatos.ClaseDatosVuelo.fecha = fecha

                        else:
                            os.system("cls")
                            print "Ingreso el dia de manera erronea, favor reintentar..."
                            time.sleep(3)

                    else:

                        if fechaActual.day < dia <= 31:

                            MenuDatos.ClaseDatosVuelo.fecha = fecha

                        else:
                            os.system("cls")
                            print "Ingreso el dia de manera erronea, favor reintentar..."
                            time.sleep(3)

            else:
                os.system("cls")
                print "Ingreso el ano de manera erronea, Intente nuevamente..."
                time.sleep(3)

        else:
            os.system("cls")
            print "No se ingreso bien el formato DD/MM/AAAA..."
            time.sleep(3)

    elif len(fecha) == 8:

        if fecha[1] and fecha[3] == "/":

            mes = fecha[2]
            mes = int(mes)

            dia = fecha[0]
            dia = int(dia)

            ano = fecha[4:8]
            ano = int(ano)

            if ano == fechaActual.year:

                if mes == fechaActual.month:

                    if numeroPar(mes):

                        if dia > fechaActual.day and dia <= 30:

                            MenuDatos.ClaseDatosVuelo.fecha = fecha

                        else:
                            os.system("cls")
                            print "Ingreso el dia de manera erronea, favor reintentar..."
                            time.sleep(3)

                    else:

                        if dia > fechaActual.day and dia <= 31:

                            MenuDatos.ClaseDatosVuelo.fecha = fecha

                        else:
                            os.system("cls")
                            print "Ingreso el dia de manera erronea, favor reintentar..."
                            time.sleep(3)

                elif mes > fechaActual.month:

                    if numeroPar(mes):

                        if 0 < dia <= 30:

                            MenuDatos.ClaseDatosVuelo.fecha = fecha

                        else:
                            os.system("cls")
                            print "Ingreso el dia de manera erronea, favor reintentar..."
                            time.sleep(3)

                    else:

                        if 0 < dia <= 31:

                            MenuDatos.ClaseDatosVuelo.fecha = fecha

                        else:
                            os.system("cls")
                            print "Ingreso el dia de manera erronea, favor reintentar..."
                            time.sleep(3)

                else:
                    os.system("cls")
                    print "Ingreso un mes menor al actual, favor intente nuevamente..."
                    time.sleep(3)

            elif ano > fechaActual.year:

                if 0 < mes <= 12:

                    if numeroPar(mes):

                        if 0 < dia <= 30:

                            MenuDatos.ClaseDatosVuelo.fecha = fecha

                        else:
                            os.system("cls")
                            print "Ingreso el dia de manera erronea, favor reintentar..."
                            time.sleep(3)

                    else:

                        if 0 < dia <= 31:

                            MenuDatos.ClaseDatosVuelo.fecha = fecha

                        else:
                            os.system("cls")
                            print "Ingreso el dia de manera erronea, favor reintentar..."
                            time.sleep(3)

            else:
                os.system("cls")
                print "Ingreso el ano de manera erronea, Intente nuevamente..."
                time.sleep(3)

        else:
            os.system("cls")
            print "No se ingreso bien el formato DD/MM/AAAA..."
            time.sleep(3)

    else:

        if len(fecha) < 8:
            os.system("cls")
            print "Ingreso algun digito de menos, favor reintentar..."
            time.sleep(3)

        else:
            os.system("cls")
            print "Ingreso algun digito de mas, favor reintentar..."
            time.sleep(3)

def horaVuelo():
    os.system("cls")
    print "Ingresar hora de vuelo (HH:MM): "

    hora = raw_input()

    horas = hora[0:2]
    horas = int(horas)

    minutos = hora[3:5]
    minutos = int(minutos)

    if (0 <= horas < 24 ) and (0 <= minutos < 60):

        MenuDatos.ClaseDatosVuelo.horaInicio = hora

    else:
        os.system("cls")
        print "Ingreso mal la hora de la reserva, intente nuevamente..."
        time.sleep(3)

def menuAsientos():
    from MenuPrincipal import avionViaje
    from MenuPrincipal import variablesAsiento
    os.system("cls")
    for x in range(avionViaje("filas")):

        for y in range(avionViaje("columnas")):

            if avionViaje[x][y]:

                if avionViaje[x][y] == 1:
                    variablesAsiento.letra = "A"
                if avionViaje[x][y] == 2:
                    variablesAsiento.letra = "B"
                if avionViaje[x][y] == 3:
                    variablesAsiento.letra = "C"
                if avionViaje[x][y] == 4:
                    variablesAsiento.letra = "D"
                if avionViaje[x][y] == 5:
                    variablesAsiento.letra = "E"
                if avionViaje[x][y] == 6:
                    variablesAsiento.letra = "F"

                variablesAsiento.numero = x

    print ("Su codigo de asiento es: ", variablesAsiento.letra, variablesAsiento.numero)

    print ("\n\nPara volver al Menu presionar ENTER")
    salir = input()

    os.system("cls")

def numeroPar(num):

    if num % 2 == 0:
        return True

    return False