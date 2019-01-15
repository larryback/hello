select subject_name, sum(gender) from (
    select sbj.name, (case when s.gender = 1 then '남' else '여' end), count(*) 
      from Enroll e inner join subjects sbj on sbj.id = e.subjects
					inner join Student s on s.id = e.student 
                    where s.addr = '서울'
                    group by sbj.id., s.gender
                    order by sbj.name, s.gender desc0)sub
group by subject_name;
                    

# named은 인덱스가 없어서  소팅하는데 시간이 오래 걸린다. 대신에 sbj.id 로 하면 인덱스 기능이 있어서  소팅하는데 시간이 덜 걸린다.
# 서울지역 과목별 성별(남녀) 학생수.

insert into Test(id, name) values(10, "aaa");

insert ignore into Test(id, name) values(10, "aaa");

replace into Test(id, name) values(23, "aaa");

#과목명을 가나다 한줄로 쓴다.


select group_concate(name)
from subjects order by name;

select * from subject;

start transaction;

update Student set name = "111" where id = 1;


select group_concat(name) from subjects;

select avg(final_grade) from Grade;

# 임시 테이블을 활용하여 가나다순 과목별 한줄로 표현alter

create temporary table t_aaa(nm varchar(31));

insert into t_aaa(nm) select name from subjects order by name;

select group_concat(nm) from t_aaa;
