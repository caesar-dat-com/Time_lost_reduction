"""This part controls the connection with the database on mysql with mysql connector"""
from decouple import config
from datetime import datetime
from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String, DateTime, Float
from sqlalchemy.orm import sessionmaker, declarative_base

engine = create_engine(f"postgresql://{config("DB_USER")}:{config("DB_PASSWORD")}@{config("DB_HOST")}/{config("DB_DATABASE")}")
base = declarative_base()

class act_programados(base):
    __tablename__ = config("DB_TABLE1")
    id = Column(Integer(), primary_key=True)
    Codigo_centro = Column(String(30))
    Centro = Column(String(70))
    Ubicacion_tecnica = Column(String(200))
    Denominacion_Ubicacion = Column(String(200))
    Equipo = Column(String(30))
    Denominacion = Column(String(200))
    No_Plan = Column(String(40))
    Desc_Plan = Column(String(300))
    Orden =  Column(String(60))
    Actividad = Column(String(90))
    Clase_de_orden = Column(String(100))
    Status_sistema = Column(String(50))
    Inicio_programa = Column(DateTime())
    Duracion = Column(Float())

    def __str__(self):

        self.username
class act_no_programados(base):
    __tablename__ = config("DB_TABLE2")
    id = Column(Integer(), primary_key=True)
    Codigo_centro = Column(String(30))
    Centro = Column(String(70))
    Ubicacion_tecnica = Column(String(200))
    Denominacion_Ubicacion = Column(String(200))
    Equipo = Column(String(30))
    Denominacion = Column(String(200))
    No_Plan = Column(String(40))
    Desc_Plan = Column(String(300))
    Orden =  Column(String(60))
    Actividad = Column(String(90))
    Clase_de_orden = Column(String(100))
    Status_sistema = Column(String(50))
    Inicio_programa = Column(DateTime())
    Duracion = Column(Float())

    def __str__(self):
        self.username
class ins_no_programados(base):
    __tablename__ = config("DB_TABLE3")
    id = Column(Integer(), primary_key=True)
    Codigo_centro = Column(String())
    Centro = Column(String(70))
    Ubicacion_tecnica = Column(String(200))
    Denominacion_Ubicacion = Column(String(200))
    Equipo = Column(String())
    Denominacion = Column(String(200))
    No_Plan = Column(String(40))
    Desc_Plan = Column(String(300))
    Orden =  Column(String(60))
    Actividad = Column(String(90))
    Descripcion = Column(String(400))
    Clase_de_orden = Column(String(100))
    Status_sistema = Column(String(50))
    Inicio_programa = Column(DateTime())
    Duracion = Column(Float())

    def __str__(self):
        self.username

class ins_programados(base):
    __tablename__ = config("DB_TABLE4")
    id = Column(Integer(), primary_key=True)
    Codigo_centro = Column(String(30))
    Centro = Column(String(70))
    Ubicacion_tecnica = Column(String(200))
    Denominacion_Ubicacion = Column(String(200))
    Equipo = Column(String(30))
    Denominacion = Column(String(200))
    No_Plan = Column(String(40))
    Desc_Plan = Column(String(300))
    Orden =  Column(String(60))
    Actividad = Column(String(90))
    Descripcion = Column(String(400))
    Clase_de_orden = Column(String(100))
    Status_sistema = Column(String(50))
    Inicio_programa = Column(DateTime())
    Duracion = Column(Float())

    def __str(self):
        self.username
    
#class ins_programados(base):
#    __tablename__ = config("DB_TABLE5")
#   
#    def __str__(self):
#        self.username
#the data is not there yet

Session = sessionmaker(engine)
session = Session()

def connection(engine=engine):
    return engine

if __name__ == "__main__":
    base.metadata.drop_all(engine)
    base.metadata.create_all(engine)
