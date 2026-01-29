'''
    Ejercicio 3030
'''
class Bombilla:

    __interruptor_general = True

    def __init__(self, estado_inicial:bool = False):
        self.__encendida = estado_inicial

    def estado(self):
        if Bombilla.__interruptor_general:
            print("La bombilla está","encendida. " if self.__encendida else "apagada. ")
        else:
            print("El botón general está apagado. ")

    def encender(self):
        self.__encendida = True

    def apagar(self):
        self.__encendida = False

    @classmethod
    def activar_interruptor_general(cls):
        cls.__interruptor_general = True

        print("Interruptor general activado. Las bombillas recuperan su estado anterior.")

    @classmethod
    def desactivar_interruptor_general(cls):
        cls.__interruptor_general = False

        print("Interruptor general desactivado. Todas las bombillas apagadas.")

# Creación de las instancias
b1 = Bombilla(True)   
b2 = Bombilla(False)

b1.estado()
b2.estado()

# Apagar el interruptor general
Bombilla.desactivar_interruptor_general()
b1.estado()
b2.estado()

# Encender bombilla b2 mientras interruptor general apagado

b2.encender()
b2.estado() 

# Activar el interruptor general
Bombilla.activar_interruptor_general()
b1.estado()
b2.estado()