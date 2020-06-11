# select distinct employee_id
# from Employees
# where manager_id in (
#                     select distinct employee_id
#                     from Employees
#                     where manager_id in(
#                                         select employee_id
#                                         from Employees
#                                         where manager_id = 1
#                                         )
#                     ) and employee_id != 1



# WITH RECURSIVE CTE AS (
#     SELECT employee_id, 1 as lvl
#     FROM Employees
#     WHERE manager_id = 1 AND employee_id != 1
#     UNION ALL
#     SELECT e.employee_id, c.lvl + 1 as lvl
#     FROM CTE c INNER JOIN Employees e ON c.employee_id = e.manager_id
# )
# SELECT employee_id
# FROM CTE
# WHERE lvl <= 3
# ORDER BY employee_id;