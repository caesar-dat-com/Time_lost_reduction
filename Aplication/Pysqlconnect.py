"""This part controls the connection with the database on mysql with mysql connector"""
import mysql.connector
from decouple import config as dbconfig

def baseconnect():
    try:
        mydb = mysql.connector.connect(
            host = dbconfig("MYSQL_HOST"),
            user = dbconfig("MYSQL_USER"),
            password = dbconfig("MYSQL_PASSWORD"),
            database = dbconfig("MYSQL_DB")
            )
        cur = mydb.cursor()
        print("Succesfull Connection")
        return cur ,mydb 
    except mysql.connector.Error as err:
        print(f"error {err}")
        return None, None




