import os
import MenuDatos
import time

def main():

     cierreMenu = False

    #Inicio del Menu de insecion de Datos
     apellido = ""
     nombre = ""
     dni = 0
     numeroPasaporte = 0
     fechaNacimiento = ""
     email = ""
     celular = 0

     #Verificadores
     nombreV = False
     apellidoV = False
     dniV = False
     numeroPasaporteV = False
     fechaNacimiento = False
     email = False
     celularV = False

     while cierreMenu != True:
        os.system("cls")


        # Tipo de Datos a Ingresar, falta arreglar la vuelta al otro metodo.
        print ("1. Nombre y Apellido\n2. DNI o PASAPORTE\n3. Fecha Nacimiento\n4. Celular\n5. E-Mail\n0. Atras\n00. Salir sin guardar\n")
        seleccionMenu = input()

        if seleccionMenu == 1:

             os.system("cls")
             nombre = raw_input ("Ingrese el nombre del Cliente: ")
             nombreV = True
             os.system("cls")
             apellido = raw_input("Ingrese el apellido del Cliente: ")
             apellidoV = True

        elif seleccionMenu == 2:
            os.system("cls")
            tipoDocumente = input("\nQue documento utiliza el cliente: \n\n1. DNI\n2. PASAPORTE\n\n")

            if tipoDocumente == 1:


                os.system("cls")
                dni = input("Ingrese DNI: ")

                if dni > 100000000:
                    os.system("cls")
                    print "Ingrese un DNI correcto..."
                    dni = 0
                    time.sleep(3)
                else:
                    dniV = True

            else:
                os.system("cls")
                numeroPasaporte = input("Ingrese el Numero de Pasaporte: ")
                numeroPasaporteV = True

        elif seleccionMenu == 3:
            os.system("cls")
            fechaNacimiento = raw_input("Ingresar DD/MM/AAAA: ")
            fechaNacimientoV = True

        elif seleccionMenu == 4:
            os.system("cls")
            celular = input("Ingrese el Numero de Celular: ")

            celularV = True

        elif seleccionMenu == 5:
            os.system("cls")
            email = raw_input("Ingrese el E-Mail del Cliente: ")

            if email.find("@"):
                emailV = True

            else:
                os.system("cls")
                print "No ingreso correctamente el E-Mail..."
                time.sleep(3)

        elif seleccionMenu == 0:

            if nombreV and apellidoV and emailV and fechaNacimientoV and celularV:

                if dniV or numeroPasaporteV:

                    MenuDatos.apellido = apellido
                    MenuDatos.nombre = nombre
                    MenuDatos.dni = dni
                    MenuDatos.pasaporte = numeroPasaporte
                    MenuDatos.fechaNacimiento = fechaNacimiento
                    MenuDatos.mail = email
                    MenuDatos.celular = celular
                    MenuDatos.datosPersonales = True
                    cierreMenu = True

                else:
                    os.system("cls")
                    print "Falta ingresar el DNI o Pasaporte..."
                    time.sleep(3)
            else:
                os.system("cls")
                print "Falta algun dato por ingresar..."
                time.sleep(3)


        else:
            cierreMenu = True
