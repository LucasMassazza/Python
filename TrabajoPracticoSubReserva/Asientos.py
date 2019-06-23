import MenuPrincipal
import random

#Crea un avion con asientos aleatorios
def llenadoAleatorioAvion():

    matrizAsientos = []

    for x in range(MenuPrincipal.AvionBoeing.max737.get("filas")):

        filaTemporal = []

        for y in range(MenuPrincipal.AvionBoeing.max737.get("columnas")):

            numeroTemporal = random.choice([True,False])
            filaTemporal.append(numeroTemporal)


        matrizAsientos.append(filaTemporal)

    return matrizAsientos

#Avion con asientos Vacios
def avionVacio ():

    avion = []
    for x in range(MenuPrincipal.AvionBoeing.max737.get("columnas")):
        listaTemporal = []
        for y in random(MenuPrincipal.AvionBoeing.max737.get("filas")):
            listaTemporal.append(False)

        avion.append(listaTemporal)

    return avion


