import pandas as pd
from backend.models import Base
from backend.database import engine

df = pd.read_csv('data/flora_observations.csv')
Base.metadata.drop_all(engine)
Base.metadata.create_all(engine)

df = df.rename(columns={'scientific name': 'scientific_name'})
df[['scientific_name', 'name', 'date', 'score', 'latitude', 'longitude', 'altitude']].to_sql(
    'flora_observations',
    con=engine,
    if_exists='replace',
    index=False
)
