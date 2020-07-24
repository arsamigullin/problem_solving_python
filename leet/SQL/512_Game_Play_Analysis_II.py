
# option 1

#select a.player_id, a.device_id from activity a,
# (select player_id, min(event_date) as min_date from activity group by player_id) a1
# where a.player_id = a1.player_id and a.event_date = a1.min_date

# option 2
# Write your MySQL query statement below


#
# select player_id, device_id
# from
# (
# select *, row_number() over(partition by player_id order by event_date asc) as rn
# from Activity
# ) A
# where rn=1
# order by player_id asc
