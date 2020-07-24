# SELECT '[0-5>'           AS bin,
#        Count(session_id) AS total
# FROM   sessions
# WHERE  0 <= duration
#        AND duration < 300
# UNION
# SELECT '[5-10>'          AS bin,
#        Count(session_id) AS total
# FROM   sessions
# WHERE  300 <= duration
#        AND duration < 600
# UNION 
# SELECT '[10-15>'         AS bin,
#        Count(session_id) AS total
# FROM   sessions
# WHERE  600 <= duration
#        AND duration < 900
# UNION
# SELECT '15 or more'      AS bin,
#        Count(session_id) AS total
# FROM   sessions
# WHERE  900 <= duration