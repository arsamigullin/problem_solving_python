# my solution
# WITH sal
#      AS (SELECT seller_id,
#                 Sum(price) AS price
#          FROM   sales
#          GROUP  BY seller_id)
# SELECT sal.seller_id
# FROM   sal
# WHERE  sal.price = (SELECT Max(price) FROM   sal)

# over by rank solution
# SELECT seller_id
# FROM   (SELECT seller_id,
#                Rank()
#                  OVER (
#                    ORDER BY Sum(price) DESC) rk
#         FROM   sales
#         GROUP  BY seller_id) s
# WHERE  s.rk = 1