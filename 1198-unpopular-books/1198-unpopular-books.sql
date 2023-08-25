# Write your MySQL query statement below

SELECT book_id, name
FROM Books 
WHERE available_from < '2019-05-23' AND book_id NOT IN 
(
SELECT book_id FROM
(
SELECT book_id, sum(quantity) OVER(PARTITION BY book_id) as Total
FROM Orders
WHERE dispatch_date BETWEEN '2018-06-23' AND '2019-06-23' 
) t1
WHERE Total >= 10
)



