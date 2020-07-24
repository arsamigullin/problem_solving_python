# SELECT p.product_name,
#        Sum(o.unit) AS unit
# FROM   products p,
#        orders o
# WHERE  p.product_id = o.product_id
#        AND Year(o.order_date) = 2020
#        AND Month(o.order_date) = 2
# GROUP  BY p.product_id
# HAVING unit >= 100 