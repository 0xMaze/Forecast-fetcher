from typing import TYPE_CHECKING

from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, String

from app.db.base_class import Base

if TYPE_CHECKING:
    from .weather import Weather


class City(Base):
    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False, unique=True)
    web_id = Column(Integer, nullable=False, unique=True)
    weather = relationship("Weather", back_populates="city")
