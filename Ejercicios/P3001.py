class Galleta:
    def __init__(self, nombre, forma):
        self.nombre = nombre
        self.forma = forma

    def __hornear__(self):
        print(f"Esta galleta de {self.nombre} ha sido horneada en forma de {self.forma}. \nBuen provecho.")

galleta = Galleta("Chispas de chocolate", "estrella")

galleta.__hornear__()