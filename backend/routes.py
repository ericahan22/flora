import math
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

def fix_nan(val):
    if val is None:
        return None
    if isinstance(val, float) and math.isnan(val):
        return None
    return val

@router.get("/api/observations/")
def get_observations(db: Session=Depends(get_db)):
    results = db.query(models.FloraObservation).all()
    return [
        {
            "id": obs.id,
            "scientific_name": fix_nan(obs.scientific_name),
            "name": fix_nan(obs.name),
            "date": fix_nan(obs.date),
            "score": fix_nan(obs.score),
            "latitude": fix_nan(obs.latitude),
            "longitude": fix_nan(obs.longitude),
            "altitude": fix_nan(obs.altitude),
        }
        for obs in results
    ]
