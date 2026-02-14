create View restaurant_outlier AS
with quatrile AS
(
    SELECT
        percentile_cont(0.25) within GROUP(ORDER BY review_count) as q1,
        percentile_cont(0.75) within GROUP(ORDER BY review_count) as q3
    from business
    where categories like '%Restaurant%' 
            AND is_open = 1
            AND review_count is NOT NULL
),
limits AS
(
    SELECT
        q1,
        q3,
        (q1 - 1.5*(q3-q1)) as lower_bound,
        (q3 + 1.5*(q3-q1)) as upper_bound
    from quatrile
)
SELECT
    b.*
from business b, limits l
where 
    b.categories LIKE '%Restaurant%'
    AND b.is_open = 1
    AND b.review_count IS NOT NULL
    AND b.review_count BETWEEN l.lower_bound AND l.upper_bound