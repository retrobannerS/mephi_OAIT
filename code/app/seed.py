from seeders import *
from common import get_conn


def seed_all():
    with get_conn() as conn:
        seed_payment_methods(conn)
        seed_users(conn, 10000)
        seed_payment_infos(conn)

        seed_couriers(conn, 100)
        seed_menus(conn)
        seed_orders(conn, 50000, 100)

        seed_preference_categories(conn)
        seed_preferences(conn)
        seed_preferences_users(conn)

        seed_suppliers(conn, 20)
        seed_ingredients(conn)
        seed_ingredients_suppliers(conn)
        seed_dishes(conn)
        seed_dishes_ingredients(conn)
        seed_ingredients_preferences(conn)
        seed_dishes_menus(conn)