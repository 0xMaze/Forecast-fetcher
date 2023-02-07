import scrapy
from sqlalchemy.orm import Session
from app.api.deps import get_db
import crud


class ForecastSpider(scrapy.Spider):
    name = "weather_spider"
    start_urls = []

    # connect to the database to write the data
    def __init__(self, db: Session, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.db = get_db()

    # get the list of all cities from the database and extract their web_id field
    # a sample url: https://openweathermap.org/city/625144
    # the web_id is the last part of the url
    # loop through the list of cities and parse the data for each city
    def start_requests(self):
        cities = crud.city.get_all(self.db)
        for city in cities:
            self.start_urls.append(
                f"https://openweathermap.org/city/{city.web_id}"
            )
        for url in self.start_urls:
            yield scrapy.Request(url=url, callback=self.parse)

    # parse the data from the response using the _extract_data method
    def parse(self, response):
        weather_data = self._extract_data(response)
        # write the data to the database
        crud.weather.create(self.db, weather_data)

    @staticmethod
    def _extract_data(weather_data: dict) -> dict:
        """
        Extracts relevant data from the `weather_data` dictionary and returns it as a new dictionary.

        :param weather_data: A dictionary containing weather data from OpenWeatherMap API.
        :type weather_data: dict
        :return: A dictionary with the extracted data including city name, temperature, pressure and wind speed.
        :rtype: dict
        """
        city = weather_data["name"]
        temperature = weather_data["main"]["temp"]
        pressure = weather_data["main"]["pressure"]
        wind_speed = weather_data["wind"]["speed"]

        return {
            "city": city,
            "temperature": temperature,
            "pressure": pressure,
            "wind_speed": wind_speed,
        }
