'''
    Ejercicio 3026
'''
import os

class GestorArchivos:

    def __init__(self, rutaDirectorio):
        self.rutaDirectorio = rutaDirectorio

        if not os.path.exists(self.rutaDirectorio):
            os.makedirs(self.rutaDirectorio)

    def listar(self):
        print(os.listdir(self.rutaDirectorio))

    def crear(self, archivo):
        ruta = os.path.join(self.rutaDirectorio, archivo)
        if not os.path.exists(ruta):
            with open((ruta), 'x') as f:
                f.write("")
            print(f"Archivo {ruta} creado. ")
        else:
            print("El archivo ya existe. ")
    
    def eliminar(self, archivo):
        ruta = os.path.join(self.rutaDirectorio, archivo)
        if os.path.exists(ruta):
            os.remove(ruta)
            print(f"Archivo {ruta} eliminado. ")
        else:
            print("El archivo no existe. ")
        
    def renombrar(self, nombre_viejo, nombre_nuevo):
        ruta = os.path.join(self.rutaDirectorio, nombre_viejo)
        archivoNuevo = os.path.join(self.rutaDirectorio, nombre_nuevo)
        if os.path.exists(ruta):
            os.rename(ruta, archivoNuevo)
            print(f"Archivo {ruta} renombrado. ")
        else:
            print("No existe el archivo a renombrar. ")

    def extension(archivo):
        return os.path.splitext(archivo)[1]

class GestorArchivosAudio(GestorArchivos):
    
    def __init__(self, rutaArchivo):
        super().__init__(rutaArchivo)
        self.extensiones_audio = ['.mp3', '.wav', '.flac']
    
    def listar(self):
        # Usamos rutaDirectorio que es la del padre
        archivos_audio = [file for file in os.listdir(self.rutaDirectorio) if os.path.splitext(file)[1].lower() in self.extensiones_audio]

        print("Los archivos de audio del directorio son: ")
        for f in archivos_audio:
            print(f)
        


print("Gestor de Archivos", "-"*25)
ruta = "DIRECTORIO_PRUEBA"
g = GestorArchivos(ruta)
g.crear("documento1_PRUEBA.txt")
g.crear("LaCancionDeMessi.mp3")

print("Listamos los archivos", "-"* 20)
g.listar()

print("Renombramos el archivo","-"*10)
g.renombrar("documento1_PRUEBA.txt", "SIUUUUUUU.txt")

print("Eliminamos el archivo","-"*10)
g.eliminar("laCancionDeMessi.mp3")

print(GestorArchivos.extension("SIUUUUUUU.txt"))

print("\nGestor de Archivos de Audio", "-"*25)
ga = GestorArchivosAudio(ruta)
ga.listar()