# Write your MySQL query statement below
SELECT product_name, year, price
FROM Sales As S
LEFT JOIN Product AS P
ON S.product_id = P.product_id