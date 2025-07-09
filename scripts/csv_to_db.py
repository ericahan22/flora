import pandas as pd
from backend.models import Base, FloraObservation
from backend.database import engine, SessionLocal

def safe_float(val):
    try:
        if pd.isna(val) or val == '':
            return None
        return float(val)
    except Exception:
        return None

df = pd.read_csv('data/flora_observations.csv')
df = df.rename(columns={'scientific name': 'scientific_name'})
df = df[['scientific_name', 'name', 'date', 'score', 'latitude', 'longitude', 'altitude']]

Base.metadata.drop_all(engine)
Base.metadata.create_all(engine)

# Insert rows using SQLAlchemy ORM
session = SessionLocal()
for _, row in df.iterrows():
    obs = FloraObservation(
        scientific_name=row.get('scientific_name'),
        name=row.get('name'),
        date=row.get('date'),
        score=safe_float(row.get('score')),
        latitude=safe_float(row.get('latitude')),
        longitude=safe_float(row.get('longitude')),
        altitude=safe_float(row.get('altitude'))
    )
    session.add(obs)
session.commit()
session.close()
