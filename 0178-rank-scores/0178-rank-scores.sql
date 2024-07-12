/* Write your T-SQL query statement below */

WITH score_rank as (

    SELECT
    score,
    DENSE_RANK() OVER (ORDER BY score DESC) as rank
    FROM Scores
    )
    

    SELECT score, rank
    FROM score_rank
    ORDER BY rank