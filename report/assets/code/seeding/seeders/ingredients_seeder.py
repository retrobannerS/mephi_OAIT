import csv
import os

def seed_ingredients(conn):
    file_path = os.path.join(os.path.dirname(__file__), "csv", "ingredients.csv")
    with open(file_path, "r") as file:
        reader = csv.DictReader(file)
        ingredients = []

        for row in reader:
            ingredient = {
                "title": row["title"],
                "type": row["type"],
                "cost": float(row["cost"]),
            }
            ingredients.append(ingredient)

    with conn.cursor() as cur:
        for ingredient in ingredients:
            cur.execute(
                """
                INSERT INTO ingredients (title, type, cost)
                VALUES (%s, %s, %s)
                """,
                (ingredient["title"], ingredient["type"], ingredient["cost"]),
            )
    conn.commit()
    print(f"Inserted {len(ingredients)} ingredients into the database.")