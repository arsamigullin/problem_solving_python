# Option 1
# SELECT product_id, year AS first_year, quantity, price
# FROM
# (SELECT product_id, year, quantity, price,
# RANK() OVER (PARTITION BY product_id ORDER BY year ASC) AS yr_rank
# FROM sales) AS t
# WHERE yr_rank = 1

# Option 2
# select s.product_id,  a.first_year, s.quantity, s.price from Sales s join (select min(year) as first_year, product_id
# from Sales group by product_id) a on s.product_id = a.product_id and s.year = a.first_year