'''
    Ejercicio 3015
'''
class Empleado:

    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
        print(f"Empleado '{self.nombre}' de {self.edad} años ha sido creado.")

    def __del__(self):
        print(f"Empleado eliminado correctamente. ")

e1 = Empleado("Sergio", 25)
e2 = Empleado("Pedro", 34)

print(f"Empleado 1: {e1.nombre, e1.edad}. ")

del e1

print(f"Empleado 2: {e2.nombre, e2.edad}. ")

# Elimina al último empleado cuando termina el programa para liberar memoria