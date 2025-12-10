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

print(biblio.mostrar_libros())

print(f"Prestamos el libro con ISBN: 1234567789124 ")
biblio.prestar_libro('1234567789124')


print(biblio.mostrar_libros())

print(biblio.buscar_por_titulo("1"))