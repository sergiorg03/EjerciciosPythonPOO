class Libro:
    def __init__(self, titulo, autor, precio):
        self.titulo = titulo
        self.autor = autor
        self.precio = precio

    def Mostrar_informaciones(self):
        print(f"El libro con título: {self.titulo} ha sido escrito por el autor: {self.autor}\n y tiene un coste de {self.precio} Euros.")

libro1 = Libro("El Quijote", "Miguel de Cervantes", 29.99)

libro1.Mostrar_informaciones()