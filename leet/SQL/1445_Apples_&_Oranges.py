# SELECT a.sale_date,
#        ( a.sold_num - o.sold_num ) AS diff
# FROM   (SELECT sale_date,
#                sold_num
#         FROM   sales
#         WHERE  fruit = 'apples') a,
#        (SELECT sale_date,
#                sold_num
#         FROM   sales
#         WHERE  fruit = 'oranges') o
# WHERE  a.sale_date = o.sale_date