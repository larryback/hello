insert into Enroll(subject, student)
select sbj.id, s.id
  from (select id from Subject where id not in (select distinct subject from Enroll) order by id limit 1) sbj, 
       (select id from Student order by rand() limit 100) s;