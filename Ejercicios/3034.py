'''
    Ejercicio 3034
'''
class SintonizadorFM:

    def __init__(self, frecuencia = 80):
        self.frecuencia = 80 if (frecuencia < 80 or frecuencia > 108) else frecuencia
    
    def up(self):
        self.frecuencia += 0.5

        if self.frecuencia > 108:
            self.frecuencia = 80

    def down(self):
        self.frecuencia -= 0.5

        if self.frecuencia < 80:
            self.frecuencia = 108

    def display(self):
        print(f"Frecuencia sintonizada a {self.frecuencia} MHz. ")

#Prueba
azul = SintonizadorFM(107)
azul.up()
azul.up()
azul.up()
azul.up()
azul.display()
verde = SintonizadorFM(200)
verde.display()