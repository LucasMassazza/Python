import os
import MenuDatos

def main():
     """
     Nombre
     Apellido
     DNI o PASAPORTE
     Fecha Nacimiento
     Mail
     Celular
     """
     cierreMenu = False

     while cierreMenu != True:
        os.system("cls")
        print ("1. Nombre y Apellido\n2. DNI o PASAPORTE\n3. Fecha Nacimiento\n4. Celular\n5. E-Mail\n0. Atras\n00. Salir")
        seleccionMenu = input()

        if seleccionMenu == 1:

             os.system("cls")
             nombre = raw_input ("Ingrese el nombre del Cliente: ")
             apellido = raw_input("Ingrese el apellido del Cliente: ")

        elif seleccionMenu == 2:

            tipoDocumente = input("\nQue documento utiliza el cliente: \n\n1. DNI\n2. PASAPORTE")

            if tipoDocumente == 1:
                dni = input("Ingrese DNI: ")
            else:
                numeroPasaporte = input("Ingrese el Numero de Pasaporte: ")

        elif seleccionMenu == 3:

            fechaNacimiento = raw_input("Ingresar DD/MM/AAAA")

        elif seleccionMenu == 4:

            celular = input("Ingrese el Numero de Celular: ")

        elif seleccionMenu == 5:

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
