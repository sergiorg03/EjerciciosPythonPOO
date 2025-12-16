import sqlite3

class Libro:

    def __init__(self, titulo: str, autor: str, isbn: str, disponible:bool = True):
        self.titulo = titulo
        self.autor = autor
        self.isbn = isbn
        self.disponible = disponible

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
        
    '''def __str__(self):
        return f"El libro \"{self.titulo}\" de {self.autor} con ISBN: {self.isbn} {"Está disponible. " if self.disponible else "No está disponible. "}"'''


class Biblioteca:

    def create_db(self) -> None:
        try:
            cursor = self.conn.cursor()
            cursor.execute("CREATE TABLE IF NOT EXISTS libros (isbn TEXT PRIMARY KEY, titulo TEXT, autor TEXT, disponible BOOLEAN)")
            self.conn.commit()
        except Exception as e:
            print(f"Error al crear la base de datos: {e}")

    def get_books_from_db(self) -> list:
        try:
            libros = []
            cursor = self.conn.cursor()
            cursor.execute("SELECT titulo, autor, isbn, disponible FROM libros")
            for l in cursor.fetchall():
                libros.append(Libro(titulo=l[0], autor=l[1], isbn=l[2], disponible=l[3]))
            return libros
        except Exception as e:
            print(f"Error al obtener los libros: {e}")

    def guardar_libros_dic(self):
        self.libros = self.get_books_from_db()

    def __init__(self, nombre: str):
        self.nombre = nombre
        __NOMBRE_BD = 'biblioteca.db'
        try:
            self.conn = sqlite3.connect(__NOMBRE_BD)
        except Exception as e:
            print(f"Error al conectar a la base de datos: {e}")
        self.create_db()
        self.libros = self.get_books_from_db() if self.get_books_from_db() else []

    def save_to_db(self, libro: Libro) -> None:
        
        try:
            cursor = self.conn.cursor()
            cursor.execute("INSERT INTO libros (titulo, autor, isbn, disponible) VALUES (?, ?, ?, ?)", (libro.titulo, libro.autor, libro.isbn, libro.disponible))
            self.conn.commit()
        except Exception as e:
            print(f"Error al guardar el libro: {e}")

    def agregar_libro(self, libro: Libro) -> str | None:
        for l in self.libros:
            if l.isbn == libro.isbn:
                return f"El libro con ISBN {libro.isbn} ya está en la biblioteca. "
        else: 
            self.save_to_db(libro)
            self.guardar_libros_dic()
            return

    def mostrar_libros(self) -> list:
        return self.libros

    def buscar_por_titulo (self, titulo:str) -> Libro | None:
        try:
            cursor = self.conn.cursor()
            libro = cursor.execute("SELECT titulo, autor, isbn, disponible FROM libros WHERE UPPER(titulo) LIKE ?", (f"%{titulo.upper()}%",)).fetchone()
            if libro:
                return Libro(titulo=libro[0], autor=libro[1], isbn=libro[2], disponible=libro[3])
            else:
                return None
        except Exception as e:
            print(f"Se produjo un error al buscar el libro: {e}")
        ''' código para buscar libros en la lista
        for i in self.libros:
            if i.titulo.upper() == titulo.upper():
                return i
        else:
            return None'''

    def prestar_libro_bd(self, isbn):
        try:
            cursor = self.conn.cursor()
            cursor.execute("UPDATE libros SET disponible = ? WHERE isbn = ?", (False, isbn))
            self.conn.commit()
        except Exception as e:
            print(f"Se produjo un error al prestar el libro: {e}")

    def prestar_libro(self, isbn:str) -> bool:
        for i in self.libros:
            if i.isbn == isbn:
                i.prestar()
                self.prestar_libro_bd(isbn)
                self.guardar_libros_dic()
                return "Libro prestado correctamente. "
        else:
            print("El ISBN indicado no existe. ")
            return False

    def close_db(self):
        try:
            if self.conn:
                self.conn.close()
        except Exception as e:
            print(f"Se produjo un error al cerrar la base de datos: {e}")