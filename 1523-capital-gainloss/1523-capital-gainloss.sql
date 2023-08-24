# Write your MySQL query statement below
WITH CTE1 AS (
SELECT stock_name, Amount*-1 as amount   FROM
(SELECT DISTINCT stock_name, operation, sum(price) OVER(PARTITION BY stock_name, operation) AS Amount
FROM Stocks) t1
WHERE Operation = 'Buy'
UNION ALL
SELECT stock_name, Amount as amount FROM
(SELECT DISTINCT stock_name, operation, sum(price) OVER(PARTITION BY stock_name, operation) AS Amount
FROM Stocks) t2
WHERE Operation = 'SELL'
)
SELECT DISTINCT stock_name, sum(amount) OVER (PARTITION BY stock_name) AS capital_gain_loss
FROM CTE1