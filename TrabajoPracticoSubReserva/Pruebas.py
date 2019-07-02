import random
from datetime import datetime, date, timedelta
import os
import time


# Tipos de Aviones
class AvionBoeing:
    max737 = {"filas": 29, "columnas": 6}
class AvionAirbus:
    Neo320 = {"filas": 41, "columnas": 4}


def numeroPar(num):
    if num % 2 == 0:
        return True

    return False


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

                            return fecha

                        else:
                            os.system("cls")
                            print "Ingreso el dia de manera erronea, favor reintentar..."
                            time.sleep(3)

                    else:

                        if dia > fechaActual.day and dia <= 31:

                            return fecha

                        else:
                            os.system("cls")
                            print "Ingreso el dia de manera erronea, favor reintentar..."
                            time.sleep(3)

                elif mes > fechaActual.month:

                    if numeroPar(mes):

                        if 0 < dia <= 30:

                            return fecha

                        else:
                            os.system("cls")
                            print "Ingreso el dia de manera erronea, favor reintentar..."
                            time.sleep(3)

                    else:

                        if 0 < dia <= 31:

                            return fecha

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

                            return fecha

                        else:
                            os.system("cls")
                            print "Ingreso el dia de manera erronea, favor reintentar..."
                            time.sleep(3)

                    else:

                        if fechaActual.day < dia <= 31:

                            return fecha

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

                            return fecha

                        else:
                            os.system("cls")
                            print "Ingreso el dia de manera erronea, favor reintentar..."
                            time.sleep(3)

                    else:

                        if dia > fechaActual.day and dia <= 31:

                            return fecha

                        else:
                            os.system("cls")
                            print "Ingreso el dia de manera erronea, favor reintentar..."
                            time.sleep(3)

                elif mes > fechaActual.month:

                    if numeroPar(mes):

                        if 0 < dia <= 30:

                            return fecha

                        else:
                            os.system("cls")
                            print "Ingreso el dia de manera erronea, favor reintentar..."
                            time.sleep(3)

                    else:

                        if 0 < dia <= 31:

                            return fecha

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

                            return fecha

                        else:
                            os.system("cls")
                            print "Ingreso el dia de manera erronea, favor reintentar..."
                            time.sleep(3)

                    else:

                        if 0 < dia <= 31:

                            return fecha

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

        if len(fecha)<8:
            os.system("cls")
            print "Ingreso algun digito de menos, favor reintentar..."
            time.sleep(3)

        else:
            os.system("cls")
            print "Ingreso algun digito de mas, favor reintentar..."
            time.sleep(3)

    print fecha

def matriz():
    matriz = [[1, 2, 3], [4, 5, 6]]

    for x in range(len(matriz)):

        for y in range(len(matriz[0])):
            print matriz[x][y]


def asientosAvion():
    matrizAsientos = []

    for x in range(AvionBoeing.max737.get("filas")):

        filaTemporal = []

        for y in range(AvionBoeing.max737.get("columnas")):
            numeroTemporal = random.choice([True, False])
            filaTemporal.append(numeroTemporal)

        matrizAsientos.append(filaTemporal)

    return matrizAsientos


fechaVuelo()

