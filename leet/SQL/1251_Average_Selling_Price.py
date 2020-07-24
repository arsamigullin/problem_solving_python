# SELECT u.product_id,
#        Round(Sum(u.units * p.price) / Sum(u.units), 2) AS average_price
# FROM   prices p,
#        unitssold u
# WHERE  p.product_id = u.product_id
#        AND u.purchase_date BETWEEN p.start_date AND p.end_date
# GROUP  BY u.product_id 