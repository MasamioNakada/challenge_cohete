from requests import get
from io import BytesIO
import pandas as pd
from pandas.core.frame import DataFrame
import os
from wikiframe.cow_say import Say
from datetime import datetime

def url_to_dataframe(url:str) -> pd.core.frame.DataFrame:
    """
    This function takes a url and returns a pandas dataframe

    Parameters
    ----------
    url : str -> url of the google sheet

    Returns
    -------
    df : pd.core.frame.DataFrame -> pandas dataframe
    """
    d_url = url.replace("/edit#", "/export?")+"&format=csv"
    data = get(d_url).content
    return pd.read_csv(BytesIO(data))


def writter(dataframe: DataFrame, category:str):
    st = datetime.now()
    p = st.date().strftime('%d-%m-%Y')
    path = f'categoria/{category}/{st.year}-{st.month}/{category}-{p}.csv'
    os.makedirs(f'categoria/{category}/{st.year}-{st.month}' ,exist_ok=True)
    dataframe.to_csv(path)
    return Say().cow_says_good(f"reporte escrito exitosamente en {path}")