from faker import Faker
import psycopg
import os

fake = Faker("ru_RU")

def get_conn():
    dsn = os.environ.get("DSN")
    if not dsn:
        raise RuntimeError("DSN not set in environment variables")
    
    return psycopg.connect(dsn, autocommit=True)