import pandas as pd
from decouple import config 
import postgres_connect

df1 = pd.read_csv(r"actividades_no_programadas_clean_2.csv") #Load the csv_file with pandas
df1.to_sql(f"{config("DB_TABLE2")}", con=postgres_connect.connection(), if_exists="replace",index=False) #Load the data into a postgres table at format sql

df2 = pd.read_csv(r"actividades_programadas_clean_.csv") #Load the csv_file with pandas
df2.to_sql(f"{config("DB_TABLE1")}", con=postgres_connect.connection(), if_exists="replace",index=False) #Load the data into a postgres table at format sql

df3 = pd.read_csv(r"inspecciones_no_programadas_clean_.csv") #Load the csv_file with pandas
df3.to_sql(f"{config("DB_TABLE4")}", con=postgres_connect.connection(), if_exists="replace",index=False) #Load the data into a postgres table at format sql

df4 = pd.read_csv(r"inspecciones_programadas_clean_.csv") #Load the csv_file with pandas
df4.to_sql(f"{config("DB_TABLE3")}", con=postgres_connect.connection(), if_exists="replace",index=False) #Load the data into a postgres table at format sql
