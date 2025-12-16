# Importamos las librearias necesarias
import sqlite3
from flask import Flask, render_template, request, jsonify, flash
from biblioteca import Biblioteca, Libro

biblioteca = Biblioteca("Biblioteca Central")

app = Flask(__name__)

@app.route('/')
def index():
    libros = biblioteca.mostrar_libros()
    return render_template('index.html', libros=libros)

@app.route('/agregar', methods=['GET', 'POST'])
def agregar_libro():
    mensaje = ""
    if request.method == 'POST':
        titulo = request.form['titulo']
        autor = request.form['autor']
        isbn = request.form['isbn']
        disponible = 'disponible' in request.form  # True si el checkbox está marcado
        
        libro = Libro(titulo=titulo, autor=autor, isbn=isbn, disponible=disponible)
        print(libro)
        b = biblioteca.agregar_libro(libro) # TODO: libro con ISBN existente
        mensaje = "Libro agregado correctamente" if b is None else b
        
    return render_template('agregar.html', mensaje=mensaje)


@app.route('/prestar_libro', methods=['GET', 'POST'])
def prestar_libro():
    

    return render_template('prestar_libro.html')

@app.route('/devolver_libro', methods=['GET', 'POST'])
def devolver_libro():
    

    return render_template('devolver_libro.html')

@app.route('/base_prestar_devolver', methods=['GET', 'POST'])
def acciones_libros():
    
    return render_template('base_prestar_devolver.html')

if __name__ == '__main__':
    app.run(debug=True)