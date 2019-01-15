SELECT * FROM dooodb.Student;
alter table Student add column gender bit not null default 0;
update Student set gender = mod(id, 2) where id > 0;


update Student set gender = (case when name like '%솔%' or name like '%혜%'
or name like '%현%' or anme like '%영%'
or name like '%희%' or anme like '%주%' then 0 else 1 end);


update Student set gender = 1 
where not (name like '%솔%' or name like '%혜%'
or name like '%현%' or anme like '%영%'
or name like '%희%' or anme like '%주%')
and id > 0;
select gender, count(*) from Student group by gender;