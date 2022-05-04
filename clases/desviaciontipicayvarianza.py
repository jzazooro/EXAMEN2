import pandas as pd

pesos = pd.read_csv("dataset.csv")


class Desviacion_tipica:
    def __init__(self, csv, columna):
        self.csv = csv
        self.columna = columna

    def calculo(self):
        desv = self.csv[self.columna].mad()
        print("La desviación tipica es:")
        print(desv)

class Varianza:
    def __init__(self, csv, columna):
        self.csv = csv
        self.columna = columna

    def calculo(self):
        var = self.csv[self.columna].var()
        print("La varianza es:")
        print(var)