FROM python:3.10-slim-bullseye

WORKDIR /graduate2

COPY ./requirements.txt /graduate2/

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

COPY ./graduate2 /graduate2/
