import datetime
import random

def seed_dishes_menus(conn):
    today = datetime.date.today()
    date_range = [today + datetime.timedelta(days=i) for i in range(30)]

    with conn.cursor() as cur:
        # Получаем все меню
        cur.execute("SELECT id, count_dishes, colorfulness FROM menus")
        menus = cur.fetchall()  # список кортежей: (id, count_dishes, colorfulness)

        for date in date_range:
            for menu_id, count_dishes, max_color in menus:
                selected_dishes = []
                colorfulness_accumulated = 0

                while len(selected_dishes) < count_dishes:
                    # Выбираем блюда, которые вписываются в ограничения
                    cur.execute(
                        """
                        SELECT id, colorfulness FROM dishes
                        WHERE colorfulness <= %s
                        """,
                        (max_color - colorfulness_accumulated,)
                    )
                    dishes = cur.fetchall()  # [(id, colorfulness), ...]

                    if not dishes:
                        break  # нет подходящих блюд — выходим

                    dish = random.choice(dishes)

                    if colorfulness_accumulated + dish[1] <= max_color:
                        selected_dishes.append(dish)
                        colorfulness_accumulated += dish[1]

                # Добавляем выбранные блюда в таблицу
                for dish_id, _ in selected_dishes:
                    cur.execute(
                        """
                        INSERT INTO dishes_menus (dish_id, menu_id, date)
                        VALUES (%s, %s, %s)
                        """,
                        (dish_id, menu_id, date)
                    )

        conn.commit()