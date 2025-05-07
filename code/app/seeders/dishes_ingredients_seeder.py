import os
import csv

def seed_dishes_ingredients(conn):
    file_path = os.path.join(os.path.dirname(__file__), "csv", "dishes_ingredients.csv")
    with open(file_path, "r") as file:
        reader = csv.DictReader(file)
        values = []

        for row in reader:
            value = {
                "dish_id": row["dish_id"],
                "ingredient_id": row["ingredient_id"],
            }
            values.append(value)

    with conn.cursor() as cur:
        cur.executemany(
            """
            INSERT INTO dishes_ingredients (dish_id, ingredient_id)
            VALUES (%s, %s)
            """,
            [(value["dish_id"], value["ingredient_id"]) for value in values]
        )
        conn.commit()
    print(f"Inserted {len(values)} dishes_ingredients into the database.")