from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
'''from app import schemas, crud
from app.deps import get_db
from app.database import Base, engine'''
from . import schemas, crud
from .deps import get_db
from .database import Base, engine

Base.metadata.create_all(bind=engine)

app = FastAPI(title="ScooterFlow API")

@app.get("/")
def root():
    return {"msg": "API funcionando"}


'''
    Zonas
'''

@app.post

'''
    Patinetes
'''