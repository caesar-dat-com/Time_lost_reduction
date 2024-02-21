"""This part controls the connection with the database on mysql with mysql connector"""
import mysql.connector

def baseconnect():
    try:
        mydb = mysql.connector.connect(
            host = "",
            user = "",
            password = "",
            database = ""
            )
        cur = mydb.cursor()
        print("Succesfull Connection")
        return cur ,mydb 
    except mysql.connector.Error as err:
        print(f"error {err}")
        return None, None



