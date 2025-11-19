'''
    Ejercicio 3015
'''
class Empleado:

    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def __del__(self):
        del self
        print(f"Las referencias creadas del objeto han sido eliminadas. ")

e = Empleado("Sergio", 25)

# TODO: ejecución método __del__ sin llamada