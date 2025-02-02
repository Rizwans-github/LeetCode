# Write your MySQL query statement below
SELECT w1.id AS ID
FROM Weather AS w1
INNER JOIN Weather AS w2
ON DATEDIFF(w1.recordDate, w2.recordDate) = 1
WHERE w1.temperature > w2.temperature;