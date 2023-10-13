FROM python:3.11

RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

COPY requirements.txt /usr/src/app/
COPY .env /usr/src/app/
RUN pip install --no-cache-dir -r requirements.txt

COPY ./gburod_site /usr/src/app/

EXPOSE 8000

CMD ["gunicorn", "gburod_site.wsgi:application", "--bind", "0:8000" ]
