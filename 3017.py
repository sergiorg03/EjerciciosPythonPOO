'''
    Ejercicio 3017
'''
class MiCadena:

    def __init__(self, variable_str):
        self.cadena = variable_str

    def __add__(self, cadena):
        self.cadena += '| ' + cadena

    def __len__(self):
        return len(self.cadena.replace(" ",""))

    def __str__(self):
        print(self.cadena)

    def __contains__(self, subcadena):
        return self.cadena.__contains__(subcadena)

m = MiCadena("Hola me llamo sergio y esto es un ejemplo de prueba. ")
m.__add__("Añadido")
print(f"La longitud de la cadena sin espacios es: {m.__len__()} .")
m.__str__()
subcadena = "ser"
print(f"La cadena original contiene la subcadena {subcadena}: {m.__contains__(subcadena)}")