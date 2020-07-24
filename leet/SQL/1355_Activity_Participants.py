# option 1

# WITH cnt
#      AS (SELECT Count(*) AS act_count
#          FROM   friends
#          GROUP  BY activity)
# SELECT fr.activity
# FROM   friends fr
# GROUP  BY fr.activity
# HAVING Count(fr.activity) != (SELECT Min(act_count)
#                               FROM   cnt)
#        AND Count(fr.activity) != (SELECT Max(act_count)
#                                   FROM   cnt)

# Option 2
# SELECT fr.activity
# FROM   friends fr
# GROUP  BY fr.activity
# HAVING Count(fr.activity) != (SELECT Min(f.cnt)
#                               FROM   (SELECT Count(activity) AS cnt
#                                       FROM   friends
#                                       GROUP  BY activity) f)
#        AND Count(fr.activity) != (SELECT Max(f.cnt) AS max_cnt
#                                   FROM   (SELECT Count(activity) AS cnt
#                                           FROM   friends
#                                           GROUP  BY activity) f)