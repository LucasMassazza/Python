import numpy as np
import pandas as pd



Nombre = ["nery Pumpido",
          "Jose Schiuffino",
          "Jose Schiuffino",
          "Jose Luis Brown",
          "Oscar Ruggieri"
          "Segio Batista",
          "Ricardo Giusti",
          "Jorge Burruchaga",
          "Hector Enrique",
          "Julio Olartiche",
          "Jorge Valdano",
          "Diego maradona"]

Posicion = ["ARQ",
            "DEF",
            "DEF",
            "DEF",
            "MED",
            "MED",
            "MED",
            "MED",
            "MED",
            "DEL",
            "DEL"
]

numero = [18,9,5,19,2,14,7,12,16,11,10]



Equipo = {"Nombre": Nombre,"posicion": Posicion, "Numero": numero}

#print(Equipo)

DataFrameEquipo = pd.DataFrame(Equipo)

print(DataFrameEquipo)



