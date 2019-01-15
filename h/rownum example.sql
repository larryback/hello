select (@rownum := @rownum + 1) as '석차', stu.name '학생명', average
 from (
   select e.student, sum(g.midterm) mterm, sum(g.finalterm) fterm,
    avg((g.midterm + g.finalterm)/2) average, count(*) sbj_cnt
     from Grade g inner join Enroll e on g.enroll = e.id
    group by e.student) sub
   inner join Student stu
           on sub.student = stu.id, (select @rownum := 0) ttt
order by sub.average desc, sbj_cnt desc;

select (@rownum := @rownum + 1) as '석차', stu.name '학생명', average
  from (
    select e.student, sum(g.midterm) mterm, sum(g.finalterm) fterm,
           avg((g.midterm + g.finalterm) / 2) average, count(*) sbj_cnt
      from Grade g inner join Enroll e on g.enroll = e.id
     group by e.student) sub
    inner join Student stu
            on sub.student = stu.id, (select @rownum := 0) ttt
 order by sub.average desc, sbj_cnt desc;
