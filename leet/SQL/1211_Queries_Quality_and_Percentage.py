# SELECT q.query_name,
#        Round(Avg(q.rating / q.position), 2) AS quality,
#        c.poor_query_percentage
# FROM   queries q,
#        (SELECT q.query_name,
#                Round(( 100 * COALESCE(qc.cnt, 0) / Count(*) ), 2) AS
#                poor_query_percentage
#         FROM   queries q
#                LEFT OUTER JOIN (SELECT query_name,
#                                        Count(*) AS cnt
#                                 FROM   queries
#                                 WHERE  rating < 3
#                                 GROUP  BY query_name) qc
#                             ON qc.query_name = q.query_name
#         GROUP  BY query_name) c
# WHERE  q.query_name = c.query_name
# GROUP  BY q.query_name


# SELECT query_name,
#        Round(Sum(rating / position) / Count(*), 2) quality,
#        Round(Sum(CASE
#                    WHEN rating < 3 THEN 1
#                    ELSE 0
#                  END) / Count(*) * 100, 2)         poor_query_percentage
# FROM   queries
# GROUP  BY query_name