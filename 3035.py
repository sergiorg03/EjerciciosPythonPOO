'''
    Ejercicio 3035
'''
class Maquinista:
    def __init__(self, nombre, DNI, sueldo, rango):
        self.nombre = nombre
        self.DNI = DNI
        self.sueldo = sueldo
        self.rango = rango

    def __str__(self):
        return f"Maquinista: {self.nombre} {self.DNI} {self.sueldo}"

class Mecanico:
    
    def __init__(self, nombre, telf, especialidad):
        self.nombre = nombre
        self.telf = telf
        self.especialidad = especialidad

    def __str__(self):

        return f"Mecánico: {self.nombre} {self.especialidad}"
    
class JefeEstacion:

    def __init__(self, nombre, DNI, fecha_antiguedad):
        self.nombre = nombre
        self.DNI = DNI
        self.fecha_antiguedad = fecha_antiguedad

    def __str__(self):

        return f"Jefe Estación: {self.nombre} {self.DNI} {self.fecha_antiguedad}"

class Vagones:

    def __init__(self, numero_identificador, max_carga, carga_actual, tipo_mercancia):

        self.numero_identificador = numero_identificador
        self.max_carga = max_carga
        self.carga_actual = carga_actual
        self.tipo_mercancia = tipo_mercancia

    def __str__(self):
        return f"\tVagon: {self.numero_identificador}. \n\t\t\tCarga maxima: {self.max_carga} Kgs. \n\t\t\tCarga actual: {self.carga_actual} kgs. \n\t\t\tMercancia: {self.tipo_mercancia}."
    
class Locomotora:

    def __init__(self, matricula, potencia, antiguedad, mecanico: Mecanico):
        self.matricula = matricula
        self.potencia = potencia
        self.antiguedad = antiguedad
        self.mecanico = mecanico

    def __str__(self):
        return f"Locomotora: {self.matricula}"

class Tren: 
    
    def __init__(self, locomotora: Locomotora, maquinista: Maquinista):
        self.locomotora = locomotora
        self.maquinista = maquinista
        self.vagones = []

    def enganchaVagon(self, identificador, carga_actual, mercancia):
        if len(self.vagones) > 5:
            print(f"Se ha alcanzado el máximo de vagones disponibles por tren. ")
            return

        self.vagones.append(Vagones(numero_identificador=identificador, carga_actual=carga_actual, tipo_mercancia= mercancia, max_carga=1000))

    def __str__(self):
        texto = f"- Componentes del tren: \n\t{self.locomotora}. \n\t- Maquinista: {self.maquinista}. \n\t- Vagones:\n\t"
        for v in list(self.vagones):
            texto += f"{str(v)}\n\t"
            
        return texto

# Pruebas 
mecanico1 = Mecanico("Pepe", "658878787", "MOTOR")
maquinista1 = Maquinista("Manuel", "45567678F", 3400, "Secundario")
jefeEstacion1 = JefeEstacion("Sergio", "34345345f", "25/12/2005")
locomotora1 = Locomotora("f456", 240, 2002, mecanico1)
tren1 = Tren(locomotora1, maquinista1)
tren1.enganchaVagon(567, 450, "Plátanos")
tren1.enganchaVagon(345, 345, "Plátanos")
tren1.enganchaVagon(567, 200, "Tomates")
tren1.enganchaVagon(567, 100, "Sandias")
tren1.enganchaVagon(567, 156, "Peras")
tren1.enganchaVagon(567, 345, "Plátanos")
print(mecanico1)
print(maquinista1)
print(jefeEstacion1)
print(tren1)