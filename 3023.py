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
        print(f"Usuario '{self.nombre} {self.apellido}' creado. Usuarios activos: {Usuario.numeroUsuariosActivos}")

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

print("-"*40)
print("Creación Usuarios")
u1 = Usuario("Juan", "Martinez", 23)
u2 = Usuario.extraer_info("CR7,El bicho,37")
u3 = Usuario("Killian", "MBappe", 34)
print("-"*40)
print("Usuarios activos: ")
print(f"{Usuario.mostrar_usuarios_activos()}")

print("\nEliminamos el usuario 3. ")
del u3
print("\nMostramos los usuarios activos: ")
print(Usuario.mostrar_usuarios_activos(),"\n")

print("\n\nFin del programa y eliminado automático de los demás usuarios para liberar memoria. \n")