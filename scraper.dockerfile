FROM python:3.10

WORKDIR /app

COPY requirements.txt ./

RUN apt-get update && apt-get upgrade -y
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

COPY ./app /app

WORKDIR /app

ENV PYTHONPATH=/app
