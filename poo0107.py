'''
Solicitar el ingreso de una clave y guardarla en una cadena de caracteres.
Controlar que el tamaño esté entre 10 y 20 caracteres, en caso contrario mostrar error.
'''

clave=input(str("Ingrese la clave: "))
if (len(clave)>=10 and len(clave)<=20):
    print("Entre 10 y 20 caracteres")
else:
    print("No entre 10 y 20 caracteres")
