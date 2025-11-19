'''
    EJERCICIO 3021
''' 
class Calculadora:
    def __init__(self, variable):
        self.variable = variable

    @staticmethod
    def suma(x, y):
        return (x + y)

    @staticmethod
    def multiplicación(x, y):
        return (x * y)

    @staticmethod
    def division(x, y):
        if y == 0:
            return "No se puede dividir entre 0. "
        return (x / y)

c = Calculadora(0)
x = 5
y = 7
print(f"La suma de {x} + {y} es: {c.suma(x, y)} ")
print(f"La multiplicación de {x} x {y} es: {c.multiplicación(x, y)} ")
print(f"La división de {x} entre {y} es: {c.division(x, y)} ")

y = 0
print(f"La división de {x} entre {y} es: {c.division(x, y)} ")
