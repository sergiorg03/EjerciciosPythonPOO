# importamos las librerias necesarias
import sqlite3
import sqlite3
from datetime import datetime

con = None

# Sentencias CREACIÓN Y BORRADO DE
__NOMBRE_DB = "empresa.db"
__DROP_EMPLEADOS = "DROP TABLE IF EXISTS empleados"
__DROP_OFICINAS = "DROP TABLE IF EXISTS oficinas"
__SENTENCIA_EMPLEADOS = f"""CREATE TABLE IF NOT EXISTS empleados (
                                id_emp INTEGER PRIMARY KEY AUTOINCREMENT,
                                nombre TEXT,
                                fecha_nacimiento DATE,
                                oficina INTEGER,
                                puesto TEXT,
                                contrato DATE,
                                FOREIGN KEY(oficina) REFERENCES oficinas(id_ofi) 
                                )"""

__SENTENCIA_OFICINAS = """CREATE TABLE IF NOT EXISTS oficinas(
                                id_ofi INTEGER PRIMARY KEY AUTOINCREMENT,
                                domicilio TEXT,
                                ciudad TEXT,
                                superficie REAL                                
                                )"""

ruta_archivo = "datos_prueba_DBEmpresa.txt"

# 1. Programa que lee los datos.
def leer_datos(ruta):
    empleados = []
    oficinas = []

    # Apertura del fichero
    with open(ruta, "r", encoding="utf-8") as f:
        lineas = [l.strip() for l in f.readlines()]

    # Elimina las líneas vacias
    lineas = [l for l in lineas if l != ""]

    # Comienzo del bloque de oficinas:
    indices_unos = [i for i, l in enumerate(lineas) if l.startswith("1;")]

    if len(indices_unos) < 2:
        raise ValueError("No se encontró la separación entre empleados y oficinas")

    indice_corte = indices_unos[1]

    empleados_lineas = lineas[:indice_corte]
    oficinas_lineas = lineas[indice_corte:]

    for linea in empleados_lineas:
        partes = linea.split(";")
        emp = {
            "id": int(partes[0]),
            "nombre": partes[1],
            "fecha_nacimiento": partes[2],
            "oficina": int(partes[3]),
            "puesto": partes[4],
            "contrato": partes[5]
        }
        empleados.append(emp)

    for linea in oficinas_lineas:
        partes = linea.split(";")
        ofi = {
            "id": int(partes[0]),
            "domicilio": partes[1],
            "ciudad":partes[2],
            "superficie": float(partes[3])
        }
        oficinas.append(ofi)

    return empleados, oficinas

def insert_test_data(cursor: sqlite3.Cursor):
    insert_empleados ="""INSERT INTO empleados(id_emp, nombre, fecha_nacimiento, oficina, puesto, contrato) VALUES(?,?,?,?,?,?)"""

    insert_oficinas = """INSERT INTO oficinas(id_ofi, domicilio, ciudad, superficie) VALUES(?,?,?,?)"""

    empleados, oficinas = leer_datos(ruta_archivo)
    
    try:
        oficinas = [(o['id'], o['domicilio'],o['ciudad'], o['superficie']) for o in oficinas]
        empleados = [(e['id'], e['nombre'], e['fecha_nacimiento'], e['oficina'], e['puesto'], e['contrato']) for e in empleados]
        cursor.executemany(insert_oficinas, oficinas)
        cursor.executemany(insert_empleados, empleados)
    except Exception as e:
        print(f"Error en la insercion de datos: {e}")

def opendb():
    try:
        con = sqlite3.connect(__NOMBRE_DB)
        cursor = con.cursor()
        cursor.execute(__SENTENCIA_OFICINAS)
        cursor.execute(__SENTENCIA_EMPLEADOS)
        print(f"Tablas creadas correctamente. ")
        
        insert_test_data(cursor)
        con.commit()

        return con
        
    except Exception as e:
        print(f"Error: {e}")

def closedb(con):

    try:
        
        cursor = con.cursor()
        cursor.execute(__DROP_EMPLEADOS)
        cursor.execute(__DROP_OFICINAS)
        con.commit()
        cursor.close()

        if isinstance(con, sqlite3.Connection) and con:
            con.close()
            print("Conexión con la base de datos cerrada correctamente. ")

    except Exception as e:
        print(f"Error: {e}")


