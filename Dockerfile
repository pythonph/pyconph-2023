FROM python:3.11-slim-buster

RUN mkdir -p /usr/src/app

COPY requirements.txt /usr/src/app
RUN pip install -r /usr/src/app/requirements.txt

COPY . /usr/src/app
WORKDIR /usr/src/app

RUN python manage.py migrate

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]