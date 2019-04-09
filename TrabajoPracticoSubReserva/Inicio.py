import Menu
import os
import VariablesAccesibles

menu = Menu
variables = VariablesAccesibles

pagosDebito = 0
pagosCredito = 0
personasReservaron = 0
pagosEfectivo = 0


def main():
    cierrePrograma = False
    cierreMenu = False
    seleccionOpcionMenu = 0

    tituloYSaludo()

    while cierrePrograma != True:

        os.system("cls")
        tituloYSaludo()
        print ("1. Ingresar Datos\n2. Estadisticas\n0. Salir")
        if(seleccionOpcionMenu == 1):
            return 0
        elif(seleccionOpcionMenu ==1):
            menu.menu()



main()


def tituloYSaludo():
    print ("\033[1;36m")
    print ("BIENVENIDOS A CHAU BIONDI").center(50, "=")
    print ("")
    print ("\033[1;31m""SISTEMA DE SUB RESERVA""\033[0m").center(60)
    print ("")

