'''

    Ejercicio 3028

'''

import random

import os

import string

class generador_clave:


    def __init__(self, longitud: int = 8, caracteresEspeciales : bool = True, numeros : bool = True, mayusculas : bool = True, minusculas : bool = True):
        self.longitud = longitud

        self.caracteresEspeciales = caracteresEspeciales

        self.numeros = numeros

        self.mayusculas = mayusculas

        self.minusculas = minusculas


    def Mayusculas(self, mayusculas):

        self.mayusculas = mayusculas


    def Minusculas(self, minusculas):

        self.minusculas = minusculas


    def Numeros(self, numeros):

        self.numeros = numeros


    def CaracteresEspeciales (self, caracteresEspeciales):

        self.caracteresEspeciales = caracteresEspeciales


    def Modificar_longitud(self, longitud):
        self.longitud = longitud
    

    def generarClave(self):
        valor = ''

        if self.numeros:
            valor += string.digits

        if self.caracteresEspeciales:
            valor += string.punctuation

        if self.mayusculas:
            valor += string.ascii_uppercase

        if self.minusculas:
            valor += string.ascii_lowercase


        clave = ''.join(random.choice(valor) for _ in range(self.longitud))
        return clave



    def valoraClave(self, clave):

        robustez = 0

        if len(clave) > 10:
            robustez += 1

        if any(c.isupper() for c in clave):
            robustez += 1

        if any(c.islower() for c in clave):
            robustez += 1

        if any(c.isdigit() for c in clave):
            robustez += 1

        if any(c in string.punctuation for c in clave):
            robustez += 1

        return robustez
            



    def guardarClave(self,clave,ruta: str = 'claves.txt'):
        with open(ruta, 'w') as f:
            f.write(clave)
        

    def leerClave(self, ruta):
        if os.path.exists(ruta):
            with open(ruta, "r") as f:
                return f.read().strip()
        else:
            return None



## pruebas / casos de uso

generador_clave = generador_clave(12)

clave1 = generador_clave.generarClave()

print(clave1)

print("Robustez de la clave1 (0 es debil-5 es muy robusta): " +

str(generador_clave.valoraClave(clave1)))

print("- "*20)

generador_clave.Mayusculas(False)

generador_clave.Minusculas(False)

generador_clave.CaracteresEspeciales(True)

clave2 = generador_clave.generarClave()

print(clave2)

print("Robustez de la clave2 (0 es debil-5 es muy robusta): " +

str(generador_clave.valoraClave(clave2)))

print("- "*20)

print("Guardando la clave2 ...")

generador_clave.guardarClave(clave2)

print("Clave2 guardada ok!")

print("Leyendo la clave2 ...")

print(generador_clave.leerClave(clave2))