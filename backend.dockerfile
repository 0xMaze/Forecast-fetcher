FROM python:3.10

WORKDIR /app

COPY requirements.txt ./

RUN apt-get update && apt-get upgrade -y && apt-get install gcc

RUN pip install --upgrade pip

RUN pip install -r requirements.txt

COPY . .
