from common import fake
import random
import datetime

def generate_order_created_time(duration):
    now = datetime.datetime.now()
    start_time = now - datetime.timedelta(days=duration)
    return fake.date_time_between(start_date=start_time, end_date=now)

def generate_order_status(created_time):
    now = datetime.datetime.now()
    if now - created_time <= datetime.timedelta(days=1):
        status_weights = {
            'new': 0.5,
            'in_delivery': 0.5,
        }
        status = random.choices(
            list(status_weights.keys()), list(status_weights.values()), k=1
        )[0]
    elif datetime.timedelta(days=1) < now - created_time <= datetime.timedelta(days=3):
        status_weights = {'in_delivery': 0.1, 'delivered': 0.9}
        status = random.choices(
            list(status_weights.keys()), list(status_weights.values()), k=1
        )[0]
    else:
        status = 'delivered'

    if status == 'delivered' and random.random() < 0.05:
        status = 'returned'

    if random.random() < 0.05:
        status = 'canceled'

    return status

def seed_orders(conn, n=100, duration=30):
    with conn.cursor() as cur:
        cur.execute("SELECT id FROM users")
        users = cur.fetchall()

        cur.execute("SELECT id FROM menus")
        menus = cur.fetchall()

        cur.execute("SELECT id FROM couriers")
        couriers = cur.fetchall()

        cur.execute("SELECT id FROM payment_infos WHERE user_id IN (SELECT id FROM users)")
        payment_infos = cur.fetchall()

        orders = []
        for _ in range(n):
            user = random.choice(users)
            menu = random.choice(menus)
            courier = random.choice(couriers)
            payment_info = random.choice(payment_infos)
            created_at = generate_order_created_time(duration)

            order = (
                user[0],
                menu[0],
                created_at,
                generate_order_status(created_at),
                courier[0],
                payment_info[0],
            )
            orders.append(order)

        cur.executemany(
            """
            INSERT INTO orders (user_id, menu_id, created_at, status, courier_id, payment_info_id)
            VALUES (%s, %s, %s, %s, %s, %s)
            """,
            orders,
        )
        conn.commit()
        print(f"Inserted {len(orders)} orders into the database.")

        # Update user bonuses
        for order in orders:
            user_id = order[0]
            menu_id = order[1]
            cur.execute(
                """
                UPDATE users
                SET bonuses = bonuses + (SELECT cost FROM menus WHERE id = %s) * 0.05
                WHERE id = %s
                """,
                (menu_id, user_id),
            )
        conn.commit()
        print("Updated user bonuses based on orders.")