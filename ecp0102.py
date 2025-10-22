'''
#División segura de dos números
a = int(input("Dividendo: "))
b = int(input("Divisor: "))
c = a/b if b!=0 else 0
print("La división es igual a " + str(c))

#Detección de números pares/impares
n = int(input("Introduce un número: "))
if n%2==0:
    print("Par")
else:
    print("Impar")
'''

#Incrementa o decrementa si es mayor/menor que 10
m = int(input("Introduce un número"))
m += -1 if m > 10 else (0 if m == 10 else 1)
print(m)
