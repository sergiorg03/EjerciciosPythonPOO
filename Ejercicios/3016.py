'''
    Ejercicio 3016
'''
class ManipuladoresArchivos:
    def __init__(self, nombreArchivo):
        self.nombreArchivo = nombreArchivo
        self.retorno = open(self.nombreArchivo, "r+")
        print(self.retorno.read())

    def __del__(self):
        self.retorno.close()
        del self

    def esribir_archivo(self, frase):
        self.retorno.write(frase)
        print(self.retorno.read())

ma = ManipuladoresArchivos("archivo.txt")
ma.esribir_archivo("Hola me llamo Sergio. ")
ma.__del__()