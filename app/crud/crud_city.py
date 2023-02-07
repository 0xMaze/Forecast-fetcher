from typing import List

from sqlalchemy.orm import Session

from datetime import datetime

from crud.base import CRUDBase
from models import City, Weather

from schemas.city import CityCreate

# get_latest_weather_cities Возвращает список существующих городов с последней записанной температурой (т.е. если температура не равна None). Если указать опциональный параметр ?search={search}, то выходной список городов фильтруется по частичному совпадению названия города со значением параметра.


class CRUDCity(CRUDBase[City, CityCreate]):
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
            .filter(Weather.date >= start_date)
            .filter(Weather.date <= end_date)
        )

        return query.all()


city = CRUDCity(City)
