
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

    porcentaje = (pagaronTot*debito)/100
    os.system("cls")
    total = str(pagaronTot)
    print "Pagaron con Debito el",porcentaje,"%, de ",total
    time.sleep(3)

def pagaronCredito(pagaronTot,credito):

    porcentaje = (pagaronTot*credito)/100
    total = str(pagaronTot)
    os.system("cls")
    print "Pagaron con Credito el",porcentaje,"%, de ",total
    time.sleep(3)

def pagaronEfectivo(pagaronTot,efectivo):

    porcentaje = (pagaronTot*efectivo)/100
    os.system("cls")
    total = str(pagaronTot)
    print "Pagaron en Efectivo el",porcentaje,"%, de ",total
    time.sleep(3)