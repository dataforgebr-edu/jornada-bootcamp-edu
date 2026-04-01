from db import Base
from sqlalchemy import Column, DateTime, Integer, String
from sqlalchemy.sql import func


class Pokemon(Base):
    __tablename__ = "pokemons"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(50))
    type = Column(String(100))
    height = Column(Integer)
    weight = Column(Integer)
    created_at = Column(DateTime, default=func.now())
