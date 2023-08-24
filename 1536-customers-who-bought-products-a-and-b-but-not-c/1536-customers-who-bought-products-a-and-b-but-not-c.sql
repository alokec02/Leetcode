# Write your MySQL query statement below

SELECT DISTINCT c.customer_id, c.customer_name 
FROM Customers c
JOIN Orders o ON c.customer_id = o.customer_id
WHERE c.customer_id IN (SELECT customer_id FROM Orders WHERE product_name = 'A')
AND c.customer_id IN (SELECT customer_id FROM Orders WHERE product_name = 'B')
AND c.customer_id NOT IN (SELECT customer_id FROM Orders WHERE product_name = 'C')