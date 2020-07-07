# Write your MySQL query statement below
#select  Name as Employee  from Employee e where exists (select 1 from Employee e1 where e.ManagerId = e1.Id and e.Salary > e1.Salary)