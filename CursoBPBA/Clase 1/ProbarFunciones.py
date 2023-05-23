def OrdenamientoLista(Lista):

    ListaSum = []
    Indice = 0


    for vocales in range(0, len(Lista)-1):
        
        IndGuia = Indice+1
        ListaSum.append(Lista[Indice]+Lista[IndGuia])
        Indice = Indice+1 

    ListaSum.sort()
    print(ListaSum.sort)

oracion = {"Hola como estas"}



def VocalesOracion(oracion):

    lista = []
    lista = oracion.split()
    print(oracion)


