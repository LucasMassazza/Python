def Ejercicio1(n1,n2):

    producto=n1*n2
    

    if producto>100:
        print(f"El producto de {n1} y {n2} es: {producto}")
    else:
        suma=n1+n2
        print(f"El producto de {n1} y {n2} es: {producto}\nLa suma es {suma}")
    
def Ejercicio2(Lista):

    ListaSum = []
    Indice = 0


    for vocales in range(0, len(Lista)-1):
        
        IndGuia = Indice+1
        ListaSum.append(Lista[Indice]+Lista[IndGuia])
        Indice = Indice+1 

    ListaSum.sort()
    print(ListaSum.sort)

def Ejercicio3(oracion):
    vocales = ['a','e','i','o','u']
    VocalesMay =[]
    for char in oracion:
        if char in vocales:
            VocalesMay.append(char.upper())

def Ejercicio4(numeros, divisor):

    multiplos = [multiplo for multiplo in numeros if multiplo % divisor == 0]
    multiplosFiltrador = []

    for x in range(len(multiplos)):
        if multiplos[x] not in multiplosFiltrador:
            multiplosFiltrador.append(multiplos[x])

    multiplosFiltrador.sort()
    multiplosFiltrador

def Ejercicio5(lista):
    contador = 0
    for indice in lista:
        if isinstance(indice,(int, str)):
            if isinstance(indice, str) and indice.islower():
                contador = contador + 1
            if isinstance(indice, int) and isinstance(indice, float) == bool():
                contador = contador + 1

    contador


