# Importamos las librerias necesarias
import mysql.connector
from .env import * as v

# Conexion con la base de datos
try:    
    conexion = mysql.connector.connect(
        host="localhost",
        user="root",
        password=v.DB_PASSWORD,
        database="defaultdb"
    )
except Exception as e:
    print(f"Error al conectar a la base de datos: {e}")
finally:
    if conexion:
        conexion.close()