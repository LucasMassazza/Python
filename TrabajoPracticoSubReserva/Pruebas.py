import random
from datetime import datetime, date, time, timedelta
import calendar
import os
import time


#Tipos de Aviones
class AvionBoeing:
    max737 = {"filas":29 , "columnas": 6}
class AvionAirbus:
    Neo320 = {"filas": 41,"columnas" : 4}


def numeroPar(num):

    if num % 0:
        return True

    return False

def fechaVuelo():
    os.system("cls")
    fecha = ""
    print "Favor ingrese una fecha de Vuelo, en el formato DD/MM/AAAA: "
    fecha = raw_input()

    fechaActual = datetime.now

    if len(fecha) == 10:

        if fecha[2] and fecha[5] == "/":

            mes = fecha[3:5]
            int(mes)

            dia = fecha[0:2]
            int(dia)

            if numeroPar(mes) :

                if dia <= 30 and mes >= fechaActual.day:

                    if 12 >= mes >= fechaActual.month:

                        ano = fecha[6:10]
                        int(ano)

                        if ano >= fechaActual.year:

                            print fecha

                        else:
                            os.system("cls")
                            print "Ingrese bien el Ano..."
                            time.sleep(3)

                    else:
                        os.system("cls")
                        print "Ingrese bien el Mes..."
                        time.sleep(3)
                else:

                    os.system("cls")
                    print "Ingrese bien el Dia..."
                    time.sleep(3)


            else:

                if dia <= 31 and mes >= fechaActual.day:

                    if 12 >= mes >= fechaActual.month:

                        ano = fecha[6:10]
                        int(ano)

                        if ano >= fechaActual.year:

                            print fecha

                        else:
                            os.system("cls")
                            print "Ingrese bien el Ano..."
                            time.sleep(3)

                    else:
                        os.system("cls")
                        print "Ingrese bien el Mes..."
                        time.sleep(3)
                else:

                    os.system("cls")
                    print "Ingrese bien el Dia..."
                    time.sleep(3)
        else:
            os.system("cls")
            print "No se ingreso bien el formato DD/MM/AAAA..."
            time.sleep(3)

    else:
        os.system("cls")
        print "Ingreso algun digito de mas, favor reintentar..."
        time.sleep(3)


def matriz():

    matriz = [[1,2,3],[4,5,6]]

    for x in range(len(matriz)):

        for y in range(len(matriz[0])):

            print matriz[x][y]


#Creacion de Asientos ocupados / no ocupados
def asientosAvion():

    matrizAsientos = []

    for x in range(AvionBoeing.max737.get("filas")):

        filaTemporal = []

        for y in range(AvionBoeing.max737.get("columnas")):

            numeroTemporal = random.choice([True,False])
            filaTemporal.append(numeroTemporal)


        matrizAsientos.append(filaTemporal)

    return matrizAsientos

fechaVuelo()



# matrizAsientos.append(filaTemporal)
 #           valorTemporal = random.randint(0,1)
  #          matrizAsientos[x][y] = valorTemporal