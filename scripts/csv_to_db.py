import pandas as pd
from backend.models import Base, FloraObservation
from backend.database import engine, SessionLocal

df = pd.read_csv('data/flora_observations.csv')
df = df.rename(columns={'scientific name': 'scientific_name'})
Base.metadata.drop_all(engine)
Base.metadata.create_all(engine)

# Insert rows using SQLAlchemy ORM
session = SessionLocal()
for _, row in df.iterrows():
    obs = FloraObservation(
        scientific_name=row.get('scientific_name'),
        name=row.get('name'),
        date=row.get('date'),
        score=row.get('score'),
        latitude=row.get('latitude'),
        longitude=row.get('longitude'),
        altitude=row.get('altitude')
    )
    session.add(obs)
session.commit()
session.close()
