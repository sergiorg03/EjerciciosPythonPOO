'''
    Ejercicio 3031
'''
class CambioMonedas:

    def __init__(self, importeCompra, dineroCliente):
        self.importeCompra = importeCompra
        self.dineroCliente = dineroCliente

    def mostrar_cambio(self):
        cambio = round(self.dineroCliente - self.importeCompra, 2)
        if cambio < 0:
            print(f"Error!! Faltan {abs(cambio):.2f} euros. ")
        
        print(f"Cambio resultante de {cambio:.2f}: ")
        if cambio == 0:
            print(f"Pago realizado correctamente. \nGracias por su compra! ")
        
        billetes = [100, 50, 20, 10, 5]
        monedas = [
            (2, "2€"),
            (1, "1€"),
            (0.50, "50 cent"),
            (0.20, "20 cent"),
            (0.10, "10 cent"),
            (0.05, "5 cent")
        ]

        # Billetes de cambio
        for billete in billetes:
            if cambio >= billete:
                cantidad = int(cambio // billete) # Número de billetes del mismo valor
                cambio = round(cambio - cantidad * billete, 2)
                print(f"Billetes {billete}€: {cantidad}")
                
        # Monedas de cambio
        for dinero, nombre in monedas:
            if cambio >= dinero:
                cantidad = int(cambio//dinero) # Numero de monedas que puedo utilizar para dar el cambio del mismo valor
                cambio = round(cambio - cantidad * dinero, 2)
                print(f"Monedas {nombre}: {cantidad} ")

# Pruebas
c1 = CambioMonedas(215.35, 250)
c1.mostrar_cambio()
print("*"*20)

c2 = CambioMonedas(100, 80)
c2.mostrar_cambio()
print("*"*20)

c3 = CambioMonedas(75.75, 90)
c3.mostrar_cambio()
print("*"*20)