FROM python:alpine

WORKDIR /app

RUN pip install psycopg psycopg-binary faker

COPY ./app .

CMD [ "python", "./main.py" ]