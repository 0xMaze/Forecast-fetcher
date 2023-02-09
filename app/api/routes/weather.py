# 1. POST /weather/{city}, где {city} - название города на английском языке. Запись в БД города (перед записью необходимо проверить существование города на openweathermap.org).
# 2. GET /last_weather. Возвращает список существующих городов с последней записанной температурой. Если указать опциональный параметр ?search={search}, то выходной список городов фильтруется по частичному совпадению названия города со значением параметра.
# 3. GET /city_stats. Получает по заданному городу (передается query параметром) все данные за выбранный период, а также их средние значения за этот период.
from typing import List

import requests
from fastapi import APIRouter, Depends, HTTPException, Body
from sqlalchemy.orm import Session

from datetime import datetime

from app import schemas
from app import crud

from app.api import deps

router = APIRouter()


@router.post("/weather/{city}", response_model=schemas.City)
async def create_city(
    *,
    city: str,
    db: Session = Depends(deps.get_db),
) -> dict:
    """
    Create a new city
    """

    # check if city exists
    city_info = requests.get(
        f"https://openweathermap.org/data/2.5/find?q={city}&appid=439d4b804bc8187953eb36d2a8c26a02&units=metric"
    ).json()

    # if city not found, raise an exception
    if city_info["count"] == 0:
        raise HTTPException(status_code=404, detail="City not found")

    # convert city info to CityCreate object
    item_in = schemas.CityCreate(
        name=city_info["list"][0]["name"],
        web_id=city_info["list"][0]["id"],
    )

    # create a new city
    city = crud.city.create(db=db, obj_in=item_in)

    return city


@router.get("/last_weather", response_model=List[schemas.City])
async def get_last_weather_cities(
    *,
    db: Session = Depends(deps.get_db),
    search: str = None,
) -> List[dict]:
    """
    Get a list of cities with the last recorded temperature
    """
    cities = crud.city.get_latest_weather_cities(db=db, search=search)

    return cities


@router.get("/city_stats", response_model=List[schemas.Weather])
async def get_city_stats(
    *,
    db: Session = Depends(deps.get_db),
    city: str,
    start_date: datetime,
    end_date: datetime,
) -> List[dict]:
    """
    Get weather stats for a city in a given period
    """
    city_stats = crud.city.get_city_stats(
        db=db, city=city, start_date=start_date, end_date=end_date
    )

    return city_stats
