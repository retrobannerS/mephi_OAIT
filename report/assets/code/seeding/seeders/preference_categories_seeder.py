def seed_preference_categories(conn):
    categories = [
        "аллергены",
        "десерты, выпечка, сахар",
        "мясо, рыба",
        "овощи, лук, чеснок",
        "гарниры, каши"
    ]
    with conn.cursor() as cur:
        for category in categories:
            cur.execute(
                """
                INSERT INTO preference_categories (title)
                VALUES (%s)
                """,
                (category,),
            )
        conn.commit()
        print(f"Inserted {len(categories)} preference categories into the database.")