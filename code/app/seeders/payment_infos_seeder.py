from common import fake
import random

def seed_payment_infos(conn):
    with conn.cursor() as cur:
        cur.execute("SELECT id FROM users")
        users = cur.fetchall()

        cur.execute("SELECT id, require_requisites FROM payment_methods")
        payment_methods = cur.fetchall()

        payment_infos = []
        for user in users:
            for payment_method in payment_methods:
                if random.random() < 0.5:
                    continue
                requisites = fake.credit_card_number() if payment_method[1] else None
                payment_infos.append(
                    (user[0], payment_method[0], requisites)
                )

        cur.executemany(
            """
            INSERT INTO payment_infos (user_id, payment_method_id, requisites)
            VALUES (%s, %s, %s)
            """,
            payment_infos
        )
        conn.commit()
        print(f"Inserted {len(payment_infos)} payment infos into the database.")