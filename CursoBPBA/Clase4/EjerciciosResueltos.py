import pandas as pd
import numpy as np

def Ejercicio2():

    arr2 = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])

    arr2[arr2%2 == 0] = -1
        
    print(arr2)

def Ejercicio3():

    x = np.array([1,2,3,4,5])
    y = np.array([5,6,7,8,9])

    z = x-y
    print(z)

def Ejercicio4():

    Lista = np.arange(100).reshape(4,-1)
    print(Lista)

def Ejercicio4(Lista):
    
    
    # if Lista[Lista>10 & Lista%3 == 0]:

  
    return Lista[(Lista > 10) & (Lista%3 ==0)]
    
    #MultiploYMayor
        


#Ejercicio2()
#Ejercicio3()

a = np.arange(1000).reshape(10,-1)
print(Ejercicio4(a))