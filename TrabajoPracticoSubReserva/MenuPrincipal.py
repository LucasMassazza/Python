import MenuDatos
import os
import CalculoEstadisticas
import sys


#Los diferentes aviones que maneja la Empresa y Caracteristicas de capacidad
class AvionBoeing:
    max737 = {"filas":29 , "columnas": 6}
class AvionAirbus:
    Neo320 = {"filas": 41,"columnas" : 4}


#Referencias a Objetos
caluloEstadisticas = CalculoEstadisticas
menu = MenuDatos


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
           caluloEstadisticas.menu()
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




