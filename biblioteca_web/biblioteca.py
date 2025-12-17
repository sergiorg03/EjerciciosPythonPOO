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
            cursor.execute("CREATE TABLE IF NOT EXISTS libros (isbn TEXT PRIMARY KEY, titulo TEXT, autor TEXT, disponible BOOLEAN DEFAULT TRUE)")
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
        self.__NOMBRE_BD = './biblioteca.db'
        try:
            self.conn = sqlite3.connect(self.__NOMBRE_BD, check_same_thread=False)
        except Exception as e:
            print(f"Error al conectar a la base de datos: {e}")
        self.create_db()
        self.libros = self.get_books_from_db() if self.get_books_from_db() else []

    def agregar_libro(self, libro: Libro) -> str | None:
        __SENTENCIA = """
            INSERT INTO libros (titulo, autor, isbn, disponible)
            VALUES (?, ?, ?, ?)
        """
        __COMPROBACION_EXISTENCIA = '''
            SELECT * 
                FROM libros 
                WHERE isbn = ?
        '''
        try:
            c = self.conn.cursor()
            existe = c.execute(__COMPROBACION_EXISTENCIA, (libro.isbn, )).fetchone()
            if existe is None:
                c.execute(__SENTENCIA, (libro.titulo, libro.autor, libro.isbn, libro.disponible))
                self.conn.commit()
                self.guardar_libros_dic()
                return "Libro agregado correctamente. "
            else: # El libro existe
                return "El ISBN introducido ya existe. Introduzca un ISBN correcto. "
        except Exception as e:
            print(e)
            return "Se produjo un error a hora de añadir el libro a la biblioteca. Por favor intentelo de nuevo más tarde. "

    def mostrar_libros(self) -> list:
        try:
            c = self.conn.cursor()
            libros = c.execute("SELECT titulo, autor, isbn, disponible FROM libros").fetchall()
            if libros:
                return [Libro(titulo=l[0], autor=l[1], isbn=l[2], disponible=l[3]) for l in libros]
        except Exception as e:
            print(e)
            return "No se pudieron recuperar datos. "

    def buscar_por_titulo (self, titulo:str) -> Libro | None:
        try:
            cursor = self.conn.cursor()
            libro = cursor.execute("SELECT titulo, autor, isbn, disponible FROM libros WHERE UPPER(titulo) LIKE ?", (f"%{titulo.upper()}%",)).fetchall()
            if libro:
                return [Libro(titulo=l[0], autor=l[1], isbn=l[2], disponible=l[3]) for l in libro]
            else:
                return "No se encontraron resultados. "
        except Exception as e:
            print(f"Se produjo un error al buscar el libro: {e}")

    def prestar_libro_bd(self, isbn):
        try:
            cursor = self.conn.cursor()
            cursor.execute("UPDATE libros SET disponible = ? WHERE isbn = ?", (False, isbn))
            self.conn.commit()
        except Exception as e:
            print(f"Se produjo un error al prestar el libro: {e}")

    def prestar_libro(self, isbn:str) -> bool:
        __SENTENCIA = '''
            SELECT disponible
                FROM libros 
                WHERE isbn = ?
        '''

        try:
            c = self.conn.cursor()
            dispo = c.execute(__SENTENCIA, (isbn, )).fetchone()
            if dispo is not None:
                if dispo[0]:
                    c.execute("UPDATE libros SET disponible = ? WHERE isbn = ?", (False, isbn, ))
                    self.conn.commit()
                    self.guardar_libros_dic()
                    return "Libro prestado correctamente. " # No modificar mensaje
                else:
                    return "El libro indicado ya fue prestado anteriormente. "
            else:
                return "El libro con el ISBN indicado no existe. "
        except Exception as e:
            print(e)
            return "Ocurrio un error y no se pudo prestar el libro indicado. Intentelo de nuevo más tarde."

        '''for i in self.libros:
            if i.isbn == isbn:
                i.prestar()
                self.prestar_libro_bd(isbn)
                self.guardar_libros_dic()
                return "Libro prestado correctamente. " # No modificar mensaje
        else:
            return "El ISBN indicado no existe. "'''

    def devolver_libro(self, isbn:str) -> str:
        __SENTENCIA = f'''
            SELECT disponible 
                FROM libros
                WHERE isbn = ?
        '''
        try:
            c = self.conn.cursor()

            dispo = c.execute(__SENTENCIA, (isbn,)).fetchone()
            if dispo is not None:
                if not dispo[0]:
                    c.execute("UPDATE libros SET disponible = ? WHERE isbn = ?", (True, isbn, ))
                    self.conn.commit()
                    self.guardar_libros_dic()
                    return "Libro devuelto correctamente. " # No modificar mensaje
                    
                else:
                    return "El libro indicado se encuentra en la biblioteca. "
            else:
                return "El libro indicado no existe. "
        except Exception as e:
            print(e)
            return "Ocurrio un error y no se pudo devolver el libro indicado. Intentelo de nuevo más tarde."

    def close_db(self):
        try:
            if self.conn:
                self.conn.close()
        except Exception as e:
            print(f"Se produjo un error al cerrar la base de datos: {e}")