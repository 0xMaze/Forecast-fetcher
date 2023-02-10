FROM python:3.10

WORKDIR /app

COPY requirements.txt ./

RUN apt-get update && apt-get upgrade -y

RUN pip install --upgrade pip

RUN pip install -r requirements.txt

RUN apt-get -y install cron

COPY ./app /app
WORKDIR /app

ENV PYTHONPATH=/app

COPY ./app/run_scraper.sh /run_scraper.sh

RUN chmod +x /run_scraper.sh

WORKDIR /app
