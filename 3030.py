'''

    Ejercicio 3030

'''

class Bombilla:

    _interruptor_general = True


    def __init__(self, estado_inicial:bool = False):

        self.__encendida = estado_inicial
        self.__estado = estado_inicial

    def estado(self):
        print(f"La bombilla está","apagada" if not self._interruptor_general else "encendida")

    def encender(self):
        self.__encendida = True
        self.__estado = True

    def apagar(self):
        self.__encendida = False
        self.__estado = False
    

    @classmethod

    def activar_interruptor_general(cls):
        cls._interruptor_general = True

        print("Interruptor general activado. Las bombillas recuperan su estado anterior.")


    @classmethod

    def desactivar_interruptor_general(cls):
        cls._interruptor_general = False

        print("Interruptor general desactivado. Todas las bombillas apagadas.")

# Creación de las instancias
b1 = Bombilla(True)   
b2 = Bombilla(False)
print(f"Bombilla b1")
b1.estado()
print("Bombilla b2")
b2.estado()

# Apagar el interruptor general
Bombilla.desactivar_interruptor_general()
b1.estado()
b2.estado()

# Encender bombilla b2 mientras interruptor general apagado
b2.encender()
b2.estado() # Apagada (interruptor general OFF)

# Activar el interruptor general
Bombilla.activar_interruptor_general()
b1.estado()
b2.estado()


# TODO: Corregir clase 