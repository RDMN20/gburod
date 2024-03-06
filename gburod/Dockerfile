FROM python:3.11

WORKDIR /app

RUN python -m pip install --upgrade pip
COPY requirements.txt .
RUN pip install -r requirements.txt --no-cache-dir --verbose

COPY /gburod_site .

CMD ["gunicorn", "gburod_site.wsgi:application", "--bind", "0:8000" ]