if __name__ == '__main__':

    try:
        con = opendb()
        cursor = con.cursor()

        print("-"*20,"Mostramos los empleados","-"*20)
        print()
        # Mostramos todos los empleados
        cursor.execute("SELECT * FROM empleados")
        empleados = cursor.fetchall()
        print(empleados)


        print("\n"*2)
        print("-"*20,"Mostramos las oficinas de una determinada ciudad","-"*20)
        print()
        # Mostramos las oficinas de una determinada ciudad
        cursor.execute("SELECT * FROM oficinas WHERE UPPER(ciudad) = 'SEVILLA'")
        oficinas = cursor.fetchall()
        print(oficinas)


        print("\n"*2)
        print("-"*20,"Mostramos el nombre y la edad de empleados cuya edad está en un rango ","-"*20)
        print()
        # Nombre y edad de los empleados cuya edad se encuentra en un rango
        cursor.execute("""SELECT nombre, (strftime('%Y', 'now') - strftime('%Y', fecha_nacimiento)) AS edad
	                        FROM empleados
	                        WHERE edad BETWEEN ?  AND ?
                            ORDER BY edad ASC""", (30, 38))
        print(cursor.fetchall())


        print("\n"*2)
        print("-"*20,"Alta de un nuevo empleado","-"*20)
        print()
        # Alta de un nuevo empleado
        name = input("Inrtoduce el nombre del nuevo empleado: \n")
        fecha_nacimiento = datetime.strptime(input("Introduce la fecha de nacimiento del nuevo empleado en formato dd-mm-yyyy: \n"), '%d-%m-%Y')
        oficina = int(input("Introduce el id de la oficina del nuevo empleado: \n"))
        puesto = input("Introduce el puesto del nuevo empleado: \n")
        contrato = datetime.strptime(input("Introduce la fecha de contrato del nuevo empleado en formato dd-mm-yyyy: \n"), '%d-%m-%Y')
        try:
            cursor.execute("INSERT INTO empleados (nombre, fecha_nacimiento, oficina, puesto, contrato) VALUES (?, ?, ?, ?, ?)", (name, fecha_nacimiento.strftime('%Y-%m-%d'), oficina, puesto, contrato.strftime('%Y-%m-%d')))
            con.commit()
            print("Empleado insertado correctamente. ")
        except Exception as e:
            print(f"Se produjo un error a la hora de insertar al nuevo empleado. ")


        print("\n"*2)
        print("-"*20,"Alta de una nueva oficina","-"*20)
        print()
        # Alta de una nueva oficina
        domicilio = input("Introduzca la calle de la nueva oficina: \n")
        ciudad = input("Introduzca la ciudad de la nueva oficina: \n")
        superficie = float(input("Introduzca el total de superficie en metros cuadrados de la nueva oficina: \n"))
        try:
            cursor.execute("INSERT INTO oficinas (domicilio, ciudad, superficie) VALUES (?, ?, ?)", (domicilio, ciudad, superficie))
            con.commit()
            print("Oficina insertada correctamente. ")
        except Exception as e:
            print(f"Se produjo un error a la hora de insertar la nueva oficina. ")

        cursor.execute("SELECT id_ofi FROM oficinas WHERE UPPER(domicilio) = ? AND UPPER(ciudad) = ? AND superficie = ?", (domicilio.upper(), ciudad.upper(), superficie))
        print(f"ID de la última oficina añadida: {cursor.fetchall()}")


        print("\n"*2)
        print("-"*20,"Cambio de oficina de los empleados","-"*20)
        print()
        # Cambio de oficina de los empleados
        of_a_modif = input("Introduzca la oficina de la que quiere modificar a los empleados: \n")
        nueva_of = input("Introduzca el ID de la nueva oficina a asignar los empleados: \n")

        sentencia = """UPDATE empleados 
                        SET oficina = ?
                            WHERE oficina = ?"""
        cursor.execute(sentencia, (nueva_of, of_a_modif))
        con.commit()
        cursor.execute("SELECT * FROM empleados WHERE oficina = ?", (nueva_of,))
        print(cursor.fetchall())


        print("\n"*2)
        print("-"*20,"Empleados de la oficina con mayor superficie","-"*20)
        print()
        # Empleados de la oficina con mayor superficie
        cursor.execute("SELECT id_emp, Nombre, puesto FROM empleados WHERE oficina = (SELECT id_ofi FROM oficinas ORDER BY superficie DESC LIMIT 1)")
        print(cursor.fetchall())


        print("\n"*2)
        print("-"*20,"Borrado de un empleado","-"*20)
        print()
        # Eliminado de un empleado
        id_emp = input("Introduzca el ID del empleado a eliminar: \n")
        cursor.execute("DELETE FROM empleados WHERE id_emp = ?", (id_emp,))
        con.commit()
        cursor.execute("SELECT COUNT(*) FROM empleados WHERE id_emp = ?", (id_emp,))
        print(cursor.fetchall())


        print("\n"*2)
        print("-"*20,"Oficinas con extensión superior a la introducida","-"*20)
        print()
        # Oficinas con extensión superior a la introducida
        print("Extensión de las oficinas en orden descendente. ")
        print(cursor.execute("SELECT id_ofi AS id, superficie FROM oficinas ORDER BY superficie DESC").fetchall())
        print()
        ext = input("Introduzca la extension mínima de la oficina: \n")
        print("Oficinas con extensión superior a la introducida. ")
        cursor.execute("SELECT id_ofi, ciudad, superficie FROM oficinas WHERE superficie > ? ORDER BY superficie DESC", (ext,))
        print(cursor.fetchall())

        print("\n"*2)
        print("-"*20,"Modificación de una oficina indicada","-"*20)
        print()
        # Modificación de una oficina indicada
        ofi = input("Introduzca el ID de la oficina a modificar: \n")
        nuevo_dom = input("Introduzca el nuevo domicilio de la oficina: \n")
        print(f"Antes de la modificación: {cursor.execute("SELECT * FROM oficinas WHERE id_ofi = ?", (ofi,)).fetchall()}")
        cursor.execute("UPDATE oficinas SET domicilio = ? WHERE id_ofi = ?", (nuevo_dom, ofi,))
        con.commit()

        print(f"Despues de la modificación: {cursor.execute("SELECT * FROM oficinas WHERE id_ofi = ?", (ofi,)).fetchall()}")

    except Exception as e:
        print(f"Error: {e}")
    finally:
        closedb(con)


