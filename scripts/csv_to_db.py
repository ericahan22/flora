import pandas as pd
from app.models import Base
from app.database import engine

df = pd.read_csv('flora_observations.csv')
Base.metadata.drop_all(engine)
Base.metadata.create_all(engine)

df = df.rename(columns={'scientific name': 'scientific_name'})
df[['scientific_name', 'name', 'date', 'score', 'latitude', 'longitude', 'altitude']].to_sql(
    'flora_observations',
    con=engine,
    if_exists='replace',
    index=False
)
