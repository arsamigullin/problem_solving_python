#cumulative sum

#
# SELECT   pt.person_name
# FROM     (
#                   SELECT   *, 
#                            (Sum(weight) OVER(ORDER BY turn )) AS cum
#                   FROM     queue
#                   ORDER BY turn) pt
# WHERE    pt.cum <= 1000
# ORDER BY pt.turn DESC limit 1



# SELECT   q.person_name
# FROM     ( SELECT   *, (Sum(weight) OVER(ORDER BY turn )) AS cum
#            FROM     queue
#            ORDER BY turn) pt,
#          queue q
# WHERE    pt.cum <= 1000
# AND      pt.person_id = q.person_id
# ORDER BY pt.turn DESC limit 1