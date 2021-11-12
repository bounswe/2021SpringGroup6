FROM python:3.7.11-slim-stretch

ENV PYTHONUNBUFFERED 1

WORKDIR /usr/src/


RUN pip install --upgrade pip
COPY ./requirements.txt .
RUN pip install -r requirements.txt


COPY . .