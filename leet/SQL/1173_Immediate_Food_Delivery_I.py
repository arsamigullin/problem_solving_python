# SELECT Round(100 * Count(*) / (SELECT Count(*)
#                                FROM   delivery), 2) AS immediate_percentage
# FROM   delivery
# WHERE  order_date = customer_pref_delivery_date