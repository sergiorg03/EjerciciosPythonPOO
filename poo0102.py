'''
Realizar la carga de dos nombres por teclado. Mostrar cual de los dos es mayor alfabeticamente o si son iguales
'''

n1 = input("Primer nombre: ")
n2 = input("Segundo nombre: ")
if (n1 > n2):
    print(n1, "es mayor que ", n2)
elif (n2 > n1):
    print(n2, "es mayor que ", n1)
else:
    print(n1, "es igual a ", n2)