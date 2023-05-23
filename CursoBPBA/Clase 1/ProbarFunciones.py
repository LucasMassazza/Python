def OrdenamientoLista(Lista):

    Lista = Lista
    ListaSum = []


    ## Completar con código

    Indice = 0


    for vocales in range(0, len(Lista)-1):
        
        IndGuia = Indice+1
        ListaSum.append(Lista[Indice]+Lista[IndGuia])
        Indice = Indice+1 

    ListaSum.sort()
    print(ListaSum.sort)












