# SELECT
#     customer_number
# FROM
#     orders
# GROUP BY customer_number
# ORDER BY COUNT(*) DESC
# LIMIT 1
# ;


# SELECT customer_number FROM orders
# GROUP BY customer_number
# HAVING COUNT(customer_number)= (SELECT MAX(a.Total)
#                                 FROM (SELECT COUNT(customer_number) AS Total
#                                       FROM orders
#                                       GROUP BY customer_number) a)