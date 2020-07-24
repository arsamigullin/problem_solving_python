# columns to rows

# option 1 (my solution)
# SELECT c.customer_id,
#        c.NAME
# FROM   customers c,
#        (SELECT customer_id,
#                Sum(CASE
#                      WHEN Month(o.order_date) = 6 THEN p.price * o.quantity
#                      ELSE NULL
#                    END) AS June,
#                Sum(CASE
#                      WHEN Month(o.order_date) = 7 THEN p.price * o.quantity
#                      ELSE NULL
#                    END) AS July
#         FROM   orders o,
#                product p
#         WHERE  o.product_id = p.product_id
#         GROUP  BY customer_id) AS Purch
# WHERE  Purch.customer_id = c.customer_id
#        AND COALESCE(Purch.june, 0) >= 100
#        AND COALESCE(Purch.july, 0) >= 100

# option 2
# SELECT customer_id,
#        NAME
# FROM   (SELECT c.NAME,
#                a.customer_id,
#                Sum(CASE
#                      WHEN Substring(order_date, 1, 7) = '2020-06' THEN quantity
#                      * price
#                    END) AS june,
#                Sum(CASE
#                      WHEN Substring(order_date, 1, 7) = '2020-07' THEN quantity
#                      * price
#                    END) AS july
#         FROM   orders a
#                LEFT JOIN product b
#                       ON a.product_id = b.product_id
#                LEFT JOIN customers c
#                       ON a.customer_id = c.customer_id
#         GROUP  BY 1,
#                   2) aa
# WHERE  june >= 100
#        AND july >= 100