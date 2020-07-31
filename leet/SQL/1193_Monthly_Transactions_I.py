# SELECT tot.month,
#        tot.country,
#        tot.trans_count,
#        COALESCE(ap.approved_count, 0)        AS approved_count,
#        tot.trans_total_amount,
#        COALESCE(ap.approved_total_amount, 0) AS approved_total_amount
# FROM   (SELECT Date_format(trans_date, "%y-%m") AS month,
#                country,
#                Count(*)                         AS trans_count,
#                Sum(amount)                      AS trans_total_amount
#         FROM   transactions
#         GROUP  BY country,
#                   Date_format(trans_date, "%y-%m")) tot
#        LEFT OUTER JOIN (SELECT Date_format(trans_date, "%y-%m") AS month,
#                                country,
#                                Count(*)                         AS
#                                approved_count,
#                                Sum(amount)                      AS
#        approved_total_amount
#                         FROM   transactions
#                         WHERE  state = 'approved'
#                         GROUP  BY country,
#                                   Date_format(trans_date, "%y-%m")) ap
#                     ON tot.month = ap.month
#                        AND tot.country = ap.country