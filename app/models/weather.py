from sqlalchemy.orm import relationship
from typing import TYPE_CHECKING
import datetime

from sqlalchemy import Column, Integer, Float, ForeignKey, DateTime


from app.db.base_class import Base

if TYPE_CHECKING:
    from .city import City


class Weather(Base):
    id = Column(Integer, primary_key=True)
    temperature = Column(Float, nullable=False)
    pressure = Column(Float, nullable=False)
    wind_speed = Column(Float, nullable=False)
    time_stamp = Column(DateTime, default=datetime.datetime.utcnow)
    city_id = Column(Integer, ForeignKey("city.id"), nullable=False)
    city = relationship("City", back_populates="weather")
