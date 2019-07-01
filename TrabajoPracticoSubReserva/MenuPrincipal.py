import MenuDatos
import os
import CalculoEstadisticas
import sys
import random


#Los diferentes aviones que maneja la Empresa y Caracteristicas de capacidad
class AvionBoeing:
    max737 = {"filas":29 , "columnas": 6}
class AvionAirbus:
    Neo320 = {"filas": 41,"columnas" : 4}

#Crea un avion con asientos aleatorios
def llenadoAleatorioAvion():

    matrizAsientos = []

    for x in range(AvionBoeing.max737.get("filas")):

        filaTemporal = []

        for y in range(AvionBoeing.max737.get("columnas")):

            numeroTemporal = random.choice([True,False])
            filaTemporal.append(numeroTemporal)


        matrizAsientos.append(filaTemporal)

    return matrizAsientos

#Avion con asientos Vacios
def avionVacio ():

    avion = []
    for x in range(AvionBoeing.max737("columnas")):
        listaTemporal = []
        for y in random(AvionBoeing.max737("filas")):
            listaTemporal.append(False)

        avion.append(listaTemporal)

    return avion

#Avion generado o Importado
avionViaje = avionVacio()

#Referencias a Objetos
caluloEstadisticas = CalculoEstadisticas
menu = MenuDatos

class variablesAsiento():

    numero = 0
    letra = ""

#Variables globales
class variablesVarias():
    pagosDebito = 0
    pagosCredito = 0
    personasTot = 0
    pagosEfectivo = 0

#Codigo del menu de arranque
def main():
    cierrePrograma = False
    
    while cierrePrograma != True:

        os.system("cls")
        tituloYSaludo()
        print ("1. Ingresar Datos\n2. Estadisticas\n0. Salir\n\n")
        seleccionOpcionMenu = input()
        if seleccionOpcionMenu == 1:
           menu.menu()
        elif seleccionOpcionMenu ==2:
           caluloEstadisticas.menuEstadisticas()
        else:
           sys.exit()


#Generador del Titulo
def tituloYSaludo():
    print ("\033[1;36m")
    print ("BIENVENIDOS A CHAU BIONDI").center(50,"=")
    print ("")
    print ("\033[1;31m""SISTEMA DE RESERVA, CABOTAJE""\033[0m").center(60)
    print ("")                                                      


main()




