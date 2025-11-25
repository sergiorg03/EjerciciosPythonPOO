'''
    Ejercicio 3029
'''
class MiDiccionario:
    
    def __init__(self):
        self.diccionario = {}
    
    def agregar_elemento(self, clave, valor):

        if clave not in self.diccionario:
            self.diccionario[clave] = valor
            print("Elemento creado... ")
        
    def borrar_elemento(self, clave, valor):
        if clave in self.diccionario:
            self.diccionario.pop(clave, None)
            print("Elemento borrado... ")

    def __iter__(self):
        return iter(self.diccionario)

    def __getitem__(self, clave):
        return self.diccionario[clave]

    def __setitem__(self,clave,valor):
        self.diccionario[clave] = valor

    def __len__(self):
        return len(self.diccionario)

    def __str__(self):
        return str(self.diccionario)

    def listar_claves(self):
        return list(self.diccionario.keys())

    def listar_elementos(self):
        return self.diccionario.items()

    def borrar_diccionario(self):
        self.diccionario.clear()

    def contiene_clave(self, clave):
        return clave in self.diccionario



## pruebas / casos de uso
## creación de una instancia
dicc_1 = MiDiccionario()
## llamada de métodos
dicc_1.agregar_elemento("fruta", "manzana")
dicc_1.agregar_elemento("vegetal", "zanahoria")
dicc_1.agregar_elemento("carne", "pavo")
print(dicc_1)
print("- "*20)
## creación de un iterador
iter_dicc1 = iter(dicc_1)
print(f"primera iteracion:", next(iter_dicc1))
print(f"segunda iteracion:", next(iter_dicc1))
print(f"- "*20)
print(f"El numero de elementos del diccionario es: ",
len(dicc_1))
print(f"Las claves del diccionario es: ", dicc_1.listar_claves())
print(f"Los valores del diccionario son: ", dicc_1.listar_elementos())
print(f"fruta esta el diccionario: {dicc_1.contiene_clave("fruta")}")
print(f"La lista de elementos del diccionario es: ", dicc_1.listar_elementos())
print(f"- "*20)
dicc_1.borrar_diccionario()
print("Despues de limpiar el diccionario", dicc_1)