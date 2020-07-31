# SELECT business_id
# FROM   (SELECT *,
#                Avg(occurences)
#                  OVER (
#                    partition BY event_type) AS avg_occ
#         FROM   events) x
# WHERE  occurences > avg_occ
# GROUP  BY business_id
# HAVING Count(*) > 1



# Option 1 (my solution)
# SELECT s.business_id
# FROM   (SELECT *,
#                ( Sum(occurences)
#                    OVER(
#                      partition BY business_id, event_type ) ) AS occ, # this is redundant
#                ( Count(event_type)
#                    OVER(
#                      partition BY business_id) )              AS cnt, # this is redundant
#                ( Avg(occurences)
#                    OVER(
#                      partition BY event_type) )               AS av
#         FROM   events) s
# WHERE  s.cnt >= 2 # this is redundant
#        AND s.occ > s.av # this is redundant
# GROUP  BY s.business_id
# HAVING Count(s.business_id) >= 2