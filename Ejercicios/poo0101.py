'''
Realizar una carga por teclado del nombre, edad y altura de dos personas. Mostrar por pantalla el nombre de la persona con mayor altura
'''

print("Datos de la primera persona")
nombre = input("Nombre: ")
edad = int(input("Edad: "))
altura = float(input("Altura: "))
print("Datos de la segunda persona")
nombre2 = input("Nombre: ")
edad2 = int(input("Edad: "))
altura2 = float(input("Altura: "))
if (altura > altura2):
    print("La persona más alta es ", nombre)
else:
    print(nombre2)
