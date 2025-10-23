'''
Crear un generador de palabros técnicos (BuzzWord), con el fin de poder rellenar informes de jerga.
A partir de 3 columnas de 10 términos generaremos un palabro técnico escogiendo aleatoriamente 1 palabra de cada columna.
Vamos a utilizar tuplas para guardar la colección de elementos que no cambian.
También crearemos una función que muestra todos los palabros.

'''

# Importamos las librerias necesarias
from random import randint

columna1 = ('integrated', 'total', 'systematized', 'parallel', 'functional',
'responsive', 'optimal', 'synchronized', 'compatible', 'balanced')

columna2 = ('management', 'organizational', 'monitored', 'reciprocal',
'digital', 'logistical', 'transitional', 'incremental',
'third-generation', 'policy')

columna3 = ('options', 'flexibility', 'capability', 'mobility', 'programming',
'concept', 'time-phase', 'projection', 'hardware', 'contingency')

# Genera 3 cifras aleatorias y obtiene el buzzword correspondiente
def generateRandomBuzzWord():
    # Con el método randint(inicio, fin) muestra un entero aleatorio desde el inicio hasta el fin, AMBOS INCLUIDOS
    cifra1 = randint(0, len(columna1)-1)
    cifra2 = randint(0, len(columna2)-1)
    cifra3 = randint(0, len(columna3)-1)
    return f"{getBuzzWord(cifra1, cifra2, cifra3)}"

# Usamos un único número de 3 cifras (entre 0 y 999) que define nuestro buzzWord
def generateBuzzWord(id):
    return f"{getBuzzWord(int(str(id).zfill(3)[0]), int(str(id).zfill(3)[1]), int(str(id).zfill(3)[2])) if 0 <= id <= 999 else "No es posible generar el buzz word"}"

# Devuelve el buzzword asociado a esas 3 cifras
def getBuzzWord(col1, col2, col3):
    return f"{columna1[col1]} {columna2[col2]} {columna3[col3]}"

# Muestra todos los buzzwords
def showAllBuzzword():
    #return [[[columna3[k] for k in columna3], columna2[j] for j in columna2], columna1[i]for i in columna1]
    lista =  [generateBuzzWord(x) for x in range(0, 999)]
    return lista

print('Generando una BuzzWord aleatoria: ' + generateRandomBuzzWord())
id = int(input("Introduce un número para generar una BuzzWord: "))
print(generateBuzzWord(id))
print(f"Mostramos todos los palabros posibles: ")
listaAllBuzzWords = showAllBuzzword()
#print(f"{[x for x in listaAllBuzzWords]}")
print("\n".join(listaAllBuzzWords))
