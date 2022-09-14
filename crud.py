from sqlalchemy.orm import Session
from model import Tabla
from pandas.core.frame import DataFrame

def create_row(db:Session, element:list):
    _row = Tabla(
        cod_localidad = element[0],
        id_provincia = element[1],
        id_departamento = element[2],
        categoria = element[3],
        provincia = element[4],
        localidad = element[5],
        nombre = element[6],
        domicilio = element[7],
        codigo_postal = element[8],
        número_de_telefono = element[9],
        mail = element[10],
        web = element[11]
    )
    db.add(_row)
    db.commit()
    db.refresh(_row)
    return _row