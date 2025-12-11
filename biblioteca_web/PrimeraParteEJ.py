from biblioteca import Biblioteca, Libro

'''
    Primera parte del ejercicio. 
'''
biblio = Biblioteca("Biblioteca Central") # Creación de la biblioteca central

# Inserción de libros
biblio.agregar_libro(Libro("Libro 1", "Autor 1", "1234567789124"))
biblio.agregar_libro(Libro("Libro 2", "Autor 2", "1234567789125"))
biblio.agregar_libro(Libro("Libro 3", "Autor 3", "1234567789126"))
biblio.agregar_libro(Libro("Libro 1", "Autor 1", "1234567789124")) # Error: ISBN ya existente. 

print(f"\nMostramos los libros: \n{biblio.mostrar_libros()}")

print(f"\nPrestamos el libro con ISBN: 1234567789124 \n")
biblio.prestar_libro('1234567789124')


print(f"\nMostramos los libros: \n{biblio.mostrar_libros()}")

print(biblio.buscar_por_titulo("1"))

biblio.close_db()