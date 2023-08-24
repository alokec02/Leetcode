# Write your MySQL query statement below
SELECT DISTINCT sale_date, sum(quantity) OVER(PARTITION BY sale_date) as diff FROM (
SELECT sale_date, fruit, (
    CASE 
    WHEN fruit='apples' THEN sold_num
    WHEN fruit='oranges' THEN -sold_num
     END
) as quantity
FROM Sales ) t1
ORDER BY sale_date