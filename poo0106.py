'''
Ingresar un email y comprobar si solo tiene un @
'''
'''
email=input("Ingrese un email: ")
cantidad=0
x=0
while x <len(email):
    if email[x]=="@":
        cantidad=cantidad+1
    x=x+1
if cantidad==1:
    print("Solo contiene un @")
else:
    print("Contiene más de un @")
'''

mail=input("Ingrese un email: ")
cantidad=mail.count("@")
if cantidad==1:
    print("Solo contiene un @")
else:
    print("Contiene más de un @")