# Write your MySQL query statement below
SELECT customer_id, COUNT( customer_id) AS count_no_trans
FROM Visits
LEFT JOIN Transactions
ON Visits.visit_id = Transactions.visit_id
WHERE COALESCE(transaction_id, 0) = 0
GROUP BY customer_id;