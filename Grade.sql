#create table Grade(
#	id int unsigned not null auto_increment primary key,
 #   midterm int unsigned not null default 0,
  #  finalterm int unsigned not null default 0,
   # enroll int unsigned not null default 0,
    #constraint foreign key fk_enroll(Enroll) references Enroll.(id)
    #on delete cascade 
#); 

insert into grade(enroll, midterm, finalterm) select id, ceil(rand()*100), ceil(rand()*100) from Enroll order by id asc limit 9999;

update grade
    SET midterm = midterm + 30 + ceil(rand()*10) where midterm between 0 and 30;
update grade
   SET finalterm = finalterm + 30 + ceil(rand()*10) where finalterm between 0 and 30;
            
#REPORT 1
select i.name, sbj.subject, g.midterm, g.finalterm, g.midterm + g.finalterm as total, (g.midterm + g.finalterm)/2  as avg,
    (CASE WHEN (g.midterm + g.finalterm)/2 >= 90 THEN 'A'
        WHEN (g.midterm + g.finalterm)/2 >= 80 and (g.midterm + g.finalterm)/2 < 90 THEN 'B'
       WHEN (g.midterm + g.finalterm)/2 >= 70 and (g.midterm + g.finalterm)/2 < 80 THEN 'C'
       WHEN (g.midterm + g.finalterm)/2 >= 60 and (g.midterm + g.finalterm)/2 < 70 THEN 'D'
       ELSE 'F'
       END) as '학점'
    from Enroll e inner join info i on e.student = i.id
   inner join Subjectname sbj on e.subjectname=sbj.id
   inner join grade g on e.id=g.id order by sbj.subject, avg desc;

#REPORT 2
select T1.subject, T2.mean as '과목당 평균', T1.avg as '최고 점수', T1.name, T2.count
From (select e.id as id, i.name as name, sbj.subject as subject, (g.midterm + g.finalterm)/2 as avg
    from Enroll e inner join info i on e.student = i.id
   inner join Subjectname sbj on e.subjectname=sbj.id
   inner join grade g on e.id=g.id) as T1,
   (select sbj.subject, AVG((g.midterm + g.finalterm)/2) as mean, MAX((g.midterm + g.finalterm)/2) as max , count(*) as count
    from Enroll e inner join info i on e.student = i.id
   inner join Subjectname sbj on e.subjectname=sbj.id
   inner join grade g on e.id=g.id group by e.subjectname) as T2
Where T1.avg = T2.max and T1.subject=T2.subject;

#REPORT 3
SELECT  T3.id as '학생ID', T3.name as '이름', T3.count '수강중인 과목수', T3.totalscore as'총점', T3.avg as '평균',
    (CASE WHEN T3.avg >= 90 THEN 'A'
        WHEN T3.avg >= 80 and T3.avg < 90 THEN 'B'
       WHEN T3.avg >= 70 and T3.avg < 80 THEN 'C'
       WHEN T3.avg >= 60 and T3.avg < 70 THEN 'D'
       ELSE 'F'
       END) as '학점'
FROM
(select i.id as id, i.name as name, count(*) as count, SUM(g.midterm) + SUM(g.finalterm) as totalscore, (AVG(g.midterm) + AVG(g.finalterm))/2 as avg
    from Enroll e inner join info i on e.student = i.id
   inner join Subjectname sbj on e.subjectname=sbj.id
   inner join grade g on e.id=g.id group by i.id ) as T3 order by T3.avg desc;






select sbj.subject, AVG((g.midterm + g.finalterm)/2) as mean, MAX((g.midterm + g.finalterm)/2) as max , count(*)
    from Enroll e inner join info i on e.student = i.id
   inner join Subjectname sbj on e.subjectname=sbj.id
   inner join grade g on e.id=g.id
group by e.subjectname;


select e.id as id, i.name as name, sbj.subject as subject, (g.midterm + g.finalterm)/2 as avg
    from Enroll e inner join info i on e.student = i.id
   inner join Subjectname sbj on e.subjectname=sbj.id
   inner join grade g on e.id=g.id;


select r2.id, r2.subject, group_concat(r2.name, r2.avg)
from
    (select e.id as id, i.name as name, sbj.subject as subject, (g.midterm + g.finalterm)/2 as avg
    from Enroll e inner join info i on e.student = i.id
   inner join Subjectname sbj on e.subjectname=sbj.id
   inner join grade g on e.id=g.id) as r2
where r2.avg = r2.vmax;



select * from grade;
select * from Subjectname;
select * from Enroll;

