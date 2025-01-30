# Write your MySQL query statement below
SELECT unique_id, name
FROM Employees AS Emp
LEFT JOIN  EmployeeUNI AS EmpU
ON Emp.id = EmpU.id
