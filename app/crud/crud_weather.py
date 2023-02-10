from typing import List

from fastapi.encoders import jsonable_encoder
from sqlalchemy.orm import Session

from app.crud.base import CRUDBase
from app.models import Weather
from app.schemas.weather import WeatherCreate


class CRUDWeather(CRUDBase[Weather, WeatherCreate]):
    def create_with_city(
        self, db: Session, *, obj_in: WeatherCreate, city_id: int
    ) -> Weather:
        """
        Create a new weather record for a given city
        """
        obj_in_data = jsonable_encoder(obj_in)
        db_obj = Weather(**obj_in_data, city_id=city_id)
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj


weather = CRUDWeather(Weather)
