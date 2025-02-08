# Write your MySQL query statement below
SELECT S.user_id, IFNULL(ROUND(SUM(action= 'confirmed')/ COUNT(*), 2), 0.00) AS confirmation_rate
FROM Signups AS S
LEFT JOIN Confirmations AS C
ON S.user_id = C.user_id
GROUP BY S.user_id;