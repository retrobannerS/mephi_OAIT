import csv
import os

def seed_ingredients_preferences(conn):
    file_path = os.path.join(os.path.dirname(__file__), "csv", "ingredients_preferences.csv")
    with open(file_path, "r") as file:
        reader = csv.DictReader(file)
        values = []

        for row in reader:
            value = {
                "ingredient_id": row["ingredient_id"],
                "preference_id": row["preference_id"]
            }
            values.append(value)
    
    with conn.cursor() as cur:
        for value in values:
            cur.execute(
                """
                INSERT INTO ingredients_preferences (ingredient_id, preference_id)
                VALUES (%s, %s)
                """,
                (value["ingredient_id"], value["preference_id"]),
            )
    conn.commit()
    print(f"Inserted {len(values)} ingredients preferences into the database.")