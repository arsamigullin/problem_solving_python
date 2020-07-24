# Write your MySQL query statement below

# Option1
# SELECT Round((SELECT Count(*)
#               FROM   activity a,
#                      (SELECT player_id,
#                              Min(event_date) AS min_date
#                       FROM   activity
#                       GROUP  BY player_id) a1
#               WHERE  a.player_id = a1.player_id
#                      AND Date_add(a1.min_date, INTERVAL 1 day) = a.event_date) /
#              (
#                     SELECT Count(DISTINCT player_id)
#                     FROM
#                           activity), 2) AS fraction

# Option2
# # Write your MySQL query statement below
# SELECT Round(Count(DISTINCT player_id) / (SELECT Count(DISTINCT player_id)
#                                           FROM   activity), 2) AS fraction
# FROM   activity
# WHERE  ( player_id, Date_sub(event_date, INTERVAL 1 day) ) IN
#               (SELECT player_id,
#                Min(event_date) AS first_login
#                                                                FROM   activity
#               GROUP  BY player_id)


 #Option 3
# SELECT Round(Count(DISTINCT player_id) / (SELECT Count(DISTINCT player_id)
#                                           FROM   activity), 2) AS fraction
# FROM   activity
# WHERE  ( player_id, Date_sub(event_date, INTERVAL 1 day) ) IN
#               (SELECT player_id,
#                Min(event_date) AS first_login
#                                                                FROM   activity
#               GROUP  BY player_id)