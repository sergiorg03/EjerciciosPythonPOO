# Importamos las librearias necesarias
import sqlite3
from flask import Flask, render_template, request, jsonify
from biblioteca import Biblioteca, Libro

biblioteca = Biblioteca("Biblioteca Central")

app = Flask(__name__)

@app.route('/')
def index():
    libros = biblioteca.mostrar_libros()
    return render_template('index.html', libros=libros)

if __name__ == '__main__':
    app.run(debug=True)