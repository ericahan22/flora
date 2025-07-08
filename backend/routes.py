from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from . import models, database

router = APIRouter()

def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/observations/")
def read_observations(skip: int=0, limit: int=10, db: Session=Depends(get_db)):
    return db.query(models.FloraObservation).offset(skip).limit(limit).all()