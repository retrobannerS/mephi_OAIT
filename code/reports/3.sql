WITH 
    max_count_pair AS (
        SELECT DISTINCT
            ARRAY[dm1.dish_id, dm2.dish_id] AS pair,
            COUNT(*) AS count
        FROM
            dishes_menus dm1 JOIN dishes_menus dm2 USING(menu_id, date)
        WHERE 
            dm1.dish_id < dm2.dish_id
        GROUP BY
            pair
    )

SELECT
    d1.id AS id1,
    d2.id AS id2,
    count
FROM
    max_count_pair 
    JOIN dishes d1 ON pair[1] = d1.id
    JOIN dishes d2 ON pair[2] = d2.id