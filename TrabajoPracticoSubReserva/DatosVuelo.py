
import os
import time
import MenuDatos

variables = MenuDatos






def menu():

    cierreMenu = False
    while not cierreMenu:
        os.system("cls")
        print("1. Punto de Origen y Destino\n2. Fecha de Vuelo\n3. Hora de Vuelo\n4. Detalles de Asiento\n0. Atras\n")
        eleccionMenu = input()

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
         os.system("cls")
         print ("1. Origen\n2. Destino\n0. Atras\n\n")
         eleccion = input()


         #ELECCION DE ORIGEN
         if eleccion == 1:
             os.system("cls")
             print ("Elija el punto de Origen del Vuelo:\n\n1. Buenos Aires (BUE)\n2. Baricloche (BAR)\n3. Iguazu (IGU)\n\n")
             eleccion = input()

             if eleccion == 1:
                 variables.ClaseDatosVuelo.origen = "BUE"


             elif eleccion == 2:
                 variables.ClaseDatosVuelo.origen = "BAR"


             elif eleccion == 3:
                 variables.ClaseDatosVuelo.origen = "IGU"

             else:

                 #En caso de ingresar cualquier Verdura, Se muestra la siguiente leyenda y da unos segundos de pausa
                 print ("Favor de ingresar un dato Correcto...")
                 time.sleep(3)

         #ELECCION DE DESTINO
         elif eleccion == 2:
             os.system("cls")
             print ("Elija el punto de Destino del Vuelo:\n\n1. Buenos Aires (BUE)\n2. Baricloche (BAR)\n3. Iguazu (IGU)\n\n")
             eleccion = input()

             if eleccion == 1:
                     variables.ClaseDatosVuelo.destino = "BUE"


             elif eleccion == 2:
                     variables.ClaseDatosVuelo.destino = "BAR"


             elif eleccion == 3:
                     variables.ClaseDatosVuelo.destino = "IGU"

             else:
                     # En caso de ingresar cualquier Verdura, Se muestra la siguiente leyenda y da unos segundos de pausa
                     os.system("cls")
                     print ("Favor de ingresar un dato Correcto...")
                     time.sleep(3)

         #ELECCION DE SALIDA
         elif eleccion == 0:

             if variables.ClaseDatosVuelo.origen == variables.ClaseDatosVuelo.destino:

                 print "Debe ingresar un Origen distinto al Destino o Viceversa..."
                 time.sleep(3)
             else:
                 cierreMenu = True

def fechaVuelo():

    os.system("cls")
    print "Favor ingrese una fecha de Vuelo, en el formato DD/MM/AAAA: "



    variables.ClaseDatosVuelo.fecha = raw_input()

    #Falta realizar una comprobacion de lo que se ingresa, Ano dia y Fecha

def horaVuelo():

    os.system("cls")
    print "Ingresar hora de vuelo: "
    variables.ClaseDatosVuelo.horaInicio = raw_input()

#def detalleAsiento():




