'''
    EJERCICIO 3022
'''
class PC:

    def __init__(self, marca, modelo, precio):
        self.marca = marca
        self.modelo = modelo
        self.precio = precio

    @staticmethod
    def listar_marcas():
        print(("HP", "Dell", "Lenovo", "Apple"))

class Desktop(PC):

    def __init__(self, marca, modelo, precio, tamano):
        super().__init__(marca, modelo, precio)
        self.tamano = tamano

    def mostrar_info(self):
        print(f"El ordenador de sobremesa es de marca {self.marca}, modelo {self.modelo}, tiene un tamaño de CPU de {self.tamano} cms y cuesta {self.precio} euros. ")

class Laptop(PC):

    def __init__(self, marca, modelo, precio, tamanoPantalla):
        super().__init__(marca, modelo, precio)
        self.tamanoPantalla = tamanoPantalla
    
    def mostrar_info(self):
        print(f"El portatil de marca {self.marca}, modelo {self.modelo} y tamaño de pantalla {self.tamanoPantalla} tiene un coste de {self.precio} euros. ")

print("PC", "-"*25)
PC.listar_marcas()

print("Desktop", "-"*25)
d = Desktop("Asus", "Asrock", 2000, 7)
d.mostrar_info()

print("Laptop", "-"*25)
l = Laptop("HP", "Notebook", 800, 15.6)
l.mostrar_info()