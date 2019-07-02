
import os

def menuEstadisticas():
    import MenuPrincipal
    os.system("cls")
    print ("1. Estadistica Debito\n2. Estadistica Credito\n3. Estadistica Efectivo")
    seleccionMenu = input()
    if seleccionMenu==1:
        pagaronDebito(MenuPrincipal.personasTot, MenuPrincipal.pagosDebito)
    elif seleccionMenu==2 :
        pagaronCredito(MenuPrincipal.personasTot, MenuPrincipal.pagosCredito)

    #CORREGIR ELIF
    else:
        pagaronEfectivo(MenuPrincipal.personasTot, MenuPrincipal.pagosEfectivo)






def pagaronDebito(pagaronTot,debito):
    porcentaje = (pagaronTot*debito)/100
    os.system("cls")
    print ("Pagaron con Debito el"+porcentaje+"%")

def pagaronCredito(pagaronTot,credito):
    porcentaje = (pagaronTot*credito)/100
    os.system("cls")
    print ("Pagaron con Credito el"+porcentaje+"%")

def pagaronEfectivo(pagaronTot,efectivo):
    porcentaje = (pagaronTot,efectivo)
    os.system("cls")
    print ("Pagaron en Efectivo el"+porcentaje+"%")