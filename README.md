# Scrapy framework parser

To run the application do the following:

- `git clone https://github.com/0xMaze/Forecast-fetcher.git`
- cd into the project directory, e.g: `cd Forecast-fetcher/`
- `docker-compose up -d`
- `docker-compose run app alembic upgrade head`

After that the application should be running on _localhost:8002._ In order to acces the Swagger UI go to _localhost:8002/docs._

To stop the application type: `docker-compose stop`

# Features overview:

- `POST /weather/{city}` endpoint allows to create a city instance in the database.
- `GET /last_weather` endpoint gets a list of cities with the last recorded temperature. When the `search` query parameter is specified, then the output list of cities is filtered by a partial match of the city name with the value of the parameter.
- `GET /city_stats` endpoint gets all the data for a given city (passed by the query parameter) for the selected period (the timestamp should be specified in ISO 8601 format, e.g: 2023-02-16T16:35:34.551Z. Visit [this](https://www.timestamp-converter.com/) website for easier conversion).

Weather data is fetched every minute for each city using the Scrapy framework. In order to use the Scrapy parser at least one city should be added to the database, otherwise no data will be parsed.

# Database choice:

For this task I chose a PostgreSQL database for the following reasons:

1. ACID compliance: PostgreSQL is fully ACID compliant, meaning that it ensures data consistency and reliability in the face of errors, crashes, and hardware failures.
2. Scalability: PostgreSQL can handle a large amount of data and is known for its scalability. It can be used to handle large data sets, and it can easily be scaled horizontally by adding more nodes to the cluster.
3. Extensibility: PostgreSQL is designed to be extensible, meaning that users can easily add new data types, operators, and functions to meet their specific needs.
4. Support for complex queries: PostgreSQL has powerful support for complex queries, including subqueries, window functions, and common table expressions.
5. Open source: PostgreSQL is open source, meaning that it is free to use and has a large and active community of developers, which ensures its continued development and support.

Overall, PostgreSQL is a great choice for projects that require a reliable and scalable relational database management system.
