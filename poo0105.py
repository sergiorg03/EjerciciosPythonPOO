'''
Solicitar la carga del nombre de una persona en minúsculas.
Mostrar un mensaje si comienza con una vocal dicho nombre.
'''

n1 = input("Ingrese un nombre en minúsculas: ")
vocales = ["a", "e", "i", "o", "u"]
if (n1[0] in vocales):
    print("Comienza por vocal")
else:
    print("No comienza por vocal")