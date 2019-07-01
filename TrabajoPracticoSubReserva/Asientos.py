import MenuPrincipal
import os





def menuAsientos():

    os.system("cls")
    for x in range(MenuPrincipal.AvionBoeing.max737("filas")):

        for y in range(MenuPrincipal.AvionBoeing.max737("columnas")):

            if MenuPrincipal.avionViaje[x][y] == True:

                if MenuPrincipal.avionViaje[x][y] == 1:
                    MenuPrincipal.variablesAsiento.letra = "A"
                if MenuPrincipal.avionViaje[x][y] == 2:
                    MenuPrincipal.variablesAsiento.letra = "B"
                if MenuPrincipal.avionViaje[x][y] == 3:
                    MenuPrincipal.variablesAsiento.letra = "C"
                if MenuPrincipal.avionViaje[x][y] == 4:
                    MenuPrincipal.variablesAsiento.letra = "D"
                if MenuPrincipal.avionViaje[x][y] == 5:
                    MenuPrincipal.variablesAsiento.letra = "E"
                if MenuPrincipal.avionViaje[x][y] == 6:
                    MenuPrincipal.variablesAsiento.letra = "F"

                MenuPrincipal.variablesAsiento.numero = x

    print ("Su codigo de asiento es: ",MenuPrincipal.variablesAsiento.letra,MenuPrincipal.variablesAsiento.numero)

    print ("\n\nPara volver al Menu presionar ENTER")
    salir = input()

    os.system("cls")



