import sys
import os
from datetime import date

# Añadir el directorio actual al path para poder importar 'app'
sys.path.append(os.getcwd())

from app.database import SessionLocal, engine
from app import models

def seed():
    db = SessionLocal()
    try:
        # Limpiar datos antiguos (opcional, pero útil para pruebas limpias)
        # db.query(models.Evento).delete()
        # db.query(models.Recinto).delete()
        # db.commit()

        print("Creando recintos...")
        recintos = [
            models.Recinto(nombre="WiZink Center", ciudad="Madrid", capacidad=17453),
            models.Recinto(nombre="Palau Sant Jordi", ciudad="Barcelona", capacidad=17960),
            models.Recinto(nombre="Estadio Santiago Bernabéu", ciudad="Madrid", capacidad=81044),
            models.Recinto(nombre="Auditorio Rocío Jurado", ciudad="Sevilla", capacidad=8000),
        ]
        db.add_all(recintos)
        db.commit()

        # Refrescar para obtener IDs
        for r in recintos:
            db.refresh(r)
        
        print("Creando eventos...")
        eventos = [
            models.Evento(nombre="Concierto Rock", fecha=date(2026, 5, 20), precio=50.0, recinto_id=recintos[0].id),
            models.Evento(nombre="Festival de Jazz", fecha=date(2026, 6, 15), precio=35.0, recinto_id=recintos[1].id),
            models.Evento(nombre="Partido Benéfico", fecha=date(2026, 7, 10), precio=20.0, recinto_id=recintos[2].id),
            models.Evento(nombre="Ópera al aire libre", fecha=date(2026, 8, 5), precio=45.0, recinto_id=recintos[3].id),
            models.Evento(nombre="Monólogo Comedia", fecha=date(2026, 9, 12), precio=15.0, recinto_id=recintos[0].id),
        ]
        db.add_all(eventos)
        db.commit()
        
        print("¡Datos de prueba insertados con éxito!")
    except Exception as e:
        print(f"Error al insertar datos: {e}")
        db.rollback()
    finally:
        db.close()

if __name__ == "__main__":
    seed()
