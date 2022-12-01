FROM python:3.10

RUN mkdir -p /usr/src/app

COPY requirements.txt /usr/src/app
RUN pip install -r /usr/src/app/requirements.txt

COPY . /usr/src/app
WORKDIR /usr/src/app

RUN python manage.py migrate

EXPOSE 80

ENTRYPOINT ["./docker-entrypoint.sh"]
CMD ["gunicorn", "--bind", "0.0.0.0:80", "--access-logfile", "-", "--error-logfile", "-", "config.wsgi"]
