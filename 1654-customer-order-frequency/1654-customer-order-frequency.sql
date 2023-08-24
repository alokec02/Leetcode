# Write your MySQL query statement below

SELECT customer_id, name
FROM
(
SELECT c.customer_id, c.name, p.product_id, p.price, o.order_id, o.order_date, o.quantity
FROM 
Customers c
JOIN Orders o ON c.customer_id = o.customer_id
JOIN Product p ON o.product_id = p.product_id
GROUP BY customer_id
HAVING sum(IF(left(order_date, 7)='2020-06', quantity*price, 0)) >= 100
AND sum(IF(left(order_date, 7)='2020-07', quantity*price, 0)) >= 100
) t1
