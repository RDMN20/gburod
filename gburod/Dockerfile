FROM python:3.7

RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

COPY requirements.txt /usr/src/app/
RUN pip install --no-cache-dir -r requirements.txt

COPY ./gburod_site/ /usr/src/app/

EXPOSE 8000

CMD python gburod/gburod_site/manage.py runserver 0.0.0.0:8000
