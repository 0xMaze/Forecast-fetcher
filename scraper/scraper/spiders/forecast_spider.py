from sqlalchemy.orm import Session

import scrapy

from app.db.session import SessionLocal

from app import crud
from app import schemas


class ForecastSpider(scrapy.Spider):
    name = "weather_spider"
    allowed_domains = ["openweathermap.org"]
    start_urls = []

    # get the list of all cities from the database and extract their web_id field
    # a sample url: https://openweathermap.org/city/625144
    # the web_id is the last part of the url
    # loop through the list of cities and parse the data for each city
    def start_requests(self):
        cities = crud.city.get_all(db=SessionLocal())
        for city in cities:
            self.start_urls.append(
                f"https://openweathermap.org/data/2.5/find?q={city.name}&appid=439d4b804bc8187953eb36d2a8c26a02&units=metric"
            )
        for url in self.start_urls:
            yield scrapy.Request(url=url, callback=self.parse)

    # parse the data from the response using the _extract_data method
    def parse(self, response):
        weather_data = self._extract_data(response.json())
        # convert the data to WeatherCreate object
        item_in = schemas.WeatherCreate(
            temperature=weather_data["temperature"],
            pressure=weather_data["pressure"],
            wind_speed=weather_data["wind_speed"],
            city_id=weather_data["city_id"],
        )
        # create a new weather record
        weather = crud.weather.create_with_city(
            db=SessionLocal(), obj_in=item_in, city_id=weather_data["city_id"]
        )

    @staticmethod
    def _extract_data(weather_data: dict) -> dict:
        """
        Extracts relevant data from the `weather_data` dictionary and returns it as a new dictionary.

        :param weather_data: A dictionary containing weather data from OpenWeatherMap API.
        :type weather_data: dict
        :return: A dictionary with the extracted data including city name, temperature, pressure and wind speed.
        :rtype: dict
        """
        data = weather_data["list"][0]

        city_id = data["id"]
        temperature = data["main"]["temp"]
        pressure = data["main"]["pressure"]
        wind_speed = data["wind"]["speed"]

        return {
            "city_id": city_id,
            "temperature": temperature,
            "pressure": pressure,
            "wind_speed": wind_speed,
        }
