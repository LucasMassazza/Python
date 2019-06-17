import MenuDatos
import os
import CalculoEstadisticas
import sys


caluloEstadisticas = CalculoEstadisticas
menu = MenuDatos

pagosDebito = 0
pagosCredito = 0
personasTot = 0
pagosEfectivo = 0


def main():
    cierrePrograma = False
    cierreMenu = False
    seleccionOpcionMenu = 0
    
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

def tituloYSaludo():
    print ("\033[1;36m")
    print ("BIENVENIDOS A CHAU BIONDI").center(50,"=")
    print ("")
    print ("\033[1;31m""SISTEMA DE RESERVA""\033[0m").center(60)
    print ("")                                                      

main()




