import csv
import os

def seed_dishes(conn):
    file_path = os.path.join(os.path.dirname(__file__), "csv", "dishes.csv")
    with open(file_path, "r") as file:
        reader = csv.DictReader(file)
        dishes = []

        for row in reader:
            dish = {
                "title": row["title"],
                "type": row["type"],
                "weight": float(row["weight"]),
                "colorfulness": float(row["colorfulness"]),
            }
            dishes.append(dish)
    with conn.cursor() as cur:
        for dish in dishes:
            cur.execute(
                """
                INSERT INTO dishes (title, type, weight, colorfulness)
                VALUES (%s, %s, %s, %s)
                """,
                (dish["title"], dish["type"], dish["weight"], dish["colorfulness"]),
            )
    conn.commit()
    print(f"Inserted {len(dishes)} dishes into the database.")