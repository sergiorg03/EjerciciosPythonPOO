'''
    EJERCICIO 3023
'''

class Usuario:
    numeroUsuariosActivos = 0

    def __init__(self, nombre, apellido, edad):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad

        Usuario.numeroUsuariosActivos += 1

    @classmethod
    def extraer_info(cls, cadena):
        nombre, apellido, edad = cadena.split(",")
        return cls(nombre, apellido, edad)
    
    @classmethod
    def mostrar_usuarios_activos(cls):
        return f"El número de usuarios activos es {cls.numeroUsuariosActivos}. "

    def __del__(self):
        print(f"El usuario que se ha desconectado es: {self.nombre}, {self.apellido} y tiene {self.edad} años. ")
        Usuario.numeroUsuariosActivos -= 1

u1 = Usuario("Juan", "Martinez", 23)
u2 = Usuario.extraer_info("CR7,El bicho,37")
u3 = Usuario("Killian", "MBappe", 34)

print(Usuario.mostrar_usuarios_activos())

# TODO: Corregir la ejecucion __del__