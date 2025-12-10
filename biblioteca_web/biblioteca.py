class Libro:

    def __init__(self, titulo: str, autor: str, isbn: str):
        self.titulo = titulo
        self.autor = autor
        self.isbn = isbn
        self.disponible = True

    def prestar(self):
        if self.disponible:
            self.disponible = False
            return True
        else: 
            print(f"El libro {self.titulo} no está disponible. ")
            return False

    def devolver(self):
        if not self.disponible: 
            self.disponible = True
        else:
            print(f"El libro {self.titulo} no está prestado. ")
        
    def __str__(self):
        return f"El libro \"{self.titulo}\" de {self.autor} con ISBN: {self.isbn} {"Está disponible. " if self.disponible else "No está disponible. "}"


class Biblioteca:

    def __init__(self, nombre: str):
        self.nombre = nombre
        self.libros = []

    def agregar_libro(self, libro: Libro) -> None:
        for l in self.libros:
            if l.isbn == libro.isbn:
                print(f"El libro con ISBN {libro.isbn} ya está en la biblioteca. ")
                return
        else: 
            self.libros.append(libro)

    def mostrar_libros(self) -> str:
        cad = ""
        for l in self.libros:
            cad += str(l) + "\n"
        return cad

    def buscar_por_titulo (self, titulo:str) -> Libro | None:
        for i in self.libros:
            if i.titulo.upper() == titulo.upper():
                return i
        else:
            return None

    def prestar_libro(self, isbn:str) -> bool:
        for i in self.libros:
            if i.isbn == isbn:
                i.prestar()
                return "Libro prestado correctamente. "
        else:
            print("El ISBN indicado no existe. ")
            return False
