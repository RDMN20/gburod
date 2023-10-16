FROM python:3.11

WORKDIR /app

COPY requirements.txt .

RUN python -m pip install --upgrade pip
RUN pip install -r requirements.txt --no-cache-dir

COPY /gburod_site .

CMD ["gunicorn", "gburod_site.wsgi:application", "--bind", "0:8000" ]
