from common import fake
import datetime

def generate_courier_name():
    first_name = fake.first_name_male()
    middle_name = fake.middle_name_male()
    last_name = fake.last_name_male()
    return first_name, middle_name, last_name


def generate_birth_date(min_age=18, max_age=60):
    today = datetime.date.today()
    start_date = today.replace(year=today.year - max_age)
    end_date = today.replace(year=today.year - min_age)
    return fake.date_between(start_date=start_date, end_date=end_date)

def seed_couriers(conn, n=50):
    with conn.cursor() as cur:
        for _ in range(n):
            first_name, middle_name, last_name = generate_courier_name()
            birth_date = generate_birth_date()

            cur.execute(
                """
                INSERT INTO couriers (first_name, middle_name, last_name, birth_date)
                VALUES (%s, %s, %s, %s)
                """,
                (first_name, middle_name, last_name, birth_date),
            )
        conn.commit()
        print(f"Inserted {n} couriers into the database.")