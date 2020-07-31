# SELECT p.project_id,
#        e.employee_id
# FROM   (SELECT p.project_id,
#                Max(experience_years) max_years
#         FROM   project p,
#                employee e
#         WHERE  p.employee_id = e.employee_id
#         GROUP  BY p.project_id) pe,
#        project p,
#        employee e
# WHERE  e.employee_id = p.employee_id
#        AND p.project_id = pe.project_id
#        AND e.experience_years = pe.max_years