import pandas as pd
from pandas.core.frame import DataFrame
from datetime import datetime

class Consultas:
    """
     Procesar los datos conjuntos para poder generar una tabla con la siguiente
    información:
        o Cantidad de registros totales por categoría
        o Cantidad de registros totales por fuente
        o Cantidad de registros por provincia y categoría
    """
    def __init__(self,df) -> None:
        self.df : DataFrame = df
        df['conteo'] = df.index

    def r_categoria(self):
        """
        Cantidad de registros totales por categoría

        """
        return self.df.pivot_table(index='categoría',values='conteo',aggfunc='count')

    def r_prov_cat(self):
        """
         Cantidad de registros por provincia y categoría

        """
        return self.df.pivot_table(index=['provincia','categoría'],values='conteo',aggfunc='count')


def consulta_cine():
    """
    Procesar la información de cines para poder crear una tabla que contenga:
        o Provincia
        o Cantidad de pantallas
        o Cantidad de butacas
        o Cantidad de espacios INCAA
    """
    t = datetime.now()
    p = t.date().strftime('%d-%m-%Y')
    path = f'categoria/sala_de_cine/{t.year}-{t.month}/sala_de_cine-{p}.csv'
    df_cine = pd.read_csv(path,index_col='Unnamed: 0')

    return df_cine.pivot_table(index='Provincia', values=['Pantallas','Butacas','espacio_INCAA'],aggfunc='count')





    