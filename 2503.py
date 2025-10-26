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
    "La pulga" : Persona("Messi", datetime(2021, 6, 10)),
    "El Bicho" : Persona("CR7", datetime(2020, 5, 12)),
    "El Pepe"  : Persona("Shrek", datetime(2024, 3, 8)),
    "El niño maravilla": Persona("Kike Montisha", datetime.now()),
}

opcion = -1

def altaSocio(apodo: str , nombre: str):
    socios[apodo] = Persona(nombre, datetime.now())
    print(f"El nuevo socio \"{apodo}\"{socios[apodo].toString()}")


def bajaSocio(apodo: str):
    socios.pop(apodo)
    print(f"El socio con el apodo: {apodo} ha sido borrado correctamente. ")


def listadoSocios():

    return "\n".join(x+", "+socios[x].toString() for x in sorted(socios))


def listadoSociosAntiguedad():

    sociosOrdenadosPorAntiguedad = sorted(socios.items(), key=lambda item: item[1].fechaIngreso )
    #print(sociosOrdenadosPorAntiguedad)

    return [apodo+", "+ persona.toString() for apodo, persona in sociosOrdenadosPorAntiguedad]


def modificarSocio(apodo):
    j = socios[apodo]
    opcion = -1
    while opcion != 0:
        opcion = int(input("¿Qué desea modificar del socio? \n1 --> Nombre. \n2 --> Fecha de ingreso. \n0 --> Salir. "))
        if opcion == 1:
            j.setNombre(input("Ingrese el nuevo nombre: "))
        elif opcion == 2:
            j.setFechaIngreso(datetime.strptime(input("Ingrese la fecha de ingreso en formato yyyy-mm-dd: "), '%Y-%m-%d'))
        elif opcion == 0:
            print("Saliendo...")
        else:
            print("Opcion no valida")
    print(f"Socio modificado: {socios[apodo].toString()} correctamente. ")


def listadoSociosAno():
    anno = datetime.strptime(input("Ingrese la fecha a partir de la que desea mostrar los socios: "), "%Y")
    sociosordenados = sorted(socios.items(), key=lambda item: item[1].fechaIngreso)

    sociosFiltrados = [f"Apodo: {apodo}, {persona.toString()}" for apodo, persona in sociosordenados if persona.getFechaIngreso() > anno]

    #return f"Listado de socios a partir del año {anno}: {(apodo+', '+ persona.toString() for apodo, persona in listadoSociosAntiguedad() if persona.getFechaIngreso() > anno )}"
    return f"Listados de socios a partir del año: {anno.year}.\n" + "\n".join(sociosFiltrados)+"\n" if sociosFiltrados else f"No hay socios dados de alta a partir del año: {anno.year}.\n"


while opcion != 7:
    opcion = int(input("Elige una de las siguientes opciones: "
                       "\n1. Alta socio. "
                       "\n2. Baja socio. "
                       "\n3. Modificación socio. "
                       "\n4. Listar socios por apodo. "
                       "\n5. Listar socios por antigüedad. "
                       "\n6. Listar los socios con alta anterior a un año determinado. "
                       "\n7. Salir"))
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
        print(f"Listado de socios: \n{'\n'.join(listadoSociosAntiguedad())}\n")
    elif opcion == 6:
        print(listadoSociosAno())
    elif opcion == 7:
        print("Saliendo...")
    else:
        print("Opcion no valida")
