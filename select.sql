SELECT * FROM dooodb.Student;
select * from Student where name like '배%%';
select * from Student where id in (1, 2);
select * from Student where id between 2 and 3;
select * from Student order by addr, name desc;
select * from Student where name between '바' and '빟';
select * from Student where email like 'a%' and tel like '010-9%';
select * from Student order by rand();
select * from Student where addr = '강원' order by birth desc limit 10, 15;
select addr, count(*) as cnt from Student group by addr order by cnt desc;

select addr, count(*) as cnt,avg(id) from Student group by addr order by cnt desc;

select addr, count(*) as cnt,avg(id) from Student group by addr have cnt > 330;

select name, birth,
	(case when birth like '7%' then '아재' when birth like '8%' then '젊은이' else '청춘' end) from Student;
    



select * from Student where email like 'a%' and tel like '010-9%';
select distinct(birth) s from Student s where birth='700601';
select * from Student order by addr, name desc;