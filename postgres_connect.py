from decouple import config
from datetime import datetime
from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String, DateTime, Float
from sqlalchemy.orm import sessionmaker, declarative_base

engine = create_engine(f"postgresql://{config("DB_USER")}:{config("DB_PASSWORD")}@{config("DB_HOST")}/{config("DB_DATABASE")}")
base = declarative_base()

class act_programadas(base):
    __tablename__ = config("DB_TABLE1")
    id = Column(Integer(), primary_key=True)
    Codigo_centro = Column(Integer())
    Centro = Column(String(70))
    Ubicaion_tecnica = Column(String(70))
    Denominacion_ubicacion = Column(String(100))
    Equipo = Column(Integer())
    Denominacion = Column(String(200))
    NoPlan = Column(Integer())
    DescPlan = Column(String(400))
    Orden = Column(Integer())
    Actividad = Column(String(200))
    Clase_de_orden = Column(String(20))
    Status_sistema = Column(String(20))
    Inicio_program = Column(DateTime())
    Responsable = Column(String(30))
    Prioridad = Column(String(20))
    empty = Column(String(20))
    Duracion = Column(Float())
    def __str__(self):
        return self.username

class act_no_programadas(base):
    __tablename__= config("DB_TABLE2")
    id = Column(Integer(), primary_key=True)
    Codigo_centro = Column(Integer())
    Centro = Column(String(70))
    Ubicaion_tecnica = Column(String(70))
    Denominacion_ubicacion = Column(String(100))
    Equipo = Column(Integer())
    Denominacion = Column(String(200))
    NoPlan = Column(Integer())
    DescPlan = Column(String(400))
    Orden = Column(Integer())
    Actividad = Column(String(200))
    Clase_de_orden = Column(String(20))
    Status_sistema = Column(String(20))
    Inicio_program = Column(DateTime())
    Responsable = Column(String(30))
    Prioridad = Column(String(20))
    empty = Column(String(20))
    Duracion = Column(Float())
    def __str__(self):
        return self.username
        
class ins_programadas(base):
    __tablename__= config("DB_TABLE3")
    id = Column(Integer(), primary_key=True)
    Codigo_centro = Column(Integer())
    Centro = Column(String(70))
    Ubicaion_tecnica = Column(String(70))
    Denominacion_ubicacion = Column(String(100))
    Equipo = Column(Integer())
    Denominacion = Column(String(200))
    NoPlan = Column(Integer())
    DescPlan = Column(String(400))
    Orden = Column(Integer())
    Actividad = Column(String(200))
    Clase_de_orden = Column(String(20))
    Status_sistema = Column(String(20))
    Inicio_program = Column(DateTime())
    Responsable = Column(String(30))
    Prioridad = Column(String(20))
    empty = Column(String(20))
    Duracion = Column(Float())
    def __str__(self):
        return self.username

class ins_no_programadas(base):
    __tablename__= config("DB_TABLE4")
    id = Column(Integer(), primary_key=True)
    Codigo_centro = Column(Integer())
    Centro = Column(String(70))
    Ubicaion_tecnica = Column(String(70))
    Denominacion_ubicacion = Column(String(100))
    Equipo = Column(Integer())
    Denominacion = Column(String(200))
    NoPlan = Column(Integer())
    DescPlan = Column(String(400))
    Orden = Column(Integer())
    Actividad = Column(String(200))
    Clase_de_orden = Column(String(20))
    Status_sistema = Column(String(20))
    Inicio_program = Column(DateTime())
    Responsable = Column(String(30))
    Prioridad = Column(String(20))
    empty = Column(String(20))
    Duracion = Column(Float())
    def __str__(self):
        return self.username



Session = sessionmaker(engine)
session = Session()

def connection(engine=engine):
    return engine


if __name__ == "__main__":
    base.metadata.drop_all(engine)
    base.metadata.create_all(engine)