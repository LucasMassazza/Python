import Inicio

inicio = Inicio


def menu():

    print ("1. Estadistica Debito\n2. Estadistica Credito\n3. Estadistica Efectivo")
    seleccionMenu = input()
    if(seleccionMenu==1):
        pagaronDebito(inicio.personasReservaron,inicio.pagosDebito)
    elif(seleccionMenu==2):
        pagaronCredito(inicio.personasReservaron,inicio.pagosCredito)
    else:
        pagaronEfectivo(inicio.personasReservaron,inicio.pagosEfectivo)






def pagaronDebito(pagaronTot,debito):
    porcentaje = (pagaronTot*debito)/100
    print ("Pagaron con Debito el"+porcentaje+"%")

def pagaronCredito(pagaronTot,credito):
    porcentaje = (pagaronTot*credito)/100
    print ("Pagaron con Credito el"+porcentaje+"%")

def pagaronEfectivo(pagaronTot,efectivo):
    porcentaje = (pagaronTot,efectivo)
    print ("Pagaron en Efectivo el"+porcentaje+"%")