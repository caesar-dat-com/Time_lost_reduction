"""This part controls the connection with the database on mysql with mysql connector"""
from decouple import config
from datime import datetime
from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String, DateTime, Float
from sqlalchemy.orm import sessionmaker, declarative_base

engine = create_engine(f"postgresql://{config("DB_USER")}:{config("DB_PASSWORD")}@{config("DB_HOST")}/{config("DB_DATABASE")}")
base = declarative_base()

class act_programados(base):
    __tablename__ = config("DB_TABLE1")
    def __str__(self):
        self.username
class act_no_programados(base):
    __tablename__ = config("DB_TABLE2")
    def __str__(self):
        self.username
class ins_no_programados(base):
    __tablename__ = config("DB_TABLE3")
    def __str__(self):
        self.username

class ins_programados(base):
    __tablename__ = config("DB_TABLE4")
    def __str(self):
        self.username
    
class ins_programados(base):
    __tablename__ = config("DB_TABLE5")
    
    def __str__(self):
        self.username


Session = sessionmaker(engine)
session = Session()

def connection(engine=engine):
    return engine

    
