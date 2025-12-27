from biblioteca import Biblioteca, Libro

'''
    Primera parte del ejercicio. 
'''
biblio = Biblioteca("Biblioteca Central") # Creación de la biblioteca central

# Inserción de libros
print(biblio.agregar_libro(Libro("El señor de los anillos", "J.R.R. Tolkien", "123456789")))
print(biblio.agregar_libro(Libro("Los juegos del hambre", "Suzanne Collins", "123456788")))
print(biblio.agregar_libro(Libro("Cien años de soledad", "Gabriel Garcia Marquez", "123456787")))
print(biblio.agregar_libro(Libro("El principito", "Antoine de Saint-Exupéry", "123456788"))) # Error: ISBN ya existente. 

print(f"\nMostramos los libros: \n{"\n".join([f"{l.titulo}, {l.autor}, {l.isbn}, {"Disponible en la biblioteca" if l.disponible else "No se encuentra disponible"}" for l in biblio.mostrar_libros()])}")

print(f"\nPrestamos el libro con ISBN: 123456789 \n")
print(biblio.prestar_libro('123456789'))

print(f"\nMostramos los libros: \n{"\n".join([f"{l.titulo}, {l.autor}, {l.isbn}, {"Disponible en la biblioteca" if l.disponible else "No se encuentra disponible"}" for l in biblio.mostrar_libros()])}")

print("\n")

print(f"\nBuscamos libros que coincidan con el titulo: \n{"\n".join([f"{l.titulo}, {l.autor}, {l.isbn}, {"Disponible en la biblioteca" if l.disponible else "No se encuentra disponible"}" for l in biblio.buscar_por_titulo("l")])}")

biblio.close_db()