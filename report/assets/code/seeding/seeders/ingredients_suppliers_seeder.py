import random

def seed_ingredients_suppliers(conn):
    with conn.cursor() as cur:
        cur.execute("SELECT id FROM ingredients")
        ingredients = cur.fetchall()

        cur.execute("SELECT id FROM suppliers")
        suppliers = cur.fetchall()

        ingredients_suppliers = []
        for ingredient in ingredients:
            random_suppliers = random.sample(suppliers, k=random.randint(1, 5))

            for supplier in random_suppliers:
                ingredients_suppliers.append(
                    (ingredient[0], supplier[0])
                )
        
        cur.executemany(
            """
            INSERT INTO ingredients_suppliers (ingredient_id, supplier_id)
            VALUES (%s, %s)
            """,
            ingredients_suppliers
        )
        conn.commit()
        print(f"Inserted {len(ingredients_suppliers)} ingredients-suppliers into the database.")

