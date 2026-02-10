from fastapi import HTTPException
from sqlalchemy.orm import Session
from app import models

'''
    Recintos
'''

def crear_recinto(db: Session, recinto):
    nuevo = models.Recinto(**recinto.dict())
    db.add(nuevo)
    db.commit()
    db.refresh(nuevo)
    return nuevo


def listar_recintos(db: Session):
    return db.query(models.Recinto).all()


'''
    Eventos
'''

def crear_evento(db: Session, evento):
    if evento.precio < 0:
        raise HTTPException(400, "El precio no puede ser negativo")

    nuevo = models.Evento(**evento.dict())
    db.add(nuevo)
    db.commit()
    db.refresh(nuevo)
    return nuevo


def listar_eventos(db: Session, ciudad: str | None = None):
    query = db.query(models.Evento).join(models.Recinto)

    if ciudad:
        query = query.filter(models.Recinto.ciudad.ilike(f"%{ciudad}%"))

    return query.all()


def comprar_tickets(db: Session, evento_id: int, cantidad: int):
    evento = db.query(models.Evento).get(evento_id)

    if not evento:
        raise HTTPException(404, "Evento no encontrado")

    if evento.tickets_vendidos + cantidad > evento.recinto.capacidad:
        raise HTTPException(400, "Aforo insuficiente en el recinto")

    evento.tickets_vendidos += cantidad
    db.commit()
    db.refresh(evento)
    return evento
