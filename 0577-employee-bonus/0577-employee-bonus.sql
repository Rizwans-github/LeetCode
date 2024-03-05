# Write your MySQL query statement below
SELECT name, bonus
FROM Employee
LEFT JOIN Bonus
ON Employee.empid = Bonus.empid
WHERE COALESCE(Bonus, 0) < 1000;