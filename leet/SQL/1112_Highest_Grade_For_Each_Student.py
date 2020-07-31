# Option 1

# SELECT e.student_id,
#        Min(e.course_id) AS course_id,
#        e.grade
# FROM   enrollments e,
#        (SELECT student_id,
#                Max(grade) AS grade
#         FROM   enrollments
#         GROUP  BY student_id) g
# WHERE  e.student_id = g.student_id
#        AND e.grade = g.grade
# GROUP  BY e.student_id,
#           e.grade
# ORDER  BY e.student_id

# Option 2
# Write your MySQL query statement below
# SELECT
#     student_id, course_id, grade
# FROM (
#     SELECT
#     student_id, course_id, grade, ROW_NUMBER() OVER (PARTITION BY student_id ORDER BY grade DESC, course_id ASC) AS rn
# FROM enrollments
# ) ranked
# WHERE rn = 1
# ORDER BY student_id