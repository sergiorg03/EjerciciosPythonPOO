# Importamos las librerias necesarias
import sqlite3

'''
    Una clave externa es una clave primaria en otra clase, que sirve para relacionar ambas tablas.

    MySQL no permite realizar el FULL JOIN, sin embargo si permite el INNER JOIN, LEFT JOIN y RIGHT JOIN.
    SQLite no soporta el RIGHT JOIN ni el FULL JOIN.
'''

# Conexion con la base de datos
__NOMBRE_DB = 'nombreDB.db'

try:    
    conexion = sqlite3.connect(__NOMBRE_DB)
except Exception as e:
    print(f"Error al conectar a la base de datos: {e}")
finally:
    if conexion:
        conexion.close()

'''
    Ejecutar sentencias SQL
'''
cursor = conexion.cursor()
cursor.execute("SENTENCIA SQL")

'''
    INICIAR, GUARDAR Y VOLVER TRANSACCIONES
'''
conexion.execute("BEGIN TRANSACTION")
conexion.execute("COMMIT")
conexion.execute("ROLLBACK")


'''
    CONSULTAS PARAMETRIZADAS (Evitar SQL Injection)
    
    Cuando pasamos parámetros a una consulta SQL, debemos hacerlo mediante una tupla.
    
    IMPORTANTE: Si la tupla tiene UN SOLO elemento, es OBLIGATORIO poner una coma al final.
    Python distingue entre (25) -> entero 25, y (25,) -> tupla con el elemento 25.
'''
# Correcto:
# cursor.execute('SELECT nombre FROM usuarios WHERE edad > ?', (25,))

# Incorrecto (dará error porque (25) es un int, no una secuencia):
# cursor.execute('SELECT nombre FROM usuarios WHERE edad > ?', (25))




