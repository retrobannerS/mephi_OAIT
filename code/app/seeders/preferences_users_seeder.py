import random

def seed_preferences_users(conn):
    with conn.cursor() as cur:
        cur.execute("SELECT id FROM users")
        users = cur.fetchall()

        cur.execute("SELECT id FROM preferences")
        preferences = cur.fetchall()

        users = [user[0] for user in users]
        preferences = [pref[0] for pref in preferences]

        for user in random.sample(users, int(len(users) * 0.3)):
            selected_prefs = random.sample(preferences, random.randint(1, 5))
            for pref_id in selected_prefs:
                cur.execute(
                    """
                    INSERT INTO preferences_users (user_id, preference_id)
                    VALUES (%s, %s)
                    """,
                    (user, pref_id),
                )
        conn.commit()
        print("Inserted preferences_users into the database.")