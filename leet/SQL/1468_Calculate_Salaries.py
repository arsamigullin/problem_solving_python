# SELECT s.company_id,
#        s.employee_id,
#        s.employee_name,
#        Round(s.salary * se.tax) AS salary
# FROM   salaries s,
#        (SELECT sal.company_id,
#                ( CASE
#                    WHEN Max(sal.salary) < 1000 THEN 1.0
#                    WHEN Max(sal.salary) >= 1000
#                         AND Max(sal.salary) <= 10000 THEN 0.76
#                    WHEN Max(sal.salary) > 10000 THEN 0.51
#                  END ) AS tax
#         FROM   salaries sal
#         GROUP  BY sal.company_id) se
# WHERE  se.company_id = s.company_id
# ORDER  BY s.company_id,
#           s.employee_id