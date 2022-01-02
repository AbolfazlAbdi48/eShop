FROM python:alpine

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBOFFRED 1

WORKDIR /src

COPY ./requirements.txt .
COPY ./src /src

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

CMD while ! python manage.py sqlflush > /dev/null 2>&1 ; do sleep 1 ; done && \
        python manage.py makemigrations --noinput && \
        python manage.py migrate --noinput && \
        gunicorn -b 0.0.0.0:8000 eShop.wsgi

CMD gunicorn -b 0.0.0.0:8000 eShop.wsgi