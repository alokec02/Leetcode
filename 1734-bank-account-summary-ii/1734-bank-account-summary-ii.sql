# Write your MySQL query statement below

SELECT name, balance 
FROM
(SELECT DISTINCT u.account, u.name, sum(t.amount) OVER(PARTITION BY t.account) as balance 
FROM Users u
JOIN Transactions t ON u.account = t.account) t
WHERE balance > 10000