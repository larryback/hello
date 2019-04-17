select max (sbj.name) sbj_name, avg(g.midterm + g.finalterm) / 2 aver, count(*) stu_cnt,
	(select enroll from Grade ggg inner join Enroll eee on ggg.finalterm)