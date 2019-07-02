import os
import MenuDatos
import time

def main():

    cierreMenu = False
    while not cierreMenu:

        os.system("cls")
        print "Elija el medio de pago con el cual va utilizar:\n\n1. Debito\n2. Credito\n3. Efectivo\n"
        eleccionMenu = input()

        if eleccionMenu == 1:
            MenuDatos.MedioPago.medio =  "Debito"
            cierreMenu = True

        elif eleccionMenu == 2:
            MenuDatos.MedioPago.medio = "Credito"
            cierreMenu = True
        elif eleccionMenu == 3:
            MenuDatos.MedioPago.medio = "Efectivo"
            cierreMenu = True

        else:
            os.system("cls")
            print "Favor ingrese una opcion correcta..."
            time.sleep(3)


