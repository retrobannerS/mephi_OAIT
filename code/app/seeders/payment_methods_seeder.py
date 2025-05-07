def seed_payment_methods(conn):
    payment_methods = [
        {
            "title": "Наличные курьеру",
            "require_requisites": False,
        },
        {
            "title": "Карта курьеру",
            "require_requisites": True,
        },
        {
            "title": "Карта",
            "require_requisites": True,
        },
        {
            "title": "Яндекс.Сплит",
            "require_requisites": True,
        },
    ]

    with conn.cursor() as cur:
        for method in payment_methods:
            cur.execute(
                """
                INSERT INTO payment_methods (title, require_requisites)
                VALUES (%s, %s)
                """,
                (method["title"], method["require_requisites"]),
            )
    conn.commit()
    print("Inserted payment methods into the database.")