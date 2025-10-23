'''
Implementa una aplicación que gestione un club donde identifica a los socios por un apodo personal y único.
De cada socio, además del apodo, se guarda el nombre y su fecha de ingreso en el club.
Utiliza un diccionario donde las claves serán los apodos y los valores son objetos de la clase socio.
Las operaciones se mostrarán en un menú que tendrá las siguientes opciones:
1. Alta socio.
2. Baja socio.
3. Modificación socio.
4. Listar socios por apodo.
5. Listar socios por antigüedad.
6. Listar los socios con alta anterior a un año determinado
7. Salir
'''

#Importamos las librerias necesarias
from datetime import datetime, date

class Persona:

    nombre: str
    fechaIngreso: datetime

    def __init__(self, nombre: str, fechaIngreso:datetime):
        self.nombre = nombre
        self.fechaIngreso = fechaIngreso

    def getNombre(self):
        return self.nombre

    def getFechaIngreso(self):
        return self.fechaIngreso

    def setNombre(self, nombre:str):
        self.nombre = nombre

    def setFechaIngreso(self, fechaIngreso:datetime):
        self.fechaIngreso = fechaIngreso

    def toString(self):
        return f"Nombre: {self.getNombre()}, fecha de ingreso: {self.getFechaIngreso()}"

# socios = {"apodo" : Persona, "apodo2" : Persona2.....}
socios = {
    "La pulga" : Persona("Messi", datetime.now()),
    "El Bicho" : Persona("CR7", datetime.now()),
    "El Pepe" : Persona("Shrek", datetime.now())
}

opcion = -1

def altaSocio(apodo: str , nombre: str):
    socios[apodo] = Persona(nombre, datetime.now())
    print(f"El nuevo socio \"{apodo}\"{socios[apodo].toString()}")


def bajaSocio(apodo: str):
    socios.pop(apodo)
    print(f"El socio con el apodo: {apodo} ha sido borrado correctamente. ")


def listadoSocios():
    return "\n".join(x+", "+socios[x].toString() for x in socios)


def listadoSociosAntiguedad():
    pass


def modificarSocio(apodo):
    j = socios[apodo]
    opcion = -1
    while opcion != 0:
        opcion = int(input("¿Qué desea modificar del socio? \n1 --> Nombre. \n2 --> Fecha de ingreso. \n 0 --> Salir. "))
        if opcion == 1:
            j.setNombre(input("Ingrese el nuevo nombre: "))
        elif opcion == 2:
            j.setFechaIngreso(date(input("Ingrese la fecha de ingreso en formato yyyy-mm-dd: ")))
        elif opcion == 0:
            print("Saliendo...")
        else:
            print("Opcion no valida")
    print(f"Socio modificado {socios[apodo].toString()} correctamente. ")


while opcion != 7:
    opcion = int(input("Elige una de las siguientes opciones: \n1. Alta socio. \n2. Baja socio. \n3. Modificación socio. \n4. Listar socios por apodo. \n5. Listar socios por antigüedad. \n6. Listar los socios con alta anterior a un año determinado. \n7. Salir"))
    if opcion == 1:
        apodo = input("Introduce el apodo del nuevo socio: ")
        nombre = input("Introduce el nombre del nuevo socio: ")
        altaSocio(apodo, nombre)
    elif opcion == 2:
        apodo = input("Introduce el apodo del socio a dar de baja: ")
        bajaSocio(apodo)
    elif opcion == 3:
        apodo = input("Introduce el apodo del socio a modificar: ")
        modificarSocio(apodo)
    elif opcion == 4:
        print(f"Listado de socios: \n{listadoSocios()}")
    elif opcion == 5:
        print(f"Listado de socios: \n{listadoSociosAntiguedad()}")
    elif opcion == 6:
        pass
    elif opcion == 7:
        print("Saliendo...")
    else:
        print("Opcion no valida")
