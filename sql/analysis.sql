-- 1. Total Revenue

SELECT
SUM(revenue) AS total_revenue
FROM orders;


-- 2. Total Orders

SELECT
COUNT(order_id) AS total_orders
FROM orders;


-- 3. Top 10 Customers

SELECT
customer_id,
customer_name,
SUM(revenue) AS total_spend

FROM orders

GROUP BY
customer_id,
customer_name

ORDER BY total_spend DESC

LIMIT 10;


-- 4. Sales by City

SELECT
city,
SUM(revenue) AS city_revenue

FROM orders

GROUP BY city

ORDER BY city_revenue DESC;