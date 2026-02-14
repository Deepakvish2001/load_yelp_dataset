-- Which restaurants having highest number of review
SELECT
    name as restaurant_name,
    SUM(review_count) as review_count,
    ROUND(AVG(stars)::NUMERIC,5) as avg_rating
from restaurant_outlier
GROUP BY restaurant_name
ORDER BY review_count DESC
LIMIT 10