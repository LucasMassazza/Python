
import os
import time

def menuEstadisticas():
    from MenuPrincipal import variablesVarias
    os.system("cls")
    print ("1. Estadistica Debito\n2. Estadistica Credito\n3. Estadistica Efectivo")
    seleccionMenu = input()
    if seleccionMenu==1:
        pagaronDebito(variablesVarias.personasTot, variablesVarias.pagosDebito)
    elif seleccionMenu==2 :
        pagaronCredito(variablesVarias.personasTot, variablesVarias.pagosCredito)

    #CORREGIR ELIF
    else:
        pagaronEfectivo(variablesVarias.personasTot, variablesVarias.pagosEfectivo)






def pagaronDebito(pagaronTot,debito):
    from MenuPrincipal import variablesVarias
    porcentaje = (pagaronTot*debito)/100
    os.system("cls")
    print ("Pagaron con Debito el"+porcentaje+"%, de"+variablesVarias.personasTot)
    time.sleep(3)

def pagaronCredito(pagaronTot,credito):
    from MenuPrincipal import variablesVarias
    porcentaje = (pagaronTot*credito)/100
    os.system("cls")
    print ("Pagaron con Credito el"+porcentaje+"%, de"+variablesVarias.personasTot)
    time.sleep(3)

def pagaronEfectivo(pagaronTot,efectivo):
    from MenuPrincipal import variablesVarias
    porcentaje = (pagaronTot,efectivo)
    os.system("cls")
    print ("Pagaron en Efectivo el"+porcentaje+"%, de"+variablesVarias.personasTot)
    time.sleep(3)