SELECT
    bonuses,
    COUNT(*) AS count
FROM
    users
GROUP BY
    bonuses
ORDER BY
    bonuses ASC;