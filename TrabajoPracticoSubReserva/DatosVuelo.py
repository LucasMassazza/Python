
import os
import time
import MenuDatos

variables = MenuDatos


def main():



    cierreMenu = False
    while not cierreMenu:
        os.system("cls")
        print("1. Punto de Origen y Destino\n2. Fecha de Vuelo\n3. Hora de Vuelo\n4. Detalles de Asiento\n0. Atras")
        eleccionMenu = raw_input()

        #Eleccion del Menu

        if eleccionMenu == 1:
            origenYDestino()

        elif eleccionMenu == 2:
            fechaVuelo()

        elif eleccionMenu == 3:
            horaVuelo()

        elif eleccionMenu == 4:#detalleAsiento()
            print "HOLA"

        else:
            return 0

def origenYDestino(): #En esta funcion se ingresan los datos de Origen y Destino
     os.system("cls")

     #Menu De seccion de Origen
     cierreMenu = False

     while not cierreMenu:

         print ("1. Origen\2. Destino\n0. Atras\n\n")
         eleccion = input()

         if eleccion == 1:
             print ("Elija el punto de Origen del Vuelo:\n\n1. Buenos Aires (BUE)\n2. Baricloche (BAR)\n3. Iguazu (IGU)\n\n")
             eleccion = input()

             if eleccion == 1:
                 variables.DatosVuelo.origen = "BUE"
                 cierreMenu = True

             elif eleccion == 2:
                 variables.DatosVuelo.origen = "BAR"
                 cierreMenu = True

             elif eleccion == 3:
                 variables.DatosVuelo.origen = "IGU"
                 cierreMenu = True
             else:

                 #En caso de ingresar cualquier Verdura, Se muestra la siguiente leyenda y da unos segundos de pausa
                 print ("Favor de ingresar un dato Correcto...")
                 time.sleep(3)


         elif eleccion == 2:

             if eleccion == 1:
                 print (
                     "Elija el punto de Destino del Vuelo:\n\n1. Buenos Aires (BUE)\n2. Baricloche (BAR)\n3. Iguazu (IGU)\n\n")
                 eleccion = input()

                 if eleccion == 1:
                     variables.DatosVuelo.destino = "BUE"
                     cierreMenu = True

                 elif eleccion == 2:
                     variables.DatosVuelo.destino = "BAR"
                     cierreMenu = True

                 elif eleccion == 3:
                     variables.DatosVuelo.destino = "IGU"
                     cierreMenu = True
                 else:

                     # En caso de ingresar cualquier Verdura, Se muestra la siguiente leyenda y da unos segundos de pausa
                     print ("Favor de ingresar un dato Correcto...")
                     time.sleep(3)

         elif eleccion == 0:

             if variables.DatosVuelo.origen == variables.DatosVuelo.destino:

                 print "Debe ingresar un Origen distinto al Destino o Viceversa..."
                 time.sleep(3)
             else:
                 cierreMenu = True


def fechaVuelo():

    os.system("cls")
    print "Favor ingrese una fecha de Vuelo, en el formato DD/MM/AAAA: "
    variables.DatosVuelo.fecha = raw_input()

    #Falta realizar una comprobacion de lo que se ingresa, Año dia y Fecha

def horaVuelo():

    os.system("cls")
    print "Ingresar hora de vuelo: "
    variables.DatosVuelo.horaInicio = raw_input()

#def detalleAsiento():




