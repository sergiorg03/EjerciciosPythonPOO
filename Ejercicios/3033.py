'''
    Ejercicio 3033
'''
import random

class Colores:

    def __init__(self):
        self.colores = "AZUL:ROJO:AMARILLO:VERDE:BLANCO:NEGRO"

    def tabla_colores(self, n):
        lista_colores = self.colores.split(":")
        
        #Comprobamos que el número de colores que nos pidan sea el mismo que colores tenemos
        if n > len(lista_colores):
            return "No hay suficientes colores para elegir. "

        return random.sample(lista_colores, n) # Obtenemos los n colores aleatoriamente 

    def sumar_color(self, name):
        name = name.upper()

        if name not in self.colores.split(":"):
            self.colores += f":{name}"

# Prueba
tc = Colores()
tc.sumar_color("violeta")
tc.sumar_color("magenta")
tc.sumar_color("naranja")
print(tc.tabla_colores(3))