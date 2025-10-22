'''
Escribe un programa donde partiendo de una frase que conste exclusivamente de palabras separadas por espacios, las palabras de la frase se almacenarán en una lista.
Finalmente, se mostrarán por pantalla las palabras que estén repetidas y, a continuación las que no lo estén.
Ejemplo de salida por consola:
['uno', 'dos', 'dos', 'tres', 'tres', 'tres']
Palabras repetidas: ['dos', 'tres']
Palabras no repetidas: ['uno']
'''

frase = input("Ingresa una frase: ").split() # .split() --> te separa una cadena por el caracter indicado. Por defecto lo separa por espacios " "

palabrasRepetidas = []
palabrasNoRepetidas = []

for palabra in frase:
    if frase.count(palabra) > 1:
        if palabra not in palabrasRepetidas:
            palabrasRepetidas.append(palabra)
    else:
        if palabra not in palabrasNoRepetidas:
            palabrasNoRepetidas.append(palabra)

print(f"la frase original es: {frase}")
print(f"Las palabras repetidas son: {palabrasRepetidas}")
print(f"Las palabras no repetidas son: {palabrasNoRepetidas}")