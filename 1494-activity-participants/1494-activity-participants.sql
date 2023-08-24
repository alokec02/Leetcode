# Write your MySQL query statement below
WITH Temp AS
(SELECT activity, count(id) OVER(PARTITION BY activity) as People
FROM Friends
) 
SELECT DISTINCT activity FROM TEMP
WHERE People <> (SELECT MAX(People) FROM Temp)
AND People <> (SELECT MIN(People) FROM Temp)




