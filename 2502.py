'''
Queremos gestionar la plantilla de un equipo de fútbol, en la que a cada jugador se le asigna un dorsal que no puede estar repetido.
Para ello vamos a crear un diccionario, con el dorsal como clave y un objeto de la clase Jugador como valor.
De cada jugador se guarda el DNI, el nombre, la posición en el campo (para simplificar, los jugadores pueden ser porteros, defensas, centrocampistas y
delanteros) y su estatura. Define la clase Jugador, implementa los siguientes métodos estáticos:

➢ altaJugador(plantilla, dorsal): que añade una entrada al diccionario con el dorsal y el jugador creado dentro del método, introduciendo sus datos por consola.

➢ eliminarJugador(plantilla, dorsal): que elimina la entrada correspondiente al jugador.
Dicho dorsal desaparece del diccionario hasta que se asigne a otro jugador por medio de un alta. El método devuelve el jugador eliminado.

➢ mostrar (plantilla): que muestra una lista de los dorsales con los nombres de los jugadores correspondientes.

➢ editarJugador(plantilla, dorsal): que permite modificar los datos de un jugador, excepto su dorsal. Devuelve true si el dorsal existe y false en caso contrario. SUSTITUIMOS UN JUGADOR POR OTRO.
Dorsal 3 pertenece a Luis, se llama a la función, y le damos el dorsal 3 a otro jugador nuevo.
'''

class Jugador:
    DNI = ""
    nombre = ""
    posicion = ""
    estatura = 0

    def __init__(self, dni: str, nombre: str, posicion: str, estatura: int):
        self.DNI = dni
        self.nombre = nombre
        self.posicion = posicion
        self.estatura = estatura

    def getDNI(self):
        return self.DNI

    def getNombre(self):
        return self.nombre

    def getPosicion(self):
        return self.posicion

    def getEstatura(self):
        return self.estatura

    def setNombre(self, nombre):
        self.nombre = nombre

    def setPosicion(self, posicion):
        self.posicion = posicion

    def setEstatura(self, estatura):
        self.estatura = estatura

    def toString(self):
        return f"DNI: {self.getDNI()}, Nombre: {self.getNombre()}, Posición: {self.getPosicion()}, Estatura: {self.getEstatura()}"


if __name__ == '__main__':
    POSICIONES = ["PORTERO", "DEFENSA", "CENTROCAMPISTA", "DELANTERO"]
    j1 = Jugador("28548847", "SERGIO", "CENTROCAMPISTA", 160)
    j2 = Jugador("28544447", "ANDRES", "DELANTERO", 180)
    j3 = Jugador("23338847", "SULI", "DELANTERO", 190)
    j4 = Jugador("28511147", "JONATAN", "DEFENSA", 165)
    j5 = Jugador("28523237", "LUIS", "CENTROCAMPISTA", 160)
    plantilla = {6: j1, 5: j2, 7: j3, 2: j4, 3: j5}

'''
Intentar poner un atributo por defecto en el método y eliminar el método mostrarJugador
'''
    def mostrar(plantilla):
        for i in plantilla:
            print(f"Jugador con dorsal {i}: {plantilla[i].toString()}")

    def altaJugador(plantilla, dorsal):
        DNI = input("Introduce el DNI del jugador nuevo: ")
        nombre = input("Introduce el nombre del jugador nuevo: ")
        pos = input("Introduce la posicion del jugador nuevo (portero, defensa, centrocampista o delantero): ")
        altura = int(input("Introduce la altura del jugador nuevo: "))
        j6 = Jugador(DNI, nombre, pos, altura)
        plantilla[dorsal] = j6
        print("Jugador añadido correctamente .")

    def eliminarJugador(plantilla, dorsal):
        plantilla.pop(dorsal)
        print("Jugador eliminado correctamente.")

    def mostrarJugador(plantilla, dorsal):
        print(f"Jugador con dorsal {dorsal}: {plantilla[dorsal].toString()}")

    def editarJugador(plantilla, dorsal):
        print(f"Editando al jugador {dorsal}.")
        opcion = -1
        while opcion != 0:
            opcion = int(input("Que datos desea editar? \n1 --> Nombre \n2 --> posicion \n3 --> Estatura \n0 --> SALIR"))
            if opcion == 1:
                plantilla[dorsal].setNombre(input("Introduce el nombre del jugador: "))
            elif opcion == 2:
                pos = input("Introduce la posicion del jugador (portero, defensa, centrocampista o delantero si no se le asignará por defecto PORTERO): ")
                plantilla[dorsal].setPosicion(pos if pos.upper() in POSICIONES else "PORTERO")
            elif opcion == 3:
                plantilla[dorsal].setEstatura(input("Introduce la altura del jugador: "))
            elif opcion == 0:
                print("Saliendo del modo edición. ")
            else:
                print("Opcion invalida. ")
        mostrarJugador(plantilla, dorsal)

    def cambioJugadorDorsal(plantilla, dorsal):
        dni = input("Introduce el DNI del jugador: ")
        nombre = input("Introduce el nombre del jugador: ")
        posicion = input("Introduce la posicion del jugador (portero, defensa, centrocampista o delantero si no se le asignará por defecto PORTERO): ")
        posicion = posicion if posicion.upper() in POSICIONES else "portero"
        estatura = input("Introduce la altura del jugador: ")
        plantilla[dorsal] = Jugador(dni, nombre, posicion, int(estatura))




    '''print("PLANTILLA ACTUAL ..................")
    mostrar(plantilla)
    print("\nAlta del jugador con el dorsal 10 ..........")
    altaJugador(plantilla, 10);
    print("\nElimina al jugador con el dorsal 7 ..........")
    eliminarJugador(plantilla, 7)
    print("\nPLANTILLA ACTUAL ..................")
    mostrar(plantilla)'''
    print("\nEdita al jugador con el dorsal 2 ..........")
    editarJugador(plantilla, 2)
    #cambioJugadorDorsal(plantilla, 2) # Sustitución de un jugador por otro
    print("\nPLANTILLA ACTUAL ..................")
    mostrar(plantilla)