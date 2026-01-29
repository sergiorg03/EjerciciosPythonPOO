'''
    Ejercicio 3012
'''

class Video:

    def __init__(self, titulo, duracion, categoria):
        self.titulo = titulo
        self.duracion = duracion
        self.categoria = categoria

    def mirar_video(self):
        print("Estas viendo el video. ")

    def detener_video(self):
        print("Has detenido el video. ")

class Audio:
    
    def __init__(self, titulo, nombreArtista):
        self.titulo = titulo
        self.nombreArtista = nombreArtista

    def escuchar_audio(self):
        print("Estas escuchando el audio. ")
    
    def detener_audio(self):
        print("Has detenido el audio. ")

class Media(Video, Audio):
    
    def __init__(self, titulo, duracion, categoria, nombreArtista):
        Video.__init__(self, titulo, duracion, categoria)
        Audio.__init__(self, titulo, nombreArtista)

m1 = Media("Concierto Live", "60", "Trap", "Bad Bunny")
m1.mirar_video()
m1.escuchar_audio()
m1.detener_video()  
m1.detener_audio()
