'''
    Ejercicio 3037
'''
class CuentaCorriente:

    # Apartado B: Atributo estático
    banco = "Banco"

    def __init__(self, DNI, nombre, saldo=0, gestor=None):
        self.DNI = DNI
        self.nombre = nombre
        self.saldo = saldo
        self.gestor = gestor

    def sacar_dinero(self, n):
        if n > 0 and self.saldo > 0:
            self.saldo -= n
            return f"Puede realizar una retirada de {n} euros.\nTiene {self.saldo} euros disponibles. "
        return f"No es posible retirar dinero. No dispone de saldo suficiente. "

    def ingresar_dinero(self, cantidad):
        if cantidad > 0:
            self.saldo += cantidad
            print(f"La cantidad de {cantidad} euros ha sido añadida correctamente a su saldo. ")
        else: 
            print("La cantidad a ingresar deberá de ser mayor a 0 euros. ")

    def mostrar_informacion(self):
        texto = f"El propietario de la cuenta corriente es {self.nombre}, con DNI {self.DNI} y dispone de un saldo de {self.saldo} euros. \n"
        texto += f"{self.gestor}" if self.gestor else ""
        return texto

class Gestor:
    def __init__(self, nombre, telefono, importe_max=10_000):
        self.nombre = nombre
        self.telefono = telefono
        self.importe_max = importe_max

    def __str__(self):
        return f"Su gestor de la cuenta es {self.nombre}, su telefono de contacto es {self.telefono} y el importe máximo por operaciones autorizado es de {self.importe_max} euros. "


gestor1 = Gestor("Ana", "654321987")
cuenta1 = CuentaCorriente("12345678A", "Sergio", 5000, gestor1)
cuenta2 = CuentaCorriente("87654321B", "Luis")

print(cuenta1.mostrar_informacion())
print(cuenta2.mostrar_informacion())

print(cuenta1.sacar_dinero(1000))
cuenta2.ingresar_dinero(200)
print(cuenta2.mostrar_informacion())