'''
Ej. 11. Define una lista que tenga 5 numeros. Suma los elementos y muestra el resultado de la suma.
       Define una lista que tenga 5 numeros. Suma los elementos y muestra el resultado de la suma.
'''
print("Ejercicio 11.")

lista = [2, 6, 23, 93, 19]

suma = sum(lista)

print(suma)

'''
EJ. 12. Dada la lista = [1000, 6000, 400, 23, 130, 400, 60, 2000] Cuenta cuantos elementos de la lista superan el valor de 100.
'''
print("Ejercicio 12.")
lista2 = [1000, 6000, 400, 23, 130, 400, 60, 2000]

contador = [+1 for x in lista2 if x > 100]

print(len(contador))

'''
Ej. 13. Dada la lista nombres = ["juan", "ana", "marcos", "carlos", "luis"]
        Cuenta cuantos tienen mas de 5 caracteres.
'''
print("Ejercicio 13.")
nombres = ["juan", "ana", "marcos", "carlos", "luis"]

contador2 = [n for n in nombres if len(n)>5]

print(len(contador2))

'''
Ej. 14. Dada la lista = [1000, 6000, 400, 23, 130, 400, 60, 2000] Identifica cual es el mayor y cual es el menor. Y la posición en la que se encuentran
'''
print("Ejercicio 14.")
lista3 = [1000, 6000, 400, 23, 130, 400, 60, 2000]

print(max(lista3), "y está en la posicion: ", lista3.index(max(lista3)))
print(min(lista3), "y está en la posicion: ", lista3.index(min(lista3)))


'''
Ej. Opcional. Muestra los que son más altos que el promedio.
'''
print("Ejercicio Opcional.")

promedio = (sum(lista3)/len(lista3))
print("El promedio es: ", promedio)

listaMayoresMedia = [x for x in lista3 if x > promedio]

print(listaMayoresMedia)