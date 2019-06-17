import os
import MenuDatos

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
     while cierreMenu != True:
        os.system("cls")


        # Tipo de Datos a Ingresar, falta arreglar la vuelta al otro metodo.
        print ("1. Nombre y Apellido\n2. DNI o PASAPORTE\n3. Fecha Nacimiento\n4. Celular\n5. E-Mail\n0. Atras\n00. Salir")
        seleccionMenu = input()

        if seleccionMenu == 1:

             os.system("cls")
             nombre = raw_input ("Ingrese el nombre del Cliente: ")
             os.system("cls")
             apellido = raw_input("Ingrese el apellido del Cliente: ")

        elif seleccionMenu == 2:
            os.system("cls")
            tipoDocumente = input("\nQue documento utiliza el cliente: \n\n1. DNI\n2. PASAPORTE\n\n")

            if tipoDocumente == 1:
                os.system("cls")
                dni = input("Ingrese DNI: ")
            else:
                os.system("cls")
                numeroPasaporte = input("Ingrese el Numero de Pasaporte: ")

        elif seleccionMenu == 3:
            os.system("cls")
            fechaNacimiento = raw_input("Ingresar DD/MM/AAAA: ")

        elif seleccionMenu == 4:
            os.system("cls")
            celular = input("Ingrese el Numero de Celular: ")

        elif seleccionMenu == 5:
            os.system("cls")
            email = raw_input("Ingrese el E-Mail del Cliente: ")

        elif seleccionMenu == 0:

            MenuDatos.apellido = apellido
            MenuDatos.nombre = nombre
            MenuDatos.dni = dni
            MenuDatos.pasaporte = numeroPasaporte
            MenuDatos.fechaNacimiento = fechaNacimiento
            MenuDatos.mail = email
            MenuDatos.celular = celular
            cierreMenu = True

        else:
            cierreMenu = True
