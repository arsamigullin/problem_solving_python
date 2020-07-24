# SELECT Min(log_id) AS start_id,
#        Max(log_id) AS end_id
# FROM   (SELECT log_id,
#                ( log_id - Dense_rank() OVER(ORDER BY log_id) ) AS row_ranking
#         FROM   logs) AS temp
# GROUP  BY row_ranking
# ORDER  BY start_id

'''
Consider this example
log_id
1
2
3
7
8
10

to group contiguous ranges in the FROM clause we use dense_rank() which does not have gaps (like usual rank())
so, in FROM clause we will have this
log_id   log_id - Dense_rank()
1           1 - 1 = 0
2           2 - 2 = 0
3           3 - 3 = 0
7           7 - 4 = 3
8           8 - 5 = 3
10          10 - 6 = 4
'''