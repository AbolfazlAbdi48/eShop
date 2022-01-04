FROM python:alpine

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBOFFRED 1

WORKDIR /src

COPY ./requirements.txt .
COPY ./src /src

RUN apk add --no-cache jpeg-dev zlib-dev
RUN apk add --no-cache --virtual .build-deps build-base linux-headers

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

CMD gunicorn -b 0.0.0.0:8000 eShop.wsgi