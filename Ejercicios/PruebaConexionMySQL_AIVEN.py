# Importamos las librerias necesarias
# pip install pymysql, python-dotenv, cryptography
import pymysql
import cryptography
import os
from dotenv import load_dotenv

load_dotenv()

# Conexion con la base de datos
try:    
    timeout = 10
    conexion = pymysql.connect(
        host="mysql-pruebas-sergiorodriguezprofesional-8ed7.h.aivencloud.com",
        port=13648,
        user="avnadmin",
        password=os.getenv("DB_PASSWORD"),
        db="defaultdb",
        connect_timeout=timeout
    )

    print("Conexión establecida correctamente. ")
    '''cursor = connection.cursor()
    cursor.execute("CREATE TABLE mytest (id INTEGER PRIMARY KEY)")
    cursor.execute("INSERT INTO mytest (id) VALUES (1), (2)")
    cursor.execute("SELECT * FROM mytest")
    print(cursor.fetchall())'''
except Exception as e:
    print(f"Error al conectar a la base de datos: {e}")
