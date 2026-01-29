'''
    Ejercicio 3036
'''
from collections import deque

class Cola:

    def __init__(self):
        self.cola = deque()

    def insertar(self, n):
        self.cola.append(n)

    def extraer(self):
        return self.cola.popleft() if self.cola else None

    def numeroElementos(self):
        return len(self.cola)

    def mostrar(self):
        print("Mostramos la cola: ")
        for i, val in enumerate(self.cola, 1):
            print(f"{i}: {val}")

# prueba
c1 = Cola()
c1.insertar(25)
c1.insertar(212)
c1.insertar(13)
c1.insertar(2)
c1.insertar(22)
c1.insertar(11)
c1.insertar(4)
c1.insertar(23)
c1.mostrar()
print("Número de elementos: ",c1.numeroElementos())
print("Extrae:", c1.extraer())
print("Extrae:", c1.extraer())
print("Extrae:", c1.extraer())
c1.mostrar()