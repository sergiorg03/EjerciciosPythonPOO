'''
    Ejercicio 3020
'''
class Trabajador:

    def __init__(self, nombre, salario, edad):
        self.nombre = nombre
        self.salario = salario
        self.edad = edad

    def mostrar_funcion(self):
        print("Soy un trabajador. ")

    def mostrar_info(self):
        print(f"Me llamo {self.nombre} y cobro {self.salario} euros. ")

class Director(Trabajador):
    
    def __init__(self, nombre, salario, edad, prima):
        super().__init__(nombre, salario, edad)
        self.prima = prima

    def mostrar_funcion(self):
        print("Soy el director de la empresa. ")

    def mostrar_info(self):
        print("Soy el director y me llamo {self.nombre} y cobro {self.salario} euros y tengo una prima de {self.prima} euros. ")

class Ingeniero(Trabajador):

    def __init__(self, nombre, salario, edad, especialidad):
        super().__init__(nombre, salario, edad)
        self.especialidad = especialidad

    def mostrar_funcion(self):
        print("Soy un ingeniero. ")
        
    def mostrar_info(self):
        print(f"Soy el ingeniero y me llamo {self.nombre}, cobro {self.salario} y estoy especializado en {self.especialidad}. ")


print("Trabajador ", "-"*25)
t = Trabajador("Pepe", 1500, 45)
t.mostrar_funcion()
t.mostrar_info()

print("Director ", "-"*25)
d = Director("manueh", 2000, 35, 1500)
d.mostrar_funcion()
d.mostrar_info()

print("Ingeniero ", "-"*25)
i = Ingeniero("Messi", 1800, 26, "Informática")
i.mostrar_funcion()
i.mostrar_info()