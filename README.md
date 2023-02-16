# Scrapy framework parser

To run the application do the following:

- `git clone https://github.com/0xMaze/Forecast-fetcher.git`
- cd into the project directory, e.g: `cd /Forecast-fetcher`
- `docker-compose up -d`
- `docker-compose run app alembic upgrade head`

After that the application should be running on _localhost:8002._ In order to acces the Swagger UI go to _localhost:8002/docs._

To stop the application type: `docker-compose stop`

# Features overview:

- `POST /weather/{city}` endpoint allows to create a city instance in the database.
- `GET /last_weather` endpoint gets a list of cities with the last recorded temperature. When the `search` query parameter is specified, then the output list of cities is filtered by a partial match of the city name with the value of the parameter.
- `GET /city_stats` endpoint gets all the data for a given city (passed by the query parameter) for the selected period (the timestamp should be specified in ISO 8601 format, e.g: 2023-02-16T16:35:34.551Z. Visit [this](https://www.timestamp-converter.com/) website for easier conversion).

Weather data is fetched every minute for each city using the Scrapy framework.
