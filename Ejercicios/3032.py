'''
    Ejercicio 3032
'''

class Calendario:


    def __init__(self, dia, mes, anio):
        self.dia = dia
        self.mes = mes 
        self.anio = anio

    def incrementarDia(self):
        meses = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

        # Comprobamos si es bisiesto el año
        if (self.anio % 4 == 0 and self.anio % 100 != 0) or (self.anio % 400 == 0):
            meses[1] = 29
        
        # Sumamos el día
        self.dia += 1

        # Comprobamos si es el último día del mes
        if self.dia > meses[self.mes - 1]:
            self.dia = 1
            self.incrementarMes()

    def incrementarMes(self):
        if self.mes == 12:
            self.mes = 1
            self.incrementarAnio(1)
        else:
            self.mes += 1

    def incrementarAnio(self, n):
        self.anio += n

    def mostrar(self):
        print(f"Fecha (DD/MM/YYYY): {self.dia}/{self.mes}/{self.anio}.")

    def iguales(self, otraFecha):
        return (self.dia == otraFecha.dia and self.mes == otraFecha.mes and self.anio == otraFecha.anio)
    
# PRUEBAS
c1 = Calendario(28, 12, 2024)
c1.incrementarDia()
c1.incrementarDia()
c1.incrementarDia()
c1.mostrar()
c2 = Calendario(4, 1, 2025)
c2.mostrar()
print("Fechas iguales:", c1.iguales(c2))
c1.incrementarDia()
c1.mostrar()
c2.mostrar()
print("Fechas iguales:", c1.iguales(c2))