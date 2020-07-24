# # Write your MySQL query statement below
# select
# e.left_operand,
# e.operator,
# e.right_operand,
# (case
# when e.operator = '>' and v1.value > v2.value then 'true'
# when e.operator = '<' and v1.value < v2.value then 'true'
# when e.operator = '=' and v1.value = v2.value then 'true'
# else 'false' end) as value
# from expressions e, Variables v1,  Variables v2 where e.left_operand = v1.name and e.right_operand = v2.name