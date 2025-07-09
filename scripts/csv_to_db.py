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
float_cols = ['score', 'latitude', 'longitude', 'altitude']
for col in float_cols:
    df[col] = df[col].apply(safe_float)

print(df.head(10))
print(df.dtypes)
Base.metadata.drop_all(engine)
Base.metadata.create_all(engine)

# Insert rows using SQLAlchemy ORM
session = SessionLocal()
for idx, row in df.iterrows():
    float_prob = False
    for col in ['score', 'latitude', 'longitude', 'altitude']:
        val = row[col]
        if val is not None and not isinstance(val, float):
            print(f"Skipping row {idx}: {col} has invalid value {val} (type {type(val)})")
            float_prob = True
            break
    if float_prob:
        continue
    for col in ['scientific_name', 'date']:
        val = row[col]
        if not isinstance(val, str):
            print(f"Skipping row {idx}: {col} has invalid value {val} (type {type(val)})")
            break
    else:
        obs = FloraObservation(
            scientific_name=row['scientific_name'],
            name=row['name'] if isinstance(row['name'], str) else None,
            date=row['date'],
            score=row['score'],
            latitude=row['latitude'],
            longitude=row['longitude'],
            altitude=row['altitude']
        )
        session.add(obs)
session.commit()
session.close()
