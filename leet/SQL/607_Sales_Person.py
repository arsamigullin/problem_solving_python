# select s.name from salesperson s where not exists
# (select 1 from orders o, company c where o.sales_id = s.sales_id and c.com_id = o.com_id and c.name='RED')