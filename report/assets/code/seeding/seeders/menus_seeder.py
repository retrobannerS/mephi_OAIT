def seed_menus(conn):
    menus = [
        {
            "title": "Похудение",
            "cost": 700,
            "count_dishes": 3,
            "colorfulness": 1000,
        },
        {
            "title": "Баланс",
            "cost": 850,
            "count_dishes": 4,
            "colorfulness": 1500,
        },
        {
            "title": "Набор",
            "cost": 1000,
            "count_dishes": 5,
            "colorfulness": 2000,
        },
    ]

    with conn.cursor() as cur:
        for menu in menus:
            cur.execute(
                """
                INSERT INTO menus (title, cost, count_dishes, colorfulness)
                VALUES (%s, %s, %s, %s)
                """,
                (menu["title"], menu["cost"], menu["count_dishes"], menu["colorfulness"]),
            )

        conn.commit()
        print(f"Inserted {len(menus)} menus into the database.")