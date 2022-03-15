FROM python:3.8

ENV PYTHONUNBUFFERED 1

WORKDIR /app

ADD . /app

COPY ./requirements /app/requirements

RUN pip install -r requirements


ENV SETTINGS='urlShortener.settings'

COPY . /app

