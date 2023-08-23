WITH CTE1 as (
  SELECT u.name, dense_rank() OVER (order by count(m.movie_id) desc, u.name asc) as rank1
  FROM MovieRating m
  JOIN Users u ON u.user_id = m.user_id
  GROUP BY u.user_id
),

CTE2 as
(
Select m2.title, dense_rank() over(order by avg(rating) desc, m2.title asc) as rank2 
from MovieRating m1
JOIN Movies m2
ON m1.movie_id = m2.movie_id
where m1.created_at between '2020-02-01' and '2020-02-29'
GROUP BY m1.movie_id
)

SELECT name AS results 
FROM CTE1
WHERE rank1 = 1

UNION ALL

SELECT title AS results
FROM CTE2
WHERE rank2 = 1

