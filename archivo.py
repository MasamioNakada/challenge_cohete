from consultas import Consultas,consulta_cine
from transformacion import transformador
from utils import url_to_dataframe, writter

import pandas as pd
from datetime import datetime
from wikiframe.cow_say import Say
from time import sleep

from sqlalchemy.orm import Session
import crud
from config import SessionLocal, engine

s = Say()

urls = {
    'museos':'https://docs.google.com/spreadsheets/d/1PS2_yAvNVEuSY0gI8Nky73TQMcx_G1i18lm--jOGfAA/edit#gid=514147473',
    'sala_de_cine':'https://docs.google.com/spreadsheets/d/1o8QeMOKWm4VeZ9VecgnL8BWaOlX5kdCDkXoAph37sQM/edit#gid=1691373423',
    'bibliotecas':'https://docs.google.com/spreadsheets/d/1udwn61l_FZsFsEuU8CMVkvU2SpwPW3Krt1OML3cYMYk/edit#gid=1605800889'
}

categories = [key for key in urls.keys()]

t = datetime.now()
p = t.date().strftime('%d-%m-%Y')



if __name__ == "__main__":
    
    #instanciamos la base de datos
    db = SessionLocal()
    
    #Extraemos los datos del URL
    #Se exporta en el directorio 'categorias'
    for key, value in urls.items():
        df = url_to_dataframe(value)
        writter(df,key)

    #Transformamos y cancatenamos los dataframes
    t = transformador(categoria= categories)
    t.concat_df()  

    #cargamos la data concatenada
    full_data = pd.read_csv(f'./out/{p}.csv',index_col='Unnamed: 0')

    #instanciamos la clase consulta
    c = Consultas(full_data)

    #Cantidad de registros totales por categoría y lo exportamos en la carpeta consulta
    c.r_categoria().to_csv(f'./consulta/categoria-{p}.csv')
    s.cow_says_good(f'consulta exportada exitosamente en ./consulta/categoria-{p}.csv')
    sleep(1)
    #Cantidad de registros por provincia y categoría
    c.r_prov_cat().to_csv(f'./consulta/prov-categ-{p}.csv')
    s.cow_says_good(f'consulta exportada exitosamente en ./consulta/prov-categ-{p}.csv')
    sleep(1)
    #Procesamiento de la informacion de cine
    consulta_cine().to_csv(f'./consulta/cine-{p}.csv')
    s.cow_says_good(f'consulta exportada exitosamente en ./consulta/cine-{p}.csv')
    sleep(1)
    for i in range(full_data.shape[0]):
        crud.create_row(db = db , element=list(full_data.iloc[i])) 
        print(f'elemento {i} agregado')

    
