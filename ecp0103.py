# for i in range(0,5):
#     print(i)
# for c in "Python":
#     print(c)


from typing import Iterable

# #Verificación de iterabilidad
# v = range(0,5)
# print(isinstance(v, Iterable))
# c = "Cadena de texto"
# print(isinstance(c, Iterable))
# l = [1, 3, 5, 7, 9]
# print(isinstance(l, Iterable))
# n = 11
# print(isinstance(n, Iterable))

#Iteradores
listaIterable = [1, 3, 5, 7, 9, 11]
iterador = iter(listaIterable)
# print(listaIterable)
# print(iterador)
# print(type(listaIterable))
# print(type(iterador))
# print(next(iterador))
# print(next(iterador))
# print(next(iterador))
# print(type(iterador))
# print(next(iterador))
# print(next(iterador))
# print(next(iterador))

print("Fuera del bucle", next(iterador))

for n in iterador:
    print(n)
# StopIteration
# print(next(iterador))

iter01 = iter(listaIterable)
iter02 = iter(listaIterable)
print("Iterador 01 -> ", next(iter01))
print("Iterador 02 -> ", next(iter02))
print("Iterador 01 -> ", next(iter01))
print("Iterador 02 -> ", next(iter02))