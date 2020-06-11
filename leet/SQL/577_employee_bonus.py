

#select e.name, b. bonus from Employee e left outer join bonus b on e.empId = b.empId where coalesce(b.bonus,0) < 1000