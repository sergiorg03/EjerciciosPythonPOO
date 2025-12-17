# Importamos las librearias necesarias
from flask import Flask, render_template, request, jsonify, flash
from biblioteca import Biblioteca, Libro
# Constantes
biblioteca = Biblioteca("Biblioteca Central")

__INDEX = 'index.html'
__AGREGAR = 'agregar.html'
__PRESTAR_LIBRO = 'prestar_libro.html'
__DEVOLVER_LIBRO = 'devolver_libro.html'
__BASE_PRESTAR_DEVOLVER = 'base_prestar_devolver.html'
__BUSCAR_LIBRO = 'buscar.html'

app = Flask(__name__)

@app.route('/')
def index():
    '''
        FUNCION QUE RENDERIZA LA PÁGINA DE INICIO DE LA BIBLIOTECA, MUESTRA TODOS LOS LIBROS DE LA BIBLIOTECA.
        :return: archivo html a renderizar
    '''
    libros = biblioteca.mostrar_libros()
    return render_template(__INDEX, libros=libros)

@app.route('/agregar', methods=['GET', 'POST'])
def agregar_libro():
    '''
        FUNCION QUE RENDERIZA LA PÁGINA DE AGREGADO DE UN LIBRO Y OBTIENE LOS DATOS DE LA PÁGINA WEB
        :return: archivo html a renderizar
    '''
    mensaje, titulo, autor, isbn, disponible = "", "", "", "", True
    if request.method == 'POST':
        titulo = request.form['titulo']
        autor = request.form['autor']
        isbn = request.form['isbn']
        disponible = 'disponible' in request.form  # True si el checkbox está marcado
        
        libro = Libro(titulo=titulo, autor=autor, isbn=isbn, disponible=disponible)

        b = biblioteca.agregar_libro(libro) # TODO: libro con ISBN existente
        mensaje = "Libro agregado correctamente" if b is None else b
        
    return render_template(__AGREGAR, mensaje=mensaje, titulo=titulo, autor=autor, isbn=isbn, disponible=disponible)


@app.route('/prestar_libro')
def prestar_libro():
    '''
        FUNCION QUE RENDERIZA LA PÁGINA DE PRESTAMO DE UN LIBRO
        :return: archivo html a renderizar
    '''
    isbn = request.args.get('isbn')
    if isbn:
        mensaje = biblioteca.prestar_libro(isbn.strip())  
    else: 
        mensaje = "No se proporciono un ISBN"
    return render_template(__PRESTAR_LIBRO, mensaje=mensaje, isbn=isbn)

@app.route('/devolver_libro', methods=['GET', 'POST'])
def devolver_libro():
    '''
        FUNCION QUE RENDERIZA LA PÁGINA DE DEVOLUCIÓN DE UN LIBRO
        :return: archivo html a renderizar
    '''
    isbn = request.args.get('isbn')
    if isbn:
        mensaje = biblioteca.devolver_libro(isbn.strip())
    else:
        mensaje = "No se proporciono un ISBN"
    return render_template(__DEVOLVER_LIBRO, mensaje=mensaje, isbn=isbn)

@app.route('/base_prestar_devolver', methods=['GET', 'POST'])
def acciones_libros():
    '''
        FUNCION QUE RENDERIZA LA BASE PARA LAS PÁGINAS DE SOLICITUD Y DEVOLUCIÓN DE LIBROS DE LA BIBLIOTECA
        :return: archivo html a renderizar
    '''
    return render_template(__BASE_PRESTAR_DEVOLVER)

@app.route('/buscar', methods=['GET', 'POST'])
def buscar_libro():
    libros, mensaje = None, None
    titulo = request.args.get('titulo')
    if titulo:
        libros = biblioteca.buscar_por_titulo(titulo.strip())
        print(libros)
        if isinstance(libros, list):
            mensaje = "Libros encontrados"
        else:
            mensaje = "No se encontraron resultados. "

        print("\n\nERROR BUSCAR_LIBRO\n\n",libros, mensaje, titulo)
    
    return render_template(__BUSCAR_LIBRO, titulo=titulo, mensaje=mensaje, libros=libros)


if __name__ == '__main__':
    app.run(debug=True)