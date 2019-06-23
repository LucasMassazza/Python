import random
import datetime


#Tipos de Aviones
class AvionBoeing:
    max737 = {"filas":29 , "columnas": 6}
class AvionAirbus:
    Neo320 = {"filas": 41,"columnas" : 4}



def fechaVuelo():
    FechaFinal = ""
    fechaActual = datetime.datetime.now()
    print "Favor ingrese una fecha de Vuelo, en el formato DD/MM/AAAA: "

    diaActual = fechaActual.day
    mesActual = fechaActual.month
    anoActual = fechaActual.year

    str(diaActual)
    str(mesActual)
    str(anoActual)

    FechaFinal = diaActual
    FechaFinal += "/"
    FechaFinal += mesActual
    FechaFinal += "/"
    FechaFinal += anoActual



    print FechaFinal


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

asientosAvion()


# matrizAsientos.append(filaTemporal)
 #           valorTemporal = random.randint(0,1)
  #          matrizAsientos[x][y] = valorTemporal