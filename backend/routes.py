from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from backend import models, database

router = APIRouter()

def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/api/observations/")
def get_all_observations(db: Session=Depends(get_db)):
    return db.query(models.FloraObservation).all()