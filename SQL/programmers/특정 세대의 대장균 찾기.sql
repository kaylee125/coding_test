select e3.ID 
from ECOLI_DATA e1
inner join ECOLI_DATA e2
on e1.ID=e2.PARENT_ID and e1.PARENT_ID is null and e2.PARENT_ID is not null
inner join ECOLI_DATA e3
on e2.ID=e3.PARENT_ID
order by e3.ID