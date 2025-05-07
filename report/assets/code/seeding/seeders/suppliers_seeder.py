from common import fake
import random

def seed_suppliers(conn, n=10):
    with conn.cursor() as cur:
        for _ in range(n):
            title = fake.company()
            productivity = random.randint(1, 200)

            cur.execute(
                """
                INSERT INTO suppliers (title, productivity)
                VALUES (%s, %s)
                """,
                (title, productivity),
            )
        conn.commit()
        print(f"Inserted {n} suppliers into the database.")