# Write your MySQL query statement below
SELECT product_id
FROM Products
-- Just a reminder for me I tend to use == twice which is incorrect
WHERE (low_fats = "Y") & (recyclable = "Y");