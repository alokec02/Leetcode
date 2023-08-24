# Write your MySQL query statement below

SELECT e.left_operand, e.operator, e.right_operand,
(
CASE 
    WHEN  e.operator = '>' AND v1.value > v2.value THEN 'true'
    WHEN  e.operator = '=' AND v1.value = v2.value THEN 'true'
    WHEN  e.operator = '<' AND v1.value < v2.value THEN 'true'
          ELSE 'false'
          END) as value
FROM Expressions e
JOIN Variables v1 ON v1.name = e.left_operand
JOIN Variables v2 ON v2.name = e.right_operand
