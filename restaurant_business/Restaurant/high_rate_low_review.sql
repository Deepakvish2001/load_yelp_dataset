-- High rating but low review count Restaurant
WITH avg_review AS
(
    SELECT
        AVG(review_count) as avg_reviews
    from restaurant_outlier
)
select
    r.name,
    r.city,
    r.stars,
    r.review_count
from restaurant_outlier r, avg_review a
WHERE r.stars >=4.5
    AND r.review_count < a.avg_reviews
ORDER BY r.stars DESC, r.review_count