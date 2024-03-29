# Write your MySQL query statement below
SELECT ROUND(SUM(IF(order_date = customer_pref_delivery_date, 1, 0)) / 
COUNT(DISTINCT customer_id) * 100, 2) AS Immediate_percentage
FROM Delivery
WHERE (customer_id, order_date) IN (
    SELECT customer_id, MIN(order_date) AS first_order
    FROM Delivery
    GROUP BY customer_id
);