from sqlalchemy import Column, Integer, String
from config import Base

#Crear un ORM para futura insercion de datos
class Tabla(Base):
    __tablename__ = "table"
    id  = Column(Integer, primary_key=True, index=True)
    cod_localidad = Column(Integer)
    id_provincia = Column(Integer)
    id_departamento = Column(Integer)
    categoria = Column(String)
    provincia = Column(String)
    localidad = Column(String)
    nombre = Column(String)
    domicilio = Column(String)
    codigo_postal = Column(String)
    número_de_telefono = Column(String)
    mail = Column(String)
    web = Column(String)

