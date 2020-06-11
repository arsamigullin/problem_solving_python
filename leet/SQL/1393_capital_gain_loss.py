# Write your MySQL query statement below
# # SELECT f.stock_name, (f.sell - s.buy) as capital_gain_loss FROM (SELECT stock_name, sum(price) as sell FROM Stocks
# WHERE operation = 'Sell' GROUP BY stock_name) as f, (SELECT stock_name, sum(price) as buy
# FROM Stocks WHERE operation = 'Buy' GROUP BY stock_name) as s WHERE f.stock_name = s.stock_name
# #

# this version is much shorter
# # select stock_name,sum(if(operation = 'Sell',price,-price))capital_gain_loss
# # from Stocks
# # group by stock_name

# Write your MySQL query statement below
# select a.stock_name, sum(a.price) as capital_gain_loss
# from(
# select stock_name,
# case when operation = 'buy' then -sum(price)
# when operation = 'sell' then sum(price) end as price
# from stocks
# group by stock_name, operation) a
# group by a.stock_name