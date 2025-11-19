'''
    EJERCICIO 3024
'''
class CuentaBancaria:
    tipo = "CC"
    tasaInteres = 0

    def __init__(self, nombre, apellidos, numero_cuenta, saldo):
        self.nombre = nombre
        self.apellidos = apellidos
        self.numero_cuenta = numero_cuenta
        self.saldo = saldo

    @classmethod
    def modificar_tasa_interes(cls, nueva_tasa):
        cls.tasaInteres = nueva_tasa

    @classmethod
    def modificar_tipo(cls, nuevo_tipo):
        cls.tipo = nuevo_tipo

    def ingreso(self, cantidad):
        if cantidad >= 0:
            self.saldo += cantidad
            print("Ingreso realizado correctamente. ")
        else:
            print("No es posible ingresar la cantidad indicada. ")

    def retiro(self, cantidad):
        if cantidad > 0:
            if cantidad <= self.saldo:
                self.saldo -= cantidad
                print("Retiro realizado correctamente. ")
            else:
                print("No dispone de tanto saldo para retirar. ")
        else:
            print("No es posible retirar esa cantidad. ")

    def aplica_tasa_interes(self):
        interes = self.saldo * self.tasaInteres
        self.saldo -= interes
        return interes

    def __str__(self):
        return f"La cuenta bancaria es de tipo {self.tipo}, \nEl titular es {self.nombre, self.apellidos}, \nEl número de cuenta es: {self.numero_cuenta}, \nDispone de un saldo de {self.saldo} euros y \nTiene un interes del {self.tasaInteres*100:.2f} %. "


c1 = CuentaBancaria("Lionel", "Messi", "ES123456789", 91234)
print("Información de la cuenta bancaria: ")
print(c1)

print("\n"*2)
c1.ingreso(-1)
c1.ingreso(50)
print("\n"*2)
c1.retiro(9999999999)
c1.retiro(70)

print("\n"*2)
c1.modificar_tasa_interes(0.3)
print(f"La tasa de interes es: {c1.aplica_tasa_interes()}")

c1.modificar_tipo("c Ahorros")

print("\n"*2, c1)