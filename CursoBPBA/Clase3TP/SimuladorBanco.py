class ClienteBanco:

    def __init__(self, nombre, apellido, dni, tipo_cuenta, saldo): 
        self.nombre=nombre
        self.apellido=apellido
        self.dni=dni
        self.tipo_cuenta=tipo_cuenta
        self.saldo=saldo
    
    def __str__(self):

        return "Nombre {}\nApellido: {}\nDNI: {}\nTipo de Cuenta: {}\nSaldo: ${}".format(self.nombre,self.apellido,self.dni,self.tipo_cuenta,self.saldo)

    def Depositar(self, dinero):

        self.saldo = self.saldo + dinero
        print(f"Saldo Actualizado {self.saldo}\nGracias {self.apellido}, {self.nombre}")

    def Retiro(self, dinero):

        if self.saldo - dinero > 0:

            self.saldo = self.saldo - dinero
            print(f"Saldo Restante {self.saldo}\n")
        else:
            print("Dinero Insuficiente...")

    def ConsultarSaldo(self):
        
        print(f"Su saldo es {self.saldo}")

class ClientePremium(ClienteBanco):
    
    def __init__(self, nombre, apellido, dni, tipo_cuenta, saldo, categoria):
        self.categoria = categoria
        super().__init__(nombre, apellido, dni, tipo_cuenta, saldo)

    def __str__(self):
        return "Nombre {}\nApellido: {}\nDNI: {}\nTipo de Cuenta: {}\nSaldo: ${}\nCategoria: {}".format(self.nombre,self.apellido,self.dni,self.tipo_cuenta,self.saldo,self.categoria)

    def Beneficios (self):
        if self.categoria == "Platinium":
            print(f"Querido {self.apellido}, {self.nombre} al ser {self.categoria} sus beneficios son:\n\nEntradas Exclusivas\nPeaje Gratis\nFilas sin colas")
        else:
            print(f"Querido {self.apellido}, {self.nombre} al ser {self.categoria} sus beneficios son:\n\nEntradas Exclusivas\nPeaje Gratis\nFilas sin colas\nVIP en aeropuertos\nDescuento en Nafta")
    
        

def Transferencia(cliente1, cliente2, saldo):

    if cliente1.saldo - saldo >= 0:
        
        cliente1.saldo = cliente1.saldo - saldo
        cliente2.saldo = cliente2.saldo + saldo
        print(f"\nLa transferencia a sido exitosa, saldo restante {cliente1.saldo}")

    else:
        print("Saldo insuciciente")

def Prestamo(cliente, prestamo):

    if prestamo < cliente.saldo/2:

        cliente.saldo = cliente.saldo + prestamo
        return True
    else:
        print("El prestamo es mayor que la mitad del saldo... Pruebe con otro monto")
        return False



cliente1 =ClienteBanco("Lucas", "Massazza", 41823343, "Ahorro", 20000)
cliente2 =ClienteBanco('Pablo', 'Perez', 26345678, 'Ahorro', 20000)
clientePremium1 = ClientePremium ("Jorge", "Fernandez", 32945023, "Corriente", 100000, "Platinium")
clientePremium2 = ClientePremium ("Daniela", "Valeria", 42845726, "Ahorro", 100000000, "Black")

print(clientePremium1)
#clientePremium1 = clientePremium1(cliente1)

#cliente1.Depositar(100000)

#cliente1.Retiro(90000)

#cliente1.Retiro(30000)

#cliente1.ConsultarSaldo()

Transferencia(cliente1,cliente2,10000)

print(f"\nSaldo Lucas: {cliente1.saldo}")
print(f"\nSaldo Pablo: {cliente2.saldo}")

#print(Prestamo(cliente1,9000))
#print(cliente1.saldo)

#print(Prestamo(cliente2,11000))
#print(cliente2.saldo)

#clientePremium1.Beneficios
#rint("\n\n\n")
#clientePremium2.Beneficios


