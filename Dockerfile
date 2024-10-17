FROM python:3.11-slim

WORKDIR /usr/src/app/weather

COPY requirements.txt /usr/src/app/weather

RUN pip install -r /usr/src/app/weather/requirements.txt

COPY . /usr/src/app/weather