# SELECT ss.student_id,
#        ss.student_name,
#        ss.subject_name,
#        Count(e.subject_name) AS attended_exams

# here we shuffle all possible options between students and subjects
# in other words we do cartesian products
# FROM   (SELECT *
#         FROM   students,
#                subjects) ss

# here we do left join on student id and subject_name
# doint left join only by one field will case duplication 
#        LEFT OUTER JOIN examinations e
#                     ON ss.student_id = e.student_id
#                        AND ss.subject_name = e.subject_name
# GROUP  BY ss.student_id,
#           ss.subject_name
# ORDER  BY ss.student_id,
#           ss.subject_name