'''
Un centro educativo necesita distribuir de forma aleatoria a los alumnos entre los grupos disponibles.
Tenemos lista que es una lista de nombres con el nombre de todos los alumnos del centro, n es el número de grupos que queremos tener.
Diseña la función repartoAlumnos (lista, n) que retorna una lista de listas, cada una de las cuales corresponde a un grupo.
Ejemplo:
➢ lista = ['a1', 'a2', 'a3', ..., 'a49', 'a50']
➢ n = 5
'''

import random as r

lista = [f"a{x}" for x in range(1, 50)]

n = int(input("Introduce el número de grupos en los que desea repartir a los alumnos: "))

def repartirAlumnos(listaDeAlumnos: list, n: int):
    personasPorLista = len(listaDeAlumnos)/n
    listasTotales = {}

    for i in range(n):
        listas = []

        for x in range(int(personasPorLista)):
            randomNum = r.randint(0, len(listaDeAlumnos)-1)
            listas.append(listaDeAlumnos[randomNum])
            listaDeAlumnos.pop(randomNum)

        listasTotales[i] = listas

    return listasTotales

# print(repartirAlumnos(lista, n))

listaFinal = repartirAlumnos(lista, n)

#Mostramos la lista
for i in listaFinal:
    print(f"Lista {i+1}: {listaFinal[i]}")