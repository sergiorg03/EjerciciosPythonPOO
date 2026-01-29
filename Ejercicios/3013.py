'''
  Ejercicio 3013
'''
class Vector4D:
    def __init__(self, u, v, x, y):
        self.u = u
        self.v = v
        self.x = x
        self.y = y
    
    def __add__(self, vector):
        return (self.u + vector.u, self.v + vector.v, self.x + vector.x, self.y + vector.y)

    def __sub__(self, vector):
        return (self.u - vector.u, self.v - vector.v, self.x - vector.x, self.y - vector.y)


    def __mul__(self, vector):
        return ((self.u * vector.u) + (self.v * vector.v) + (self.x * vector.x) + (self.y * vector.y))
        

    def __truediv__(self, escalar):
        return (self.u / escalar, self.v / escalar, self.x / escalar, self.y / escalar)

v = Vector4D(1, 4, 5, 9)
v2 = Vector4D(5, 73, 8, 1)
print(f"La suma de los vectores {v.u, v.v, v.x, v.y} + {v2.u, v2.v, v2.x, v2.y} es: {v.__add__(v2)}.")
print(f"La resta de los vectores {v.u, v.v, v.x, v.y} - {v2.u, v2.v, v2.x, v2.y} es: {v.__sub__(v2)}. ")
print(f"La multiplicación de los vectores {v.u, v.v, v.x, v.y} x {v2.u, v2.v, v2.x, v2.y} es: {v.__mul__(v2)}. ")
escalar = 3
print(f"La división del vector {v.u, v.v, v.x, v.y} entre el escalar {escalar} es: {v.__truediv__(escalar)}")