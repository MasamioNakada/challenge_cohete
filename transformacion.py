from datetime import datetime
import os
import pandas as pd
from wikiframe.cow_say import Say



obj_col = { 'bibliotecas' : ['Cod_Loc','IdProvincia','IdDepartamento','Categoría','Provincia','Localidad','Nombre','Domicilio','CP','Teléfono','Mail','Web'],
            'museos' : ['Cod_Loc','IdProvincia','IdDepartamento','categoria','provincia','localidad','nombre','direccion','CP','telefono','Mail','Web'],
            'sala_de_cine' : ['Cod_Loc','IdProvincia','IdDepartamento','Categoría','Provincia','Localidad','Nombre','Dirección','CP','Teléfono','Mail','Web']}
norm_cols = ['cod_localidad','id_provincia','id_departamento','categoría','provincia','localidad','nombre','domicilio','codigo_postal','número_de_telefono','mail','web']

categories = ['bibliotecas','museos','sala_de_cine']


class transformador:
    def __init__(self,categoria:list) -> None:
        self.categoria = categoria
        self.t = datetime.now()
        self.p = datetime.now().date().strftime('%d-%m-%Y')

    def concat_df(self):
        data_dict = {}
        for cat in self.categoria:
            path = f'categoria/{cat}/{self.t.year}-{self.t.month}/{cat}-{self.p}.csv'
            data_dict[cat] = pd.read_csv(path, index_col='Unnamed: 0')       

        d_0 = pd.DataFrame()
        for key, value in obj_col.items():
            data_dict[key] = data_dict[key][value]  
            data_dict[key].columns = norm_cols

        for cat in self.categoria:
            d_0 = pd.concat([d_0,data_dict[cat]],axis=0)

        for  col in d_0.columns:
            if d_0[col].dtype == 'int64':
                d_0[col]= d_0[col].astype(float)

        os.makedirs('out',exist_ok=True)
        path = f'out/{self.p}.csv'
        d_0.to_csv(path)
        Say().cow_says_good(f'Dataframe concatenado importado en {path}')
        



