/* Write your T-SQL query statement below */
-- https://leetcode.com/problems/list-the-products-ordered-in-a-period/submissions/
WITH product_counts AS (
SELECT product_id, SUM(unit) as unit
    from Orders
    WHERE order_date < '2020-03-01' AND order_date > '2020-01-31'
    GROUP BY product_id
)
SELECT product_name, unit 
FROM Products
INNER JOIN product_counts pc ON pc.product_id = Products.product_id
WHERE unit >= 100

