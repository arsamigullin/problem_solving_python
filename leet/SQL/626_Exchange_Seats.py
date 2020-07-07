# Write your MySQL query statement below
#select * from seat where id%2=0;
#select * from seat where id%2=1;


# option 1
# SELECT (CASE WHEN MOD(id,2)=1 AND id!=(SELECT COUNT(*) FROM seat) THEN id+1
# WHEN MOD(id,2)=0 THEN id-1
# ELSE id END)id, student
# FROM seat
# ORDER BY 1

# option2
# SELECT
#     (CASE
#         WHEN MOD(id, 2) != 0 AND counts != id THEN id + 1
#         WHEN MOD(id, 2) != 0 AND counts = id THEN id
#         ELSE id - 1
#     END) AS id,
#     student
# FROM
#     seat,
#     (SELECT
#         COUNT(*) AS counts
#     FROM
#         seat) AS seat_counts
# ORDER BY id ASC;

# option3
# SELECT
#     s1.id, COALESCE(s2.student, s1.student) AS student
# FROM
#     seat s1
#         LEFT JOIN
#     seat s2 ON ((s1.id + 1) ^ 1) - 1 = s2.id
# ORDER BY s1.id;