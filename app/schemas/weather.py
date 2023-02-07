from pydantic import BaseModel
from typing import Optional
import datetime


# Shared properties
class WeatherBase(BaseModel):
    temperature: float
    pressure: float
    wind_speed: float


# Properties to receive on item creation
class WeatherCreate(WeatherBase):
    pass


# Properties shared by models stored in DB
class WeatherInDBBase(WeatherBase):
    id: int
    time_stamp: datetime.datetime
    city_id: int

    class Config:
        orm_mode = True


# Properties to return to client
class Weather(WeatherInDBBase):
    pass
