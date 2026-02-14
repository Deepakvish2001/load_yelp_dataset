-- Best city for opening restaurant
select
    city,
    state,
    COUNT(*) as total_restaurant,
    ROUND(AVG(stars)::numeric,2) as avg_rating,
    sum(review_count) as total_review
from restaurant_outlier
where categories like '%Restaurant%' and is_open = 1
GROUP BY city, state
ORDER BY total_review DESC, avg_rating DESC
LIMIT 10