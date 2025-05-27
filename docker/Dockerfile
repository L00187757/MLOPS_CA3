FROM python:3.9-slim

WORKDIR /app
RUN apt-get update && \
    apt-get install -y --no-install-recommends gcc python3-dev && \
    rm -rf /var/lib/apt/lists/*

COPY app/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt


COPY app /app
COPY dataset/bmi.csv /app/dataset/bmi.csv

RUN python models/train.py

EXPOSE 5000

