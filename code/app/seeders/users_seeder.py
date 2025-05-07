from common import fake
import datetime
import random

def generate_phone_number():
    """Форматирует номер телефона в виде 10 цифр без кода страны."""
    return fake.numerify("9#########")


def generate_name_by_gender(gender):
    """Генерация имени, отчества и фамилии в зависимости от пола."""
    if gender == "male":
        first_name = fake.first_name_male()
        middle_name = fake.middle_name_male()
        last_name = fake.last_name_male()
    else:
        first_name = fake.first_name_female()
        middle_name = fake.middle_name_female()
        last_name = fake.last_name_female()
    return first_name, middle_name, last_name

def generate_birth_date(min_age=18, max_age=80):
    """Генерация даты рождения в диапазоне от min_age до max_age лет назад."""
    today = datetime.date.today()
    start_date = today.replace(year=today.year - max_age)
    end_date = today.replace(year=today.year - min_age)
    return fake.date_between(start_date=start_date, end_date=end_date)

def seed_users(conn, n=50):
    with conn.cursor() as cur:
        for _ in range(n):
            sex = random.choice(["male", "female"])
            first_name, middle_name, last_name = generate_name_by_gender(sex)

            cur.execute(
                """
                INSERT INTO users (first_name, middle_name, last_name, sex, birth_date, phone_number, address, bonuses)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
                """,
                (
                    first_name,
                    middle_name,
                    last_name,
                    sex,
                    generate_birth_date(),
                    generate_phone_number(),
                    fake.street_address() if random.random() < 0.3 else None,
                    0,
                ),
            )

        conn.commit()
        print(f"Inserted {n} users into the database.")
        cur.execute("SELECT id FROM users")
        all_users = cur.fetchall()
        for user_id in all_users:
            if random.random() < 0.3:
                cur.execute(
                    """
                    UPDATE users
                    SET invited_by_id = %s
                    WHERE id = %s
                    """,
                    (random.choice(all_users)[0], user_id[0]),
                )
        conn.commit()
        print("Updated invited_by_id for some users.")