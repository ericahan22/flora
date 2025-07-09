from sqlalchemy import Column, Integer, String, Float
from .database import Base

class FloraObservation(Base):
    __tablename__ = "flora_observations"
    id = Column(Integer, primary_key=True, autoincrement=True)
    scientific_name = Column(String)
    name = Column(String)
    date = Column(String)
    score = Column(Float)
    latitude = Column(Float)
    longitude = Column(Float)
    altitude = Column(Float)