from typing import List

from sqlalchemy.orm import Session

from datetime import datetime

from app.crud.base import CRUDBase
from app.models import City, Weather

from app.schemas.city import CityCreate


class CRUDCity(CRUDBase[City, CityCreate]):
    def create(self, db: Session, *, obj_in: CityCreate) -> City:
        """
        Create a new city if it doesn't already exist
        """
        db_obj = self.get_by_name(db, name=obj_in.name)
        if db_obj:
            return db_obj

        return super().create(db, obj_in=obj_in)

    def get_latest_weather_cities(
        self, db: Session, *, search: str = None
    ) -> List[City]:
        """
        Get a list of cities with the last recorded temperature
        """
        query = (
            db.query(City).join(Weather).filter(Weather.temperature != None)
        )

        if search:
            query = query.filter(City.name.ilike(f"%{search}%"))

        return query.all()

    def get_city_stats(
        self,
        db: Session,
        *,
        city: str,
        start_date: datetime,
        end_date: datetime,
    ) -> List[Weather]:
        """
        Get a list of weather data for a given city in a specified period
        """
        query = (
            db.query(Weather)
            .join(City)
            .filter(City.name == city)
            .filter(Weather.time_stamp >= start_date)
            .filter(Weather.time_stamp <= end_date)
        )

        return query.all()


city = CRUDCity(City)
