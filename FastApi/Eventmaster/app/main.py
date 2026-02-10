from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from app import schemas, crud
from app.deps import get_db
from app.database import Base, engine

Base.metadata.create_all(bind=engine)

app = FastAPI(title="EventMaster API")

@app.get("/")
def root():
    return {"msg": "API funcionando"}


'''
    Recintos
'''

@app.post("/recintos/", response_model=schemas.RecintoResponse)
def crear_recinto(recinto: schemas.RecintoCreate, db: Session = Depends(get_db)):
    return crud.crear_recinto(db, recinto)


@app.get("/recintos/", response_model=list[schemas.RecintoResponse])
def listar_recintos(db: Session = Depends(get_db)):
    return crud.listar_recintos(db)


'''
    Eventos
'''

@app.post("/eventos/", response_model=schemas.EventoResponse)
def crear_evento(evento: schemas.EventoCreate, db: Session = Depends(get_db)):
    return crud.crear_evento(db, evento)


@app.get("/eventos/", response_model=list[schemas.EventoResponse])
def listar_eventos(ciudad: str | None = None, db: Session = Depends(get_db)):
    return crud.listar_eventos(db, ciudad)


@app.patch("/eventos/{id}/comprar")
def comprar_evento(id: int, cantidad: int, db: Session = Depends(get_db)):
    return crud.comprar_tickets(db, id, cantidad)
