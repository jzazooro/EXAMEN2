import pandas as pd

pesos = pd.read_csv("dataset.csv")


class Media:
    def __init__(self, csv, columna):
        self.csv = csv
        self.columna = columna

    def calculo(self):
        media = self.csv[self.columna].mean()
        print("La media es:")
        print(media)